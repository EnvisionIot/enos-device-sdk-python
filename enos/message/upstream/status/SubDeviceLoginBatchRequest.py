import time

from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.DeviceCredential import DeviceCredential
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.core.util.SignUtil import SignUtil
from enos.message.upstream.status.SubDeviceLoginBatchResponse import SubDeviceLoginBatchResponse
from enos.message.upstream.status.SubDeviceLoginInfo import SubDeviceLoginInfo
from enos.core.util.CheckUtil import CheckUtil


class SubDeviceLoginBatchRequest(BaseRequest):

    def __init__(self):
        super(SubDeviceLoginBatchRequest,self).__init__()

    @classmethod
    def builder(cls):
        return Builder()

    def check(self):
        super(SubDeviceLoginBatchRequest, self).check()
        params = self.get_params()
        CheckUtil.check_not_empty(params['timestamp'], 'timestamp')
        CheckUtil.check_not_empty(params['subDevices'], 'subDevices')
        CheckUtil.check_not_empty(params['clientId'], 'clientId')
        CheckUtil.check_not_empty(params['signMethod'], 'signMethod')

    def get_answer_type(self):
        return SubDeviceLoginBatchResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.SUB_DEVICE_LOGIN_BATCH


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__client_id = "login.batch"
        self.__timestamp = 0
        self.__sign_method = SignUtil.DEFAULT_SIGN_METHOD
        self.__sub_device_credentials = list()

    def add_sub_device_info(self, product_key, device_key, device_secret):
        return self.add_sub_device_credentials(DeviceCredential(product_key, None, device_key, device_secret))

    def add_sub_device_credentials(self, credential):
        self.__sub_device_credentials.append(credential)
        return self

    def create_method(self):
        return MethodConstants.SUB_DEVICE_LOGIN_BATCH

    def create_params(self):
        params = dict()
        params["clientId"] = self.__client_id
        if int(self.__timestamp) <= 0:
            self.__timestamp = str(time.time())
        params["timestamp"] = str(self.__timestamp)
        params["signMethod"] = self.__sign_method

        sub_device_list = list()
        for credential in self.__sub_device_credentials:
            sub_device = SubDeviceLoginInfo(credential.get_product_key(), None,
                                            credential.get_device_key(), credential.get_device_secret(),
                                            self.__sign_method, self.__timestamp, self.__client_id, False)
            sub_dev_data = dict()
            sub_dev_data["productKey"] = credential.get_product_key()
            sub_dev_data["deviceKey"] = credential.get_device_key()
            sub_dev_data["secureMode"] = str(sub_device.get_secure_mode().get_mode_id())
            sub_dev_data["sign"] = sub_device.get_sign()
            sub_device_list.append(sub_dev_data)

        if len(sub_device_list) > 0:
            params["subDevices"] = sub_device_list
        return params

    def set_client_id(self, client_id):
        self.__client_id = client_id

    def set_timestamp(self, timestamp):
        self.__timestamp = timestamp

    def set_sign_method(self, sign_method):
        self.__sign_method = sign_method

    def create_request_instance(self):
        return SubDeviceLoginBatchRequest()
