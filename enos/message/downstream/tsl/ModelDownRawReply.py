from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.message.BaseReply import BaseReply


class ModelDownRawReply(BaseReply):
    def __init__(self, payload=bytes()):
        super(ModelDownRawReply, self).__init__()
        self.__payload = payload

    def get_format_topic(self):
        return DeliveryTopicFormat.MODEL_DOWN_RAW_REPLY

    def set_payload(self, payload):
        self.__payload = payload

    def get_payload(self):
        return self.__payload

    def encode(self):
        return self.__payload
