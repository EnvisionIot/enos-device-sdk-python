import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse
from enos.message.upstream.ota.Firmware import Firmware


class OtaGetVersionResponse(BaseResponse):

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.GET_VERSION_TOPIC_REPLY)

    def get_firmware_info(self):
        data_list = self.get_data()
        results = list()
        if data_list is not None:
            for data in data_list:
                firmware = Firmware()
                firmware.version = data.get('version')
                firmware.sign_method = data.get('signMethod')
                firmware.sign = data.get('sign')
                firmware.file_url = data.get('fileUrl')
                firmware.file_size = data.get('fileSize')
                results.append(firmware)
            return results

    @classmethod
    def get_class(cls):
        return cls.__name__
