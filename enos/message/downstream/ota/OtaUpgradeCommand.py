import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseCommand import BaseCommand
from enos.core.util.Deprecation import deprecated
from enos.message.downstream.ota.OtaUpgradeReply import OtaUpgradeReply
from enos.message.upstream.ota.Firmware import Firmware


class OtaUpgradeCommand(BaseCommand):

    def get_answer_type(self):
        return OtaUpgradeReply()

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.DEVICE_OTA_COMMAND)

    def decode_to_object(self, msg):
        base = OtaUpgradeCommand()
        base.__dict__ = msg
        return base

    @deprecated
    def getMatchTopicPattern(self):
        return self.get_match_topic_pattern()

    @deprecated
    def decodeToObject(self, msg):
        return self.decode_to_object(msg)

    def get_firmware_info(self):
        firmware = Firmware()
        params = self.get_params()
        firmware.version = params.get('version')
        firmware.sign_method = params.get('signMethod')
        firmware.sign = params.get('sign')
        firmware.file_url = params.get('fileUrl')
        firmware.file_size = params.get('fileSize')
        return firmware

    @classmethod
    def get_class(cls):
        return cls.__name__

    @deprecated
    def getFirmwareInfo(self):
        return self.get_firmware_info()

    @deprecated
    def getClass(self):
        return self.get_class()
