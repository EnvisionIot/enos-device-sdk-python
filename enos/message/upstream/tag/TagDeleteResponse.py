import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse


class TagDeleteResponse(BaseResponse):
    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.TAG_DELETE_REPLY)

    def decode_to_object(self, msg):
        base = TagDeleteResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__