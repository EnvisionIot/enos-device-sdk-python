import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseCommand import BaseCommand
from enos.message.downstream.device.SubDeviceDisableReply import SubDeviceDisableReply


class SubDeviceDisableCommand(BaseCommand):

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.SUB_DEVICE_DISABLE_COMMAND)

    def decode_to_object(self, msg):
        base = SubDeviceDisableCommand()
        base.__dict__ = msg
        return base

    def get_answer_type(self):
        return SubDeviceDisableReply()

    @classmethod
    def get_class(cls):
        return cls.__name__

