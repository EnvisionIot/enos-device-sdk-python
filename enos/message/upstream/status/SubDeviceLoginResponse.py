from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse
from enos.core.util.Deprecation import deprecated
import re


class SubDeviceLoginResponse(BaseResponse):

    def get_sub_product_key(self):
        data = self.get_data()
        return data['productKey']

    def get_sub_device_key(self):
        data = self.get_data()
        return data['deviceKey']

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.SUB_DEVICE_LOGIN_REPLY)

    def decode_to_object(self, msg):
        base = SubDeviceLoginResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__

    @deprecated
    def getSubProductKey(self):
        return self.get_sub_product_key()

    @deprecated
    def getSubDeviceKey(self):
        return self.get_sub_device_key()

    @deprecated
    def getMatchTopicPattern(self):
        return self.get_match_topic_pattern()

    @deprecated
    def decodeToObject(self, msg):
        return self.decode_to_object(msg)

    @deprecated
    def getClass(self):
        return self.get_class()
