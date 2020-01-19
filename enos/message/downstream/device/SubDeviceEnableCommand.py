import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseCommand import BaseCommand
from enos.message.downstream.device.SubDeviceEnableReply import SubDeviceEnableReply


class SubDeviceEnableCommand(BaseCommand):

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.SUB_DEVICE_ENABLE_COMMAND)

    def decode_to_object(self, msg):
        base = SubDeviceEnableCommand()
        base.__dict__ = msg
        return base

    def get_answer_type(self):
        return SubDeviceEnableReply()

    @classmethod
    def get_class(cls):
        return cls.__name__

