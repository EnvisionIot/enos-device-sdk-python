from abc import ABCMeta, abstractmethod

from enos.core.exception.EnvisionException import EnvisionException
from enos.core.message.body.AnswerableMessageBody import AnswerableMessageBody
from enos.core.util.Deprecation import deprecated
from enos.core.util.CheckUtil import CheckUtil
from enos.core.util.StringUtil import StringUtil

MAX_MESSAGE_SIZE = 512 * 1024


class BaseRequest(AnswerableMessageBody):
    __metaclass__ = ABCMeta

    def __init__(self):
        super(BaseRequest, self).__init__()
        self.__qos = 1
        self.__product_key = ''
        self.__device_key = ''

    @abstractmethod
    def get_format_topic(self):
        pass

    @abstractmethod
    def get_answer_type(self):
        pass

    def get_message_topic(self):
        return self.get_format_topic().format(self.get_product_key(), self.get_device_key())

    def get_answer_topic(self):
        return self.get_message_topic() + '_reply'

    def set_topic_args(self):
        pass

    def check(self):
        if self.get_message_size() > MAX_MESSAGE_SIZE:
            raise EnvisionException('message too large, max length is: %s' % MAX_MESSAGE_SIZE)
        CheckUtil.check_not_empty(self.get_product_key(), 'product key')
        CheckUtil.check_not_empty(self.get_device_key(), 'device key')

    def get_product_key(self):
        return self.__product_key

    def set_product_key(self, product_key):
        self.__product_key = product_key

    def get_device_key(self):
        return self.__device_key

    def set_device_key(self, device_key):
        self.__device_key = device_key

    def get_qos(self):
        return self.__qos

    def set_qos(self, qos):
        if qos < 0 or qos >= 2:
            raise EnvisionException('qos only support 0,1 in current version')
        self.__qos = qos

    @deprecated
    def getMessageTopic(self):
        return self.get_message_topic()

    @deprecated
    def getAnswerTopic(self):
        return self.get_answer_type()

    @deprecated
    def setTopicArgs(self):
        return self.set_topic_args()

    @deprecated
    def getProductKey(self):
        return self.get_product_key()

    @deprecated
    def setProductKey(self, product_key):
        self.set_product_key(product_key)

    @deprecated
    def getDeviceKey(self):
        return self.get_device_key()

    @deprecated
    def setDeviceKey(self, device_key):
        return self.set_device_key(device_key)

    @deprecated
    def getQos(self):
        return self.get_qos()

    @deprecated
    def setQos(self, qos):
        return self.set_qos(qos)


class BaseBuilder(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self._product_key = ''
        self._device_key = ''

    @abstractmethod
    def create_method(self):
        return ''

    @abstractmethod
    def create_params(self):
        return ''

    @abstractmethod
    def create_request_instance(self):
        pass

    def set_product_key(self, product_key):
        self._product_key = product_key
        return self

    def set_device_key(self, device_key):
        self._device_key = device_key
        return self

    def build(self):
        request = self.create_request_instance()
        if StringUtil.is_not_empty(self._product_key):
            request.set_product_key(self._product_key)

        if StringUtil.is_not_empty(self._device_key):
            request.set_device_key(self._device_key)

        request.set_method(self.create_method())
        request.set_params(self.create_params())
        return request

    @deprecated
    def createMethod(self):
        return self.create_method()

    @deprecated
    def createParams(self):
        return self.create_params()

    @deprecated
    def createRequestInstance(self):
        return self.create_request_instance()

    @deprecated
    def setProductKey(self, product_key):
        return self.set_product_key(product_key)

    @deprecated
    def setDeviceKey(self, device_key):
        return self.set_device_key(device_key)
