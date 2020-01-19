import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse


class IntMeaturepointPostResponse(BaseResponse):

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.INTEGRATION_MEASUREPOINT_POST_REPLY)

    def decode_to_object(self, msg):
        base = IntMeaturepointPostResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__
