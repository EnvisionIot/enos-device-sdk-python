import json

from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.exception.EnvisionException import EnvisionException
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.core.util.StringUtil import StringUtil
from enos.message.upstream.integration.IntModelUpRawResponse import IntModelUpRawResponse


class IntModelUpRawRequest(BaseRequest):
    payload = list()

    def __init__(self):
        super(IntModelUpRawRequest, self).__init__()

    @classmethod
    def builder(cls):
        return Builder()

    def get_id(self):
        return "unknown"

    def set_id(self, message_id):
        raise EnvisionException('cannot set raw request message id')

    def encode(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload
        return self

    def get_answer_type(self):
        return IntModelUpRawResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.INTEGRATION_MODEL_UP_RAW

    def to_string(self):
        return "IntModelUpRawRequest{" + "payload=" + json.dumps(self.payload) + "} "


class Builder(BaseBuilder):
    payload = list()

    def __init__(self):
        super(Builder, self).__init__()

    def set_payload(self, payload):
        self.payload = payload
        return self

    def create_method(self):
        return MethodConstants.INTEGRATION_MODEL_UP_RAW

    def create_params(self):
        raise EnvisionException('unsupported operation')

    def create_request_instance(self):
        return IntModelUpRawRequest()

    def build(self):
        request = self.create_request_instance()
        if StringUtil.is_not_empty(self._product_key):
            request.set_product_key(self._product_key)

        if StringUtil.is_not_empty(self._device_key):
            request.set_device_key(self.set_device_key)

        request.set_method(self.create_method())
        request.set_payload(self.payload)
        return request
