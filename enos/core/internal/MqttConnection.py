import logging
import sched
import threading
import time
from enum import Enum

from enos.core.constant.ResponseCode import ResponseCode
from enos.core.exception.EnvisionException import EnvisionException
from enos.core.internal.DefaultProcessor import DefaultProcessor
from enos.core.internal.Profile import Profile
from enos.core.internal.ResponseToken import ResponseToken
from enos.core.internal.SecureMode import VIA_PRODUCT_SECRET, VIA_DEVICE_SECRET
from enos.core.message.BaseRequest import BaseRequest
from enos.core.message.IMessageHandler import IMessageHandler
from enos.core.message.IResponseCallback import IResponseCallback
from enos.core.util.ConcurrentDict import ConcurrentDict
from enos.core.util.StringUtil import StringUtil
from enos.message.downstream.activate.DeviceActivateCommand import DeviceActivateCommand
from enos.message.downstream.activate.DeviceActivateReply import DeviceActivateReply
from enos.message.upstream.status.SubDeviceLoginRequest import SubDeviceLoginRequest
from enos.core.util.ConcurrentSet import ConcurrentSet
import paho.mqtt.client as mqtt

from enos.message.upstream.status.SubDeviceLogoutRequest import SubDeviceLogoutRequest


class MqttConnection(object):
    __logger = logging.getLogger(__name__)
    __request_id = 0
    __lock = threading.Lock()
    __connect_timeout = 10

    class State(Enum):
        NOT_CONNECTED = 0
        CONNECTING = 1
        CONNECTED = 2
        DISCONNECTED = 3
        CLOSED = 4

    def __init__(self, profile):
        self.__profile = profile
        self.__mqtt_processor = DefaultProcessor(self, self.__profile)
        self.__state = MqttConnection.State.NOT_CONNECTED
        self.__subscribed_topic_cache = ConcurrentSet()
        self.__logined_sub_device = ConcurrentDict()
        self.__paho_client = None
        self.__connection_condition = threading.Condition()
        self.__client_lock = threading.RLock()

        # user callbacks
        self.__on_device_dynamic_active = None
        self.__on_connect = None
        self.__on_disconnect = None
        self.__on_connect_failed = None

    @property
    def on_device_dynamic_active(self):
        return self.__on_internal_device_dynamic_activate

    @on_device_dynamic_active.setter
    def on_device_dynamic_active(self, value):
        self.__on_device_dynamic_active = value

    @property
    def on_connect(self):
        return self.__on_connect

    @on_connect.setter
    def on_connect(self, value):
        self.__on_connect = value

    @property
    def on_disconnect(self):
        return self.__on_disconnect

    @on_disconnect.setter
    def on_disconnect(self, value):
        self.__on_disconnect = value

    @property
    def on_connect_failed(self):
        return self.__on_connect_failed

    @on_connect_failed.setter
    def on_connect_failed(self, value):
        self.__on_connect_failed = value

    def connect(self):
        with self.__client_lock:
            if self.__state != MqttConnection.State.NOT_CONNECTED:
                raise EnvisionException('connect is not allowed at illegal state: ' + str(self.__state))

        rc = self.__do_connect()
        if rc == 0:
            with self.__connection_condition:
                got_it = self.__connection_condition.wait(MqttConnection.__connect_timeout)
                if not got_it:
                    MqttConnection.__logger.error('Client id: [{}] connect timeout'
                                                  .format(self.__profile.get_client_id()))

    def connect_async(self):
        with self.__client_lock:
            if self.__state != MqttConnection.State.NOT_CONNECTED:
                raise EnvisionException('connect is not allowed at illegal state: ' + str(self.__state))

            self.__state = MqttConnection.State.CONNECTING
            self.__initialize_underlying_client()
            self.__create_connection_options()

            self.__paho_client.connect_async(host=self.__profile.get_host(), port=self.__profile.get_port(),
                                             keepalive=self.__profile.get_keep_alive_interval())
            self.__paho_client.loop_start()

    def reconnect(self):
        with self.__client_lock:
            if self.__state != MqttConnection.State.CONNECTED and self.__state != MqttConnection.State.DISCONNECTED:
                raise EnvisionException('reconnect is not allowed at illegal state: ' + str(self.__state))

            self.__disconnect_underlying_client()
            self.__state = MqttConnection.State.DISCONNECTED

            self.__do_connect()
            with self.__connection_condition:
                got_it = self.__connection_condition.wait(MqttConnection.__connect_timeout)
                if not got_it:
                    MqttConnection.__logger.error('Client id: [{}] connect timeout'
                                                  .format(self.__profile.get_client_id()))

    def __do_connect(self):
        try:
            self.__initialize_underlying_client()
            self.__create_connection_options()

            rc = self.__paho_client.connect(host=self.__profile.get_host(), port=self.__profile.get_port(),
                                            keepalive=self.__profile.get_keep_alive_interval())
            if rc == 0:
                self.__paho_client.loop_start()
            return rc
        except Exception as e:
            MqttConnection.__logger.error('connect failed,  url: {}, err : ' + self.__profile.get_server_url() + str(e))

            self.__state = MqttConnection.State.NOT_CONNECTED

            self.__disconnect_underlying_client()

            if self.__on_connect_failed is not None:
                self.__mqtt_processor.get_executor().submit(self.__on_connect_failed)

            raise EnvisionException('failed to connect: ' + self.__profile.get_server_url() + str(e))

    def __initialize_underlying_client(self):
        self.__paho_client = mqtt.Client(client_id=self.__profile.get_client_id(),
                                         clean_session=self.__profile.get_mqtt_clean_session(),
                                         protocol=Profile.MQTTv3_1_1)
        self.__load_callbacks()

        # register device dynamic activation handler
        if self.__profile.get_secure_mode().get_mode_id() == VIA_PRODUCT_SECRET:
            self.__register_device_activate_info_command()

    def __create_connection_options(self):
        # set ssl
        if self.__profile.get_ssl_secured():
            ssl_context = self.__profile.create_ssl_context()
            self.__paho_client.tls_set_context(ssl_context)

        # set username and password
        self.__paho_client.username_pw_set(self.__profile.get_mqtt_username(), self.__profile.get_mqtt_password())
        # auto reconnect set
        if self.__profile.get_auto_reconnect():
            self.__paho_client.reconnect_delay_set(self.__profile.get_auto_reconnect_min_sec(),
                                                   self.__profile.get_auto_reconnect_max_sec())
        self.__paho_client.max_queued_messages_set(self.__profile.get_max_queued_message())
        self.__paho_client.max_inflight_messages_set(self.__profile.get_max_inflight_message())

    def __register_device_activate_info_command(self):
        default_activate_handler = IMessageHandler()
        default_activate_handler.on_message = self.__on_internal_device_dynamic_activate
        self.__mqtt_processor.set_arrived_msg_handler(DeviceActivateCommand.get_class(), default_activate_handler)

    def is_connected(self):
        return self.__paho_client.is_connected()

    def disconnect(self):
        with self.__client_lock:
            if self.__state == MqttConnection.State.DISCONNECTED:
                MqttConnection.__logger.warning('connection is already disconnected')
                return

            if self.__state != MqttConnection.State.CONNECTED:
                raise EnvisionException('client is not at connected state: ' + str(self.__state))

            self.__disconnect_underlying_client()

            self.__state = MqttConnection.State.DISCONNECTED

    def close(self):
        """ Close client and release related resources"""
        with self.__client_lock:
            if self.__state == MqttConnection.State.CLOSED:
                MqttConnection.__logger.warning('connection is already closed')
                return

            self.__disconnect_underlying_client()

            self.get_processor().get_executor().shutdown()

            self.__paho_client = None

            self.__state = MqttConnection.State.CLOSED

    def __disconnect_underlying_client(self):
        # always clean the subscribed cache if disconnect the client
        self.__subscribed_topic_cache.clear()
        try:
            if self.__paho_client is not None and self.__paho_client.is_connected():
                self.__paho_client.disconnect()
                self.__paho_client.loop_stop()
        except Exception as e:
            MqttConnection.__logger.error('failed to close the underlying transport' + str(e))

    def fast_publish(self, delivery):
        if self.__state != MqttConnection.State.CONNECTED:
            raise EnvisionException('fast publish is not allowed at state: {}, method is: {}'
                                    .format(self.__state, delivery.get_method()))
        try:
            self.__fill_request(delivery)
            delivery.check()
            self.__do_fast_publish(delivery)
            self.__post_publish(delivery)
        except Exception as e:
            raise EnvisionException('fast publish failed: {}'.format(str(e)))

    def publish(self, request):
        """ This method blocks until the response is received or action timeout is reached"""
        if self.__state != MqttConnection.State.CONNECTED:
            raise EnvisionException('publish is not allowed at state: {}, method is: {}'
                                    .format(self.__state, request.get_method()))
        try:
            self.__fill_request(request)
            request.check()
            self.__subscribe_response_if_needed(request)

            token = self.__get_token(request)
            self.get_processor().register_response_token(token.get_response_id(), token)

            try:
                self.__do_fast_publish(request)
                if token is None:
                    raise EnvisionException('response token not set')
                response = token.wait_for_response(self.__profile.get_operation_timeout())
            except Exception as e:
                MqttConnection.__logger.error('[sync] publish error: {}, topic is: {}'
                                              .format(str(e), request.get_message_topic()))
                if token is not None:
                    self.get_processor().deregister_response_token(token.get_response_id())
                    token.mark_failure(e)
                raise e

            self.__post_publish(request, response)

            return response
        except Exception as e:
            raise EnvisionException('[sync] publish error: {}, topic is {}'
                                    .format(str(e), request.get_message_topic()))

    def async_publish(self, request, callback=None):
        """ Publish asynchronous without block,
            user should check if request is success with callback extends ResponseCallback"""
        if self.__state != MqttConnection.State.CONNECTED:
            raise EnvisionException('async publish is not allowed at state: {}, method is: {}'
                                    .format(self.__state, request.get_method()))
        if callback is None:
            self.fast_publish(request)

        try:
            self.__fill_request(request)
            request.check()
            self.__subscribe_response_if_needed(request)

            token = self.__get_token_with_callback(request, callback)
            self.get_processor().register_response_token(token.get_response_id(), token)

            try:
                self.__do_fast_publish(request)
                if token is None:
                    raise EnvisionException('response token not set')
                self.__mqtt_processor.get_executor().submit(
                    token.wait_for_response(self.__profile.get_operation_timeout()))
            except Exception as e:
                if token is not None:
                    self.get_processor().deregister_response_token(token.get_response_id())
                    token.mark_failure(e)
                else:
                    callback.on_failure()

        except Exception as e:
            raise EnvisionException('[async] publish error: {}, topic is {}'
                                    .format(str(e), request.get_message_topic()))

    def __do_fast_publish(self, delivery):
        """ Deliver request or reply to broker.
            This method blocks until request is sent out and mqtt ack is returned without response"""
        try:
            if self.__paho_client.is_connected():
                if delivery.get_qos() == 0 or delivery.get_qos() == 1:
                    self.__paho_client.publish(delivery.get_message_topic(), delivery.encode(), delivery.get_qos())
                elif delivery.get_qos() == 2:
                    raise EnvisionException('qos 2 not allowed')
                else:
                    raise EnvisionException('invalid qos!')
        except Exception as e:
            raise EnvisionException('publish message failed, message topic: {} \n error message: {}'
                                    .format(delivery.get_message_topic(), str(e)))

    def __fill_request(self, request):
        if StringUtil.is_empty(request.get_id()):
            request.set_id(str(MqttConnection.inc_and_get_message_id()))

        # If publish reply, version is not request
        if isinstance(request, BaseRequest) and StringUtil.is_empty(request.get_version()):
            request.set_version(Profile.VERSION)

        if StringUtil.is_empty(request.get_product_key()) and StringUtil.is_empty(request.get_device_key()):
            request.set_product_key(self.__profile.get_product_key())
            request.set_device_key(self.__profile.get_device_key())

    def __subscribe_response_if_needed(self, request):
        """ Subscribe answer topic if not cached"""
        topic = request.get_answer_topic()
        if not self.__subscribed_topic_cache.exists(topic):
            self.__paho_client.subscribe(topic, request.get_qos())
            self.__subscribed_topic_cache.add(topic)

    def __post_publish(self, request, response=None):
        if self.__profile.get_auto_reconnect() and self.__profile.get_auto_login_sub_device():
            if isinstance(request, SubDeviceLoginRequest) and (response is None or response.is_success()):
                self.__logined_sub_device.add(request.get_device_credential().get_device_key(),
                                              request.get_device_credential())
            elif isinstance(request, SubDeviceLogoutRequest) and (response is None or response.is_success()):
                self.__logined_sub_device.pop(request.get_device_key())

    def __get_token(self, request):
        return ResponseToken(self.get_answer_topic(request))

    def __get_token_with_callback(self, request, callback):
        """ Wrap the original callback to support timeout feature"""
        answer_topic = self.get_answer_topic(request)

        # schedule when timeout
        def timeout_schedule_task():
            self.get_processor().deregister_response_token(answer_topic)
            callback.on_failure(EnvisionException('call back task timeout'))

        scheduler = sched.scheduler(time.time, time.sleep)
        event = scheduler.enter(self.__profile.get_operation_timeout(),
                                priority=1, action=timeout_schedule_task, argument=())

        def on_response(response):
            callback.on_response(response)
            scheduler.cancel(event)

        def on_failure(exception):
            callback.on_failure(exception)
            scheduler.cancel(event)

        wrapped_callback = IResponseCallback()
        wrapped_callback.on_response = on_response
        wrapped_callback.on_failure = on_failure

        return ResponseToken(self.get_answer_topic(request), wrapped_callback)

    def __on_internal_connect(self, client, user_data, session_flag, rc):
        if rc == 0:
            self.__state = MqttConnection.State.CONNECTED
            with self.__connection_condition:
                self.__connection_condition.notify_all()
            MqttConnection.__logger.info('Client id: [{}] connect success, connect state: {}'
                                         .format(self.__profile.get_client_id(), self.__paho_client.is_connected()))
        else:
            MqttConnection.__logger.warning('bad connection, error code: {}'.format(str(rc)))
            return

        # auto login sub device when reconnected
        sub_devices = self.__logined_sub_device.copy()
        if sub_devices and self.__profile.get_auto_reconnect():
            self.get_processor().get_executor().submit(self.__auto_login_sub_device, sub_devices)

        # handle user callback
        if self.__on_connect is not None:
            self.__mqtt_processor.get_executor().submit(self.__on_connect)

    def __on_internal_disconnect(self, client, user_data, rc):
        if rc != 0:
            MqttConnection.__logger.warning('bad disconnection, error code: {}'.format(str(rc)))
            return
        MqttConnection.__logger.info('Client id: [{}] connection lost'.format(self.__profile.get_client_id()))
        # always clear the subscriptions
        self.__subscribed_topic_cache.clear()

        # disable reconnect of paho client
        if not self.__profile.get_auto_reconnect():
            self.__paho_client.loop_stop()

        # handle user callback
        if self.__on_disconnect is not None:
            self.__mqtt_processor.get_executor().submit(self.__on_disconnect)

    def __on_internal_message(self, client, user_data, message):
        self.__mqtt_processor.message_arrived(message)

    def __load_callbacks(self):
        self.__paho_client.on_connect = self.__on_internal_connect
        self.__paho_client.on_disconnect = self.__on_internal_disconnect
        self.__paho_client.on_message = self.__on_internal_message

    # handle activate response
    def __on_internal_device_dynamic_activate(self, arrived_message, arg_list):
        with self.__client_lock:
            device_credential = arrived_message.get_device_credential()
            device_secret = device_credential.get_device_secret()

            MqttConnection.__logger.info('device dynamic activate success, device key is : '
                                         .format(device_credential.get_device_key()))

            # handle user callback
            if self.__on_device_dynamic_active is not None:
                try:
                    self.__on_device_dynamic_active(device_secret)
                except Exception as e:
                    MqttConnection.__logger.error("on_device_dynamic_active process raise exception: %r" % e)

            # fast publish reply
            reply = DeviceActivateReply().builder() \
                .set_code(ResponseCode.SUCCESS) \
                .set_message('device activate success') \
                .set_product_key(device_credential.get_product_key()) \
                .set_device_key(device_credential.get_device_key()) \
                .build()
            reply.set_id(arrived_message.get_id())
            self.fast_publish(reply)

    def __auto_login_sub_device(self, sub_devices):
        for sub_device in sub_devices.keys():
            try:
                request = SubDeviceLoginRequest.builder().set_sub_device_credential(sub_devices[sub_device]).build()
                if request.get_secure_mode().get_mode_id() == VIA_DEVICE_SECRET:
                    response = self.publish(request)
                    if response.is_success():
                        MqttConnection.__logger.info('auto login sub-device {} successfully'.format(sub_device))
                    else:
                        MqttConnection.__logger.error('failed to auto login sub-device {} , response code {}'
                                                      .format(sub_device, response.get_code()))
                else:
                    MqttConnection.__logger.warning("don't support auto login sub-device using mode = {} for {}"
                                                    .format(request.get_secure_mode(), sub_device))
            except Exception as e:
                MqttConnection.__logger.error("failed to login sub-device: {}, err msg: {}".format(sub_device, str(e)))

    def get_logined_sub_device(self):
        return self.__logined_sub_device.copy()

    def get_processor(self):
        return self.__mqtt_processor

    @staticmethod
    def get_answer_topic(request):
        if request.get_id() is None:
            raise EnvisionException('request message id not set')
        return request.get_answer_topic() + '_' + request.get_id()

    @staticmethod
    def inc_and_get_message_id():
        with MqttConnection.__lock:
            MqttConnection.__request_id += 1
            if MqttConnection.__request_id == 65536:
                MqttConnection.__request_id = 1
            return MqttConnection.__request_id
