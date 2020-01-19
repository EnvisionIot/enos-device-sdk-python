from abc import ABCMeta, abstractmethod

from enos.core.message.IArrivedMessage import IArrivedMessage
from enos.core.message.body.AnswerableMessageBody import AnswerableMessageBody


class BaseCommand(AnswerableMessageBody, IArrivedMessage):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(BaseCommand, self).__init__()
        self.__product_key = ''
        self.__device_key = ''
        self.__message_topic = ''

    @abstractmethod
    def get_answer_type(self):
        pass

    def get_product_key(self):
        return self.__product_key

    def set_product_key(self, product_key):
        self.__product_key = product_key

    def get_device_key(self):
        return self.__device_key

    def set_device_key(self, device_key):
        self.__device_key = device_key

    def get_message_topic(self):
        return self.__message_topic

    def set_message_topic(self, topic):
        self.__message_topic = topic

    def decode_to_object(self, msg):
        base = BaseCommand()
        base.__dict__ = msg
        return base


