from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.status.SubDeviceLogoutResponse import SubDeviceLogoutResponse


class SubDeviceLogoutRequest(BaseRequest):

    def __init__(self, sub_product_key, sub_device_key):
        super(SubDeviceLogoutRequest, self).__init__()
        self.__sub_product_key = sub_product_key
        self.__sub_device_key = sub_device_key

    @classmethod
    def builder(cls):
        return Builder()

    def get_answer_type(self):
        return SubDeviceLogoutResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.SUB_DEVICE_LOGOUT

    def get_sub_product_key(self):
        return self.__sub_product_key

    def get_sub_device_key(self):
        return self.__sub_device_key


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder,self).__init__()
        self.__sub_product_key = ''
        self.__sub_device_key = ''

    def set_sub_product_key(self, sub_product_key):
        self.__sub_product_key = sub_product_key
        return self

    def set_sub_device_key(self, sub_device_key):
        self.__sub_device_key = sub_device_key
        return self

    def create_method(self):
        return MethodConstants.SUB_DEVICE_LOGOUT

    def create_params(self):
        params = dict()
        params["productKey"] = self.__sub_product_key
        params["deviceKey"] = self.__sub_device_key
        return params

    def create_request_instance(self):
        return SubDeviceLogoutRequest(self.__sub_product_key, self.__sub_device_key)
