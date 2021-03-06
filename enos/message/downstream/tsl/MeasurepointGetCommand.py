import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseCommand import BaseCommand
from enos.core.util.Deprecation import deprecated
from enos.message.downstream.tsl.MeasurepointGetReply import MeasurepointGetReply


class MeasurepointGetCommand(BaseCommand):

    def get_answer_type(self):
        return MeasurepointGetReply()

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.MEASUREPOINT_GET_COMMAND)

    def decode_to_object(self, msg):
        base = MeasurepointGetCommand()
        base.__dict__ = msg
        return base

    @deprecated
    def getMatchTopicPattern(self):
        return self.get_match_topic_pattern()

    @deprecated
    def decodeToObject(self, msg):
        return self.decode_to_object(msg)

    @classmethod
    def get_class(cls):
        return cls.__name__

    @deprecated
    def getClass(self):
        return self.get_class()
