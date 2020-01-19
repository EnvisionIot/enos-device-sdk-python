import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse


class SubDeviceLogoutResponse(BaseResponse):

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.SUB_DEVICE_LOGOUT_REPLY)

    def decode_to_object(self, msg):
        base = SubDeviceLogoutResponse()
        base.__dict__ = msg
        return base

    def get_sub_product_key(self):
        data = self.get_data()
        return data['productKey']

    def get_sub_device_key(self):
        data = self.get_data()
        return data['deviceKey']

    @classmethod
    def get_class(cls):
        return cls.__name__
