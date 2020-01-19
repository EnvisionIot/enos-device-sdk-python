from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.exception.EnvisionException import EnvisionException
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.core.util.StringUtil import StringUtil
from enos.message.upstream.tsl.ModelUpRawResponse import ModelUpRawResponse


class ModelUpRawRequest(BaseRequest):

    def __init__(self):
        super(ModelUpRawRequest, self).__init__()
        self.__payload = bytes()

    @classmethod
    def builder(cls):
        return Builder()

    def get_id(self):
        return "unknown"

    def set_id(self, id):
        raise EnvisionException('cannot set raw request message id')

    def encode(self):
        return self.__payload

    def set_payload(self, payload):
        self.__payload = payload
        return self

    def get_answer_type(self):
        return ModelUpRawResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.MODEL_UP_RAW


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__payload = bytes()

    def set_payload(self, payload):
        self.__payload = payload
        return self

    def create_method(self):
        return MethodConstants.THING_MODEL_UP_RAW

    def create_params(self):
        raise EnvisionException('exception is null')

    def create_request_instance(self):
        return ModelUpRawRequest()

    def build(self):
        request = self.create_request_instance()
        if StringUtil.is_not_empty(self._product_key):
            request.set_product_key(self._product_key)

        if StringUtil.is_not_empty(self._device_key):
            request.set_device_key(self._device_key)

        request.set_method(self.create_method())
        request.set_payload(self.__payload)
        return request
