from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.tsl.AttributeQueryResponse import AttributeQueryResponse


class AttributeQueryRequest(BaseRequest):
    def __init__(self):
        super(AttributeQueryRequest, self).__init__()

    def get_answer_type(self):
        return AttributeQueryResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.ATTRIBUTE_QUERY

    @classmethod
    def builder(cls):
        return Builder()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__attributes = set()

    def add_attribute(self, key):
        self.__attributes.add(key)
        return self

    def add_attributes(self, key):
        for param in key:
            self.__attributes.add(param)
        return self

    def set_attributes(self, key):
        self.__attributes = set(key)
        return self

    def query_all(self):
        self.__attributes.clear()
        return self

    def create_method(self):
        return MethodConstants.ATTRIBUTE_QUERY

    def create_params(self):
        params = dict()
        params['attributes'] = list(self.__attributes)
        return params

    def create_request_instance(self):
        return AttributeQueryRequest()
