from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest
from enos.core.message.BaseRequest import BaseBuilder
from enos.core.util.CheckUtil import CheckUtil
from enos.core.util.Deprecation import deprecated
from enos.message.upstream.topo.TopoAddResponse import TopoAddResponse


class TopoAddRequest(BaseRequest):

    @classmethod
    def builder(cls):
        return Builder()

    def check(self):
        super(TopoAddRequest, self).check()
        params = self.get_params()
        for param in params:
            CheckUtil.check_not_empty(param['productKey'], 'subDeviceInfo.productKey')
            CheckUtil.check_not_empty(param['deviceKey'], 'subDeviceInfo.deviceKey')
            CheckUtil.check_not_empty(param['clientId'], 'subDeviceInfo.clientId')
            CheckUtil.check_not_empty(param['signMethod'], 'subDeviceInfo.signMethod')
            CheckUtil.check_not_empty(param['sign'], 'subDeviceInfo.sign')

    def get_format_topic(self):
        return DeliveryTopicFormat.TOPO_ADD_TOPIC_FMT

    def get_answer_type(self):
        return TopoAddResponse()

    @deprecated
    def getAnswerType(self):
        return self.get_answer_type()

    @deprecated
    def _getPK_DK_FormatTopic(self):
        return self.get_format_topic()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__sub_device_info_list = list()

    def set_sub_device_info_list(self, sub_device_info_list):
        self.__sub_device_info_list = sub_device_info_list
        return self

    # this function means that you can only add sub_device_info one by one
    def add_sub_device(self, device_info):
        self.__sub_device_info_list.append(device_info)
        return self

    # this function means that you can add many sub_device
    def add_sub_devices(self, device_infos):
        self.__sub_device_info_list.extend(device_infos)
        return self

    def create_method(self):
        return MethodConstants.TOPO_ADD

    def create_params(self):
        params = list()
        for device_info in self.__sub_device_info_list:
            params.append(device_info.create_sign_map())
        return params

    def create_request_instance(self):
        return TopoAddRequest()

    @deprecated
    def setSubDeviceInfoList(self, sub_device_info_list):
        return self.set_sub_device_info_list(sub_device_info_list)

    @deprecated
    def addSubDevice(self, device_info):
        return self.add_sub_device(device_info)

    @deprecated
    def addSubDevices(self, device_infos):
        return self.add_sub_devices(device_infos)

    @deprecated
    def createMethod(self):
        return self.create_method()

    @deprecated
    def createParams(self):
        return self.create_params()

    @deprecated
    def createRequestInstance(self):
        return self.create_request_instance()
