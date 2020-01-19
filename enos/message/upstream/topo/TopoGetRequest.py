from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest
from enos.core.message.BaseRequest import BaseBuilder
from enos.core.util.Deprecation import deprecated
from enos.message.upstream.topo.TopoGetResponse import TopoGetResponse


class TopoGetRequest(BaseRequest):

    @classmethod
    def builder(cls):
        return Builder()

    def get_answer_type(self):
        return TopoGetResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.TOPO_GET_TOPIC_FMT

    @deprecated
    def getAnswerType(self):
        return self.get_answer_type()

    @deprecated
    def _getPK_DK_FormatTopic(self):
        return self.get_format_topic()


class Builder(BaseBuilder):

    def create_method(self):
        return MethodConstants.TOPO_GET

    def create_params(self):
        return dict()

    def create_request_instance(self):
        return TopoGetRequest()

    @deprecated
    def createMethod(self):
        return self.create_method()

    @deprecated
    def createParams(self):
        return self.create_params()

    @deprecated
    def createRequestInstance(self):
        return self.create_request_instance()
