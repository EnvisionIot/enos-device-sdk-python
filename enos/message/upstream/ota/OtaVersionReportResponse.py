from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse
from enos.core.util.Deprecation import deprecated
import re


class OtaVersionReportResponse(BaseResponse):

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.VERSION_REPORT_TOPIC_REPLY)

    def decode_to_object(self, msg):
        base = OtaVersionReportResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__

    @deprecated
    def getMatchTopicPattern(self):
        return self.get_match_topic_pattern()

    @deprecated
    def decodeToObject(self, msg):
        return self.decode_to_object(msg)

    @deprecated
    def getClass(self):
        return self.get_class()