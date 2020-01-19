from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.tag.TagDeleteResponse import TagDeleteResponse


class TagDeleteRequest(BaseRequest):
    @classmethod
    def builder(cls):
        return Builder()

    def __init__(self):
        super(TagDeleteRequest, self).__init__()

    def get_answer_type(self):
        return TagDeleteResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.TAG_DELETE_TOPIC_FMT


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder,self).__init__()
        self.__tags = set()

    def create_method(self):
        return MethodConstants.TAG_DELETE

    def create_params(self):
        param_dict = dict()
        param_dict['tags'] = list(self.__tags)
        return param_dict

    def delete_tag_key(self, tag_key):
        self.__tags.add(tag_key)
        return self

    def delete_tag_keys(self, tag_keys):
        self.__tags.update(tag_keys)
        return self

    def set_tags(self, tags):
        self.__tags = set(tags)
        return self

    def create_request_instance(self):
        return TagDeleteRequest()
