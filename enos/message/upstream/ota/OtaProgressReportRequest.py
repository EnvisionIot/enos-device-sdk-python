from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest
from enos.core.message.BaseRequest import BaseBuilder
from enos.core.util.Deprecation import deprecated
from enos.message.upstream.ota.OtaProgressReportResponse import OtaProgressReportResponse


class OtaProgressReportRequest(BaseRequest):

    @classmethod
    def builder(cls):
        return Builder()

    def check(self):
        super(OtaProgressReportRequest, self).check()

    def get_format_topic(self):
        return DeliveryTopicFormat.PROGRESS_REPORT_TOPIC_FMT

    def get_answer_type(self):
        return OtaProgressReportResponse()

    @deprecated
    def _getPK_DK_FormatTopic(self):
        return self.get_format_topic()

    @deprecated
    def getAnswerType(self):
        return self.get_answer_type()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.params = dict(step='', desc='')

    def set_step(self, step):
        self.params['step'] = step
        return self

    def set_desc(self, desc):
        self.params['desc'] = desc
        return self

    def create_method(self):
        return MethodConstants.OTA_PROGRESS

    def create_params(self):
        return self.params

    def create_request_instance(self):
        return OtaProgressReportRequest()

    @deprecated
    def setStep(self, step):
        return self.set_step(step)

    @deprecated
    def setDesc(self, desc):
        return self.set_desc(desc)

    @deprecated
    def createMethod(self):
        return self.create_method()

    @deprecated
    def createParams(self):
        return self.create_params()

    @deprecated
    def createRequestInstance(self):
        return self.create_request_instance()