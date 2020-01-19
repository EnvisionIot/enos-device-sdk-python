from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.core.util.CheckUtil import CheckUtil
from enos.core.util.StringUtil import StringUtil
from enos.message.upstream.register.DeviceRegOption import DeviceRegOption
from enos.message.upstream.register.DeviceRegisterResponse import DeviceRegisterResponse


class DeviceRegisterRequest(BaseRequest):
    __MAX_DEVICE_SIZE = 1000

    def __init__(self):
        super(DeviceRegisterRequest, self).__init__()

    @classmethod
    def builder(cls):
        return Builder()

    def get_answer_type(self):
        return DeviceRegisterResponse()

    def check(self):
        params = self.get_params()
        CheckUtil().check_max_size(params, self.__MAX_DEVICE_SIZE, 'regOptionList')

    def get_format_topic(self):
        return DeliveryTopicFormat.DEVICE_REGISTER_TOPIC_FMT

    @classmethod
    def create_batch_reg_info_dict(cls, product_key, reg_options):
        params = list()
        for reg_option in reg_options:
            params.append(cls.create_reg_info_dict(product_key, reg_option))
        return params

    @staticmethod
    def create_reg_info_dict(product_key, reg_option):
        param = dict()
        param['productKey'] = product_key
        if reg_option.device_attributes:
            param['deviceAttributes'] = reg_option.device_attributes
        if StringUtil.is_not_empty(reg_option.device_key):
            param['deviceKey'] = reg_option.device_key
        if reg_option.device_name is not None:
            param['deviceName'] = reg_option.device_name.encode()
        if StringUtil.is_not_empty(reg_option.device_desc):
            param['deviceDesc'] = reg_option.device_desc
        if StringUtil.is_not_empty(reg_option.timezone):
            param['timezone'] = reg_option.timezone
        return param


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.params = list()

    def create_method(self):
        return MethodConstants.DEVICE_REGISTER

    def create_params(self):
        return self.params

    def create_request_instance(self):
        return DeviceRegisterRequest()

    def add_batch_register_info(self, product_key, reg_options):
        self.params.extend(DeviceRegisterRequest.create_batch_reg_info_dict(product_key, reg_options))
        return self

    def set_batch_register_info(self, product_key, reg_options):
        self.params = DeviceRegisterRequest.create_batch_reg_info_dict(product_key, reg_options)
        return self

    def add_register_reg_option(self, product_key, reg_option):
        self.params.append(DeviceRegisterRequest.create_reg_info_dict(product_key, reg_option))
        return self

    def add_register_information(self, product_key, device_key, device_name, device_desc, timezone,
                                 device_attributes=None):
        device_reg_option = DeviceRegOption(device_key, device_name, device_desc, timezone, device_attributes)
        self.add_register_reg_option(product_key, device_reg_option)
        return self
