from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.integration.IntAttributePostResponse import IntAttributePostResponse


class IntAttributePostRequest(BaseRequest):

    @classmethod
    def builder(cls):
        return Builder()

    def get_format_topic(self):
        return DeliveryTopicFormat.INTEGRATION_ATTRIBUTE_POST

    def get_answer_type(self):
        return IntAttributePostResponse()

    def get_message_topic(self):
        return self.get_format_topic().format(self.get_product_key())


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        # {device_key: {key: value}}
        self.__attributes = dict()

    def add_attribute(self, device_key, key, value):
        attr = dict()
        if device_key not in self.__attributes:
            self.__attributes[device_key] = attr
        attr[key] = value
        return self

    def add_attributes(self, device_key, attrs):
        for attr in self.__attributes.get(device_key):
            if attr is None:
                attr = dict()
                self.__attributes[device_key] = attr
            attr[device_key] = attrs
        return self

    def set_attribute(self, attributes):
        self.__attributes = attributes
        return self

    def create_method(self):
        return MethodConstants.INTEGRATION_ATTRIBUTE_POST

    def create_params(self):
        params = list()
        if not self.__attributes:
            for key, value in self.__attributes.items():
                param = dict()
                param['deviceKey'] = key
                param['attributes'] = value
                params.append(param)
        return params

    def create_request_instance(self):
        return IntAttributePostRequest()
