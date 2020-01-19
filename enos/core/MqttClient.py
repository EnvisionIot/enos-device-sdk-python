import json
import logging
import logging.config
import os

from enos.core.internal.MqttConnection import MqttConnection
from enos.core.internal.Profile import Profile
from enos.core.message.IMessageHandler import IMessageHandler
from enos.core.util.Deprecation import deprecated


class MqttClient(object):
    __logger = logging.getLogger(__name__)

    def __init__(self, uri=None, product_key=None, device_key=None, device_secret=None, profile=None):
        if profile is not None:
            self.__profile = profile
        else:
            # normal device triplet
            self.__profile = Profile(uri, product_key, device_key, device_secret)
        self.__connection = MqttConnection(self.__profile)

        # user defined callbacks
        self.__on_device_dynamic_activate = None
        self.__on_connect = None
        self.__on_disconnect = None
        self.__on_connect_failed = None

    @property
    def on_device_dynamic_active(self):
        return self.__on_device_dynamic_activate

    @on_device_dynamic_active.setter
    def on_device_dynamic_active(self, value):
        self.__on_device_dynamic_activate = value

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
    def on_connected_failed(self):
        return self.__on_connect_failed

    @on_connected_failed.setter
    def on_connected_failed(self, value):
        self.__on_connect_failed = value

    def connect(self, callback=None):
        """ Connect to broker and wait for the connection is established if callback is NOT provided.
            Connect to broker in async way when callback is provided.
            In async way, user have to check whether the connection is connected before publish and so on.

        :param callback: the instance of or implements <IConnectCallback>
        """
        self.__load_callback(callback)
        if callback is not None:
            self.__connection.connect_async()
        else:
            self.__connection.connect()

    def fast_publish(self, request):
        """ Publish the request and NOT care about the response.
        :param request: request to broker
        """
        self.__connection.fast_publish(request)

    def publish(self, request, callback=None):
        """ Publish the request and wait for the response if callback is NOT provided.
            Publish the request in async way, the callback would be invoked when response is ready or error happens.
        :param request: request to broker
        :param callback: the instance of or implements <IResponseCallback>
        :return: response in sync way or None in async way
        """
        if callback is None:
            return self.__connection.publish(request)
        else:
            return self.__connection.async_publish(request, callback)

    def register_arrived_message_handler(self, arrived_message_class, handler):
        """ Register message handler for specific arrived message.
        :param arrived_message_class: the arrived message class
        :param handler: message callback, handle the received downstream message and implement your logic
        """
        message_handler = IMessageHandler()
        message_handler.on_message = handler
        self.__connection.get_processor().set_arrived_msg_handler(arrived_message_class, message_handler)

    def reconnect(self):
        """ Reconnect client to broker"""
        self.__connection.reconnect()

    def disconnect(self):
        """ Disconnect client from broker. """
        self.__connection.disconnect()

    def close(self):
        """ Close client and release related resources. """
        self.__connection.close()

    def is_connected(self):
        return self.__connection.is_connected()

    def get_profile(self):
        return self.__profile

    def get_logined_sub_device(self):
        return self.__connection.get_logined_sub_device()

    def __load_callback(self, callback):
        self.__connection.on_device_dynamic_active = self.__on_device_dynamic_activate
        self.__connection.on_connect = self.__on_connect if not callback else callback.on_connect
        self.__connection.on_disconnect = self.__on_disconnect if not callback else callback.on_disconnect
        self.__connection.on_connect_failed = self.__on_connect_failed if not callback else callback.on_connect_failed

    @staticmethod
    def setup_basic_logger(level='INFO', file_path=None,
                           log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        if file_path is not None:
            logging.basicConfig(level=level, filename=file_path, format=log_format)
        else:
            logging.basicConfig(level=level, format=log_format)

    @staticmethod
    def setup_file_logger(file_path):
        path = file_path
        if os.path.exists(path):
            with open(path, "r") as f:
                config = json.load(f)
                logging.config.dictConfig(config)

    # deprecated
    @property
    def onOnline(self):
        return self.__on_connect

    @onOnline.setter
    def onOnline(self, value):
        self.__on_connect = value

    @property
    def onOffline(self):
        return self.__on_disconnect

    @onOffline.setter
    def onOffline(self, value):
        self.__on_disconnect = value

    @property
    def onConnectFailed(self):
        return self.__on_connect_failed

    @onConnectFailed.setter
    def onConnectFailed(self, value):
        self.__on_connect_failed = value

    @deprecated
    def fastPublish(self, request):
        self.fast_publish(request)

    @deprecated
    def isConnected(self):
        return self.is_connected()

    @deprecated
    def getProfile(self):
        return self.get_profile()

    @deprecated
    def onMessage(self, arrived_message_class, handler):
        self.register_arrived_message_handler(arrived_message_class, handler)

    @staticmethod
    @deprecated
    def setupBasicLogger(level='INFO', file_path=None,
                         log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        MqttClient.setup_basic_logger(level, file_path, log_format)

    @staticmethod
    @deprecated
    def setupFileLogger(file_path):
        MqttClient.setup_file_logger(file_path)
