from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.tsl.AttributeDeleteResponse import AttributeDeleteResponse


class AttributeDeleteRequest(BaseRequest):
    def __init__(self):
        super(AttributeDeleteRequest, self).__init__()

    def get_answer_type(self):
        return AttributeDeleteResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.ATTRIBUTE_DELETE

    @classmethod
    def builder(cls):
        return Builder()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__attributes = set()

    def delete_attribute(self, key):
        self.__attributes.add(key)
        return self

    def delete_attributes(self, key):
        for param in key:
            self.__attributes.add(param)
        return self

    def create_method(self):
        return MethodConstants.ATTRIBUTE_DELETE

    def create_params(self):
        params = dict()
        params['attributes'] = list(self.__attributes)
        return params

    def create_request_instance(self):
        return AttributeDeleteRequest()
