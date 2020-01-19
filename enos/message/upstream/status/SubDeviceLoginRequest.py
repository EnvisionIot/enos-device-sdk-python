from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.DeviceCredential import DeviceCredential
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest
from enos.core.message.BaseRequest import BaseBuilder
from enos.message.upstream.status.SubDeviceLoginInfo import SubDeviceLoginInfo
from enos.core.util.CheckUtil import CheckUtil
from enos.core.util.Deprecation import deprecated
from enos.message.upstream.status.SubDeviceLoginResponse import SubDeviceLoginResponse


class SubDeviceLoginRequest(BaseRequest):

    def __init__(self, device_credential):
        super(SubDeviceLoginRequest,self).__init__()
        self.__device_credential = device_credential

    @classmethod
    def builder(cls):
        return Builder()

    def get_device_credential(self):
        return self.__device_credential

    def get_secure_mode(self):
        return self.__device_credential.get_secure_mode()

    def check(self):
        super(SubDeviceLoginRequest, self).check()
        params = self.get_params()
        CheckUtil.check_not_empty(params['productKey'], 'subDeviceInfo.productKey')
        CheckUtil.check_not_empty(params['deviceKey'], 'subDeviceInfo.deviceKey')
        CheckUtil.check_not_empty(params['clientId'], 'subDeviceInfo.client')
        CheckUtil.check_not_empty(params['signMethod'], 'subDeviceInfo.signMethod')
        CheckUtil.check_not_empty(params['sign'], 'subDeviceInfo.sign')

    def get_format_topic(self):
        return DeliveryTopicFormat.SUB_DEVICE_LOGIN

    def get_answer_type(self):
        return SubDeviceLoginResponse()

    @deprecated
    def _getPK_DK_FormatTopic(self):
        return self.get_format_topic()

    @deprecated
    def getAnswerType(self):
        return self.get_answer_type()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__sub_device_login_info = None
        self.__device_credential = None

    def set_sub_device_info(self, product_key, device_key, device_secret):
        self.__device_credential = DeviceCredential(product_key, None, device_key, device_secret)
        return self

    def set_sub_device_credential(self, device_credential):
        self.__device_credential = device_credential
        return self

    def create_method(self):
        return MethodConstants.SUB_DEVICE_LOGIN

    def create_params(self):
        self.__sub_device_login_info = SubDeviceLoginInfo(self.__device_credential.get_product_key(),
                                                          self.__device_credential.get_product_secret(),
                                                          self.__device_credential.get_device_key(),
                                                          self.__device_credential.get_device_secret())
        return self.__sub_device_login_info.get_params()

    def create_request_instance(self):
        return SubDeviceLoginRequest(self.__device_credential)

    @deprecated
    def setSubDeviceInfo(self, product_key, device_key, device_secret):
        return self.set_sub_device_info(product_key, device_key, device_secret)

    @deprecated
    def createMethod(self):
        return self.create_method()

    @deprecated
    def createParams(self):
        return self.create_params()

    @deprecated
    def createRequestInstance(self):
        return self.create_request_instance()
