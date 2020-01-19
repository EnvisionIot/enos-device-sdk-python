
import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse


class MeasurepointPostBatchResponse(BaseResponse):
    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.MEASUREPOINT_POST_BATCH_REPLY)

    def decode_to_object(self, msg):
        base = MeasurepointPostBatchResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__
