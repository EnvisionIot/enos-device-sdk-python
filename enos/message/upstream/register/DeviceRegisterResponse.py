import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.constant.FieldConstants import FieldConstants
from enos.core.message.BaseResponse import BaseResponse
from enos.message.upstream.register.DeviceBasicInfo import DeviceBasicInfo


class DeviceRegisterResponse(BaseResponse):
    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.DEVICE_REGISTER_REPLY)

    def get_device_basic_info_list(self):
        data_list = self.get_data()
        results = list()
        for data in data_list:
            device_basic_info = DeviceBasicInfo()
            device_basic_info.productKey = data.get(FieldConstants.PRODUCT_KEY)
            device_basic_info.deviceKey = data.get(FieldConstants.DEVICE_KEY)
            device_basic_info.deviceSecret = data.get(FieldConstants.ASSET_ID)
            device_basic_info.deviceSecret = data.get(FieldConstants.DEVICE_SECRET)
            results.append(device_basic_info)
            return results

    def decode_to_object(self, msg):
        base = DeviceRegisterResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__
