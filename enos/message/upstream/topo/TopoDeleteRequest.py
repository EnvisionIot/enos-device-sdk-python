from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest
from enos.core.message.BaseRequest import BaseBuilder
from enos.core.util.Deprecation import deprecated
from enos.message.upstream.topo.TopoDeleteResponse import TopoDeleteResponse


class TopoDeleteRequest(BaseRequest):

    @classmethod
    def builder(cls):
        return Builder()

    def get_format_topic(self):
        return DeliveryTopicFormat.TOPO_DELETE_TOPIC_FMT

    def get_answer_type(self):
        return TopoDeleteResponse()

    @deprecated
    def getAnswerType(self):
        return self.get_answer_type()

    @deprecated
    def _getPK_DK_FormatTopic(self):
        return self.get_format_topic()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.sub_device_list = list()

    def set_sub_devices(self, sub_device_list):
        self.sub_device_list = sub_device_list
        return self

    def set_sub_device_list(self, sub_device_list):
        self.sub_device_list = sub_device_list
        return self

    def delete_sub_device(self, product_key, device_key):
        self.sub_device_list.append((product_key, device_key))
        return self

    def delete_sub_devices(self, sub_device_list):
        for sub_device in sub_device_list:
            self.sub_device_list.append(sub_device)
        return self

    def add_sub_device_list(self, sub_device_list):
        for sub_device in sub_device_list:
            self.sub_device_list.append(sub_device)
        return self

    def create_method(self):
        return MethodConstants.TOPO_DELETE

    def create_params(self):
        params = list()
        for sub_device in self.sub_device_list:
            if len(sub_device) >= 2:
                sub_device_dict = dict()
                sub_device_dict['productKey'] = sub_device[0]
                sub_device_dict['deviceKey'] = sub_device[1]
                params.append(sub_device_dict)
        return params

    def create_request_instance(self):
        return TopoDeleteRequest()

    @deprecated
    def setSubDevices(self, sub_device_list):
        return self.set_sub_devices(sub_device_list)

    @deprecated
    def setSubDeviceList(self, sub_device_list):
        return self.set_sub_device_list(sub_device_list)

    @deprecated
    def addSubDevice(self, product_key, device_key):
        return self.delete_sub_device(product_key, device_key)

    @deprecated
    def addSubDevices(self, sub_device_list):
        return self.delete_sub_devices(sub_device_list)

    @deprecated
    def addSubDeviceList(self, sub_device_list):
        return self.add_sub_device_list(sub_device_list)

    @deprecated
    def createMethod(self):
        return self.create_method()

    @deprecated
    def createParams(self):
        return self.create_params()

    @deprecated
    def createRequestInstance(self):
        return self.create_request_instance()
