import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse


class IntAttributePostResponse(BaseResponse):
    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.INTEGRATION_ATTRIBUTE_POST_REPLYLY)

    def decode_to_object(self, msg):
        base = IntAttributePostResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__
