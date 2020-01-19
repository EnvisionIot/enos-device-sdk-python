from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest
from enos.core.message.BaseRequest import BaseBuilder
from enos.core.util.Deprecation import deprecated
from enos.message.upstream.ota.OtaVersionReportResponse import OtaVersionReportResponse


class OtaVersionReportRequest(BaseRequest):

    @classmethod
    def builder(cls):
        return Builder()

    def check(self):
        super(OtaVersionReportRequest, self).check()

    def get_format_topic(self):
        return DeliveryTopicFormat.VERSION_REPORT_TOPIC_FMT

    def get_answer_type(self):
        return OtaVersionReportResponse()

    @deprecated
    def _getPK_DK_FormatTopic(self):
        return self.get_format_topic()

    @deprecated
    def getAnswerType(self):
        return self.get_answer_type()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.params = dict(version='')

    def set_version(self, version):
        self.params['version'] = version
        return self

    def create_method(self):
        return MethodConstants.OTA_INFORM

    def create_params(self):
        return self.params

    def create_request_instance(self):
        return OtaVersionReportRequest()

    @deprecated
    def setVersion(self, version):
        return self.set_version(version)

    @deprecated
    def createMethod(self):
        return self.create_method()

    @deprecated
    def createParams(self):
        return self.create_params()

    @deprecated
    def createRequestInstance(self):
        return self.create_request_instance()
