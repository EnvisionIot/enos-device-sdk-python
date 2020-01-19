from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.ota.OtaGetVersionResponse import OtaGetVersionResponse


class OtaGetVersionRequest(BaseRequest):
    @classmethod
    def builder(cls):
        return Builder()

    def get_answer_type(self):
        return OtaGetVersionResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.GET_VERSION_TOPIC_FMT

    def __init__(self):
        super(OtaGetVersionRequest, self).__init__()


class Builder(BaseBuilder):

    def __init__(self):
        super().__init__()
        self.param_dict = dict()

    def create_method(self):
        return MethodConstants.OTA_GETVERSION

    def create_params(self):
        return self.param_dict

    def create_request_instance(self):
        return OtaGetVersionRequest()
