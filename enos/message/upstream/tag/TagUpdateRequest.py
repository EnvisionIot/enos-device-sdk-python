from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.core.util.CheckUtil import CheckUtil
from enos.message.upstream.tag.TagUpdateResponse import TagUpdateResponse


class TagUpdateRequest(BaseRequest):

    def __init__(self):
        super(TagUpdateRequest, self).__init__()

    def get_answer_type(self):
        return TagUpdateResponse()

    def check(self):
        super(TagUpdateRequest,self).check()
        params = super(TagUpdateRequest,self).get_params()
        for param in params:
            CheckUtil.check_not_empty(param.get('tagKey'), 'tagKey')
            CheckUtil.check_not_empty(param.get('tagValue'), 'tagValue')

    def get_format_topic(self):
        return DeliveryTopicFormat.TAG_UPDATE_TOPIC_FMT

    @classmethod
    def builder(cls):
        return Builder()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder,self).__init__()
        self.__tags = dict()

    def add_tag(self, tag_key, tag_value):
        self.__tags[tag_key] = tag_value
        return self

    def add_tags(self, tags):
        self.__tags.update(tags)
        return self

    def create_method(self):
        return MethodConstants.TAG_UPDATE

    def create_params(self):
        params = list()
        for key, value in self.__tags.items():
            param_dict = dict()
            param_dict['tagKey'] = key
            param_dict['tagValue'] = value
            params.append(param_dict)
        return params

    def create_request_instance(self):
        return TagUpdateRequest()
