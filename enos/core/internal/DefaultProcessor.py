import logging
import traceback
from concurrent.futures.thread import ThreadPoolExecutor

from enos.core.constant.ResponseCode import ResponseCode
from enos.core.internal.DecoderRegistry import DecoderRegistry
from enos.core.message.BaseCommand import BaseCommand
from enos.core.message.BaseReply import BaseReply
from enos.core.message.BaseResponse import BaseResponse
from enos.core.util.ConcurrentDict import ConcurrentDict


class DefaultProcessor(object):
    __logger = logging.getLogger(__name__)

    def __init__(self, mqtt_connection, profile):
        self.__mqtt_connection = mqtt_connection
        self.__profile = profile
        self.__rsp_token_dict = ConcurrentDict()
        self.__arrived_msg_handler_dict = ConcurrentDict()
        self.__executor = ThreadPoolExecutor(20, 'default executor')

    def get_executor(self):
        return self.__executor

    def register_response_token(self, key, token):
        self.__rsp_token_dict.add(key, token)

    def deregister_response_token(self, key):
        return self.__rsp_token_dict.pop(key)

    def set_arrived_msg_handler(self, arrived_msg_cls, handler):
        self.__arrived_msg_handler_dict.add(arrived_msg_cls, handler)

    def message_arrived(self, message):
        """ handler arrived response or command """
        try:
            decoder_list = DecoderRegistry.get_decoder_list()
            decode_result = None
            for decoder in decoder_list:
                result = decoder(message.topic, message.payload)
                if result is not None:
                    decode_result = result
                    break

            if not decode_result:
                DefaultProcessor.__logger.error('decode received message failed, from topic {}'.format(message.topic))

            path_list = decode_result.get_path_list()
            arrived_message = decode_result.get_arrived_msg()
            if not arrived_message:
                DefaultProcessor.__logger.error('decode message failed, from topic {}'.format(message.topic))

            # handle arrived response
            if isinstance(arrived_message, BaseResponse):
                key = message.topic + '_' + arrived_message.get_id()
                token = self.deregister_response_token(key)
                if token is None:
                    DefaultProcessor.__logger.error('no request answer the response, topic {}, message id: {}'.
                                                    format(message.topic, arrived_message.get_id()))
                    return
                # notify wait for response in publish
                token.mark_success(arrived_message)
            else:
                handler = self.__arrived_msg_handler_dict.get(arrived_message.get_class())
                if handler:
                    self.__executor.submit(self.message_handler, handler, arrived_message, path_list)
                elif isinstance(arrived_message, BaseCommand):
                    self.__executor.submit(self.handle_command_without_handler, arrived_message, path_list)

        except Exception as e:
            DefaultProcessor.__logger.error('message decode failed: ' + str(e))

    def message_handler(self, handler, msg, path_list):
        try:
            delivery_msg = handler.on_message(msg, path_list)
            # reply if needed
            if delivery_msg is not None:
                delivery_msg.set_id(msg.get_id())
                delivery_msg.set_product_key(msg.get_product_key())
                delivery_msg.set_device_key(msg.get_device_key())

                if isinstance(delivery_msg, BaseReply):
                    delivery_msg.set_topic_args(path_list)
                    if delivery_msg.get_code() < ResponseCode.USER_DEFINED_ERR_CODE and \
                            delivery_msg.get_code() != ResponseCode.SUCCESS:
                        DefaultProcessor.__logger.warning('error code of reply is not allowed')

                    self.__mqtt_connection.fast_publish(delivery_msg)
        except Exception as e:
            DefaultProcessor.__logger.error('handle the arrived message error, '
                                            'may because of registered arrived message callback' + traceback.format_exc())
            reply = self.build_reply(msg, path_list, ResponseCode.COMMAND_HANDLER_EXECUTION_FAILED,
                                     'command handler execution failed' + str(e))
            self.__logger.error(traceback.format_exc())
            self.__mqtt_connection.fast_publish(reply)

    def handle_command_without_handler(self, msg, path_list):
        reply = self.build_reply(msg, path_list, ResponseCode.COMMAND_HANDLER_NOT_REGISTERED,
                                 'downstream command handler not registered')
        self.__mqtt_connection.fast_publish(reply)

    @staticmethod
    def build_reply(msg, path_list, code, message):
        reply = msg.get_answer_type()
        reply.set_id(msg.get_id())
        reply.set_product_key(msg.get_product_key())
        reply.set_device_key(msg.get_device_key())
        reply.set_code(str(code))
        reply.set_message(message)
        reply.set_topic_args(path_list)
        return reply
