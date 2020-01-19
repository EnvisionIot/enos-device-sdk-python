from abc import abstractmethod, ABCMeta

from enos.core.exception.EnvisionException import EnvisionException
from enos.core.message.body.AckMessageBody import AckMessageBody
from enos.core.util.CheckUtil import CheckUtil
from enos.core.util.StringUtil import StringUtil


class BaseReply(AckMessageBody):

    def __init__(self):
        super(BaseReply, self).__init__()
        self.__qos = 1
        self.__product_key = ''
        self.__device_key = ''
        self.__message_topic = ''

    @abstractmethod
    def get_format_topic(self):
        pass

    def check(self):
        CheckUtil.check_not_empty(self.get_product_key(), 'productKey')
        CheckUtil.check_not_empty(self.get_device_key(), 'deviceKey')

    def set_topic_args(self, args):
        self.set_product_key(args[0])
        self.set_device_key(args[1])

    def reply_with_payload(self, code, message, data):
        self.set_code(code)
        self.set_message(message)
        self.set_data(data)

    def get_qos(self):
        return self.__qos

    def get_product_key(self):
        return self.__product_key

    def set_product_key(self, product_key):
        self.__product_key = product_key

    def get_device_key(self):
        return self.__device_key

    def set_device_key(self, device_key):
        self.__device_key = device_key

    def get_message_topic(self):
        return self.get_format_topic().format(self.get_product_key(), self.get_device_key())

    def set_message_topic(self, topic):
        raise EnvisionException("reply message type can't set topic")


class BaseBuilder(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__qos = 1
        self.__code = 0
        self.__message = ''
        self.__product_key = ''
        self.__device_key = ''

    @abstractmethod
    def create_data(self):
        pass

    @abstractmethod
    def create_reply_instance(self):
        pass

    def set_qos(self, qos):
        self.__qos = qos
        return self

    def set_code(self, code):
        self.__code = code
        return self

    def set_message(self, message):
        self.__message = message
        return self

    def set_product_key(self, product_key):
        self.__product_key = product_key
        return self

    def set_device_key(self, device_key):
        self.__device_key = device_key
        return self

    def build(self):
        reply = self.create_reply_instance()
        if self.__code is not None:
            reply.set_code(self.__code)
        else:
            reply.set_code(200)

        if StringUtil.is_not_empty(self.__message):
            reply.set_message(self.__message)

        if StringUtil.is_not_empty(self.__product_key):
            reply.set_product_key(self.__product_key.strip())

        if StringUtil.is_not_empty(self.__device_key):
            reply.set_device_key(self.__device_key.strip())

        reply.set_data(self.create_data())
        reply.set_qos(self.__qos)

        return reply





