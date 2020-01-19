from abc import ABCMeta

from enos.core.message.IArrivedMessage import IArrivedMessage
from enos.core.message.body.AckMessageBody import AckMessageBody


class BaseResponse(AckMessageBody, IArrivedMessage):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(BaseResponse, self).__init__()
        self.__product_key = ''
        self.__device_key = ''
        self.__message_topic = ''

    def get_message_topic(self):
        if hasattr(self, 'messageTopic'):
            return self.__message_topic

    def set_message_topic(self, topic):
        self.__message_topic = topic

    def get_product_key(self):
        return self.__product_key

    def set_product_key(self, product_key):
        self.__product_key = product_key

    def get_device_key(self):
        return self.__device_key

    def set_device_key(self, device_key):
        self.__device_key = device_key

    def decode_to_object(self, msg):
        base = BaseResponse()
        base.__dict__ = msg
        return base

    def set_topic_args(self):
        pass

    def is_success(self):
        return self.get_code() == 200

