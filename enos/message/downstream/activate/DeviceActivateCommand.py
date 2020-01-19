import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.constant.DeviceCredential import DeviceCredential
from enos.core.constant.FieldConstants import FieldConstants
from enos.core.message.BaseCommand import BaseCommand
from enos.message.downstream.activate.DeviceActivateReply import DeviceActivateReply


class DeviceActivateCommand(BaseCommand):
    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.ACTIVATE_INFO)

    def decode_to_object(self, msg):
        base = DeviceActivateCommand()
        base.__dict__ = msg
        return base

    def get_device_credential(self):
        params = self.get_params()
        device_credential = DeviceCredential(params[FieldConstants.PRODUCT_KEY],
                                             None,
                                             params[FieldConstants.DEVICE_KEY],
                                             params[FieldConstants.DEVICE_SECRET])
        return device_credential

    def get_answer_type(self):
        return DeviceActivateReply()

    @classmethod
    def get_class(cls):
        return cls.__name__
