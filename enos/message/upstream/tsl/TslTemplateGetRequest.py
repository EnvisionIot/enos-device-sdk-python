from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.tsl.TslTemplateGetResponse import TslTemplateGetResponse


class TslTemplateGetRequest(BaseRequest):

    def __init__(self):
        super(TslTemplateGetRequest, self).__init__()

    @classmethod
    def builder(cls):
        return Builder()

    def get_answer_type(self):
        return TslTemplateGetResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.TSL_TEMPLATE_GET


class Builder(BaseBuilder):

    def create_method(self):
        return MethodConstants.TSL_TEMPLATE_GET

    def create_params(self):
        return dict()

    def create_request_instance(self):
        return TslTemplateGetRequest()
