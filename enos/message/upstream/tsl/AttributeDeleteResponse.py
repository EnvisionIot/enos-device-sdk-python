import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse


class AttributeDeleteResponse(BaseResponse):

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.ATTRIBUTE_DELETE_REPLY)

    def decode_to_object(self, msg):
        base = AttributeDeleteResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__
