from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.tsl.AttributeUpdateResponse import AttributeUpdateResponse


class AttributeUpdateRequest(BaseRequest):
    def __init__(self):
        super(AttributeUpdateRequest, self).__init__()

    def get_answer_type(self):
        return AttributeUpdateResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.ATTRIBUTE_UPDATE

    @classmethod
    def builder(cls):
        return Builder()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder,self).__init__()
        self.__attributes = dict()

    def add_attribute(self, key, value):
        self.__attributes[key] = value
        return self

    def add_attributes(self, values):
        self.__attributes.update(values)
        return self

    def set_attributes(self, values):
        self.__attributes = values
        return self

    def create_method(self):
        return MethodConstants.ATTRIBUTE_UPDATE

    def create_params(self):
        params = dict()
        params['attributes'] = self.__attributes
        return params

    def create_request_instance(self):
        return AttributeUpdateRequest()
