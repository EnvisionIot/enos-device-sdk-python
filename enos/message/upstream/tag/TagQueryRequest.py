from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.tag.TagQueryResponse import TagQueryResponse


class TagQueryRequest(BaseRequest):
    @classmethod
    def builder(cls):
        return Builder()

    def get_answer_type(self):
        return TagQueryResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.TAG_QUERY


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__tag_keys = set()

    def add_key(self, key):
        self.__tag_keys.add(key)
        return self

    def add_keys(self, key):
        self.__tag_keys.update(key)
        return self

    def set_keys(self, keys):
        self.__tag_keys = set(keys)
        return self

    def query_all(self):
        self.__tag_keys = set()
        return self

    def create_method(self):
        return MethodConstants.TAG_QUERY

    def create_params(self):
        param_dict = dict()
        param_dict['tags'] = list(self.__tag_keys)
        return param_dict

    def create_request_instance(self):
        return TagQueryRequest()
