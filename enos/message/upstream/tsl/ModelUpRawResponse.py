import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse
from enos.core.message.IArrivedMessage import DecodeResult


class ModelUpRawResponse(BaseResponse):

    def __init__(self, payload=None):
        super(ModelUpRawResponse, self).__init__()
        self.__payload = payload

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.MODEL_UP_RAW_REPLY)

    def decode_to_object(self, msg):
        base = ModelUpRawResponse()
        base.__dict__ = msg
        return base

    def set_payload(self, payload):
        self.__payload = payload

    def get_payload(self):
        return self.__payload

    def decode(self, topic, payload):
        path = self.match(topic)
        if path is None or len(path) <= 0:
            return None
        arrived_obj = ModelUpRawResponse()
        arrived_obj.set_id("unknown")
        arrived_obj.set_payload(payload)
        arrived_obj.set_message_topic(topic)
        if len(path) > 0 and len(path[0]) > 0:
            arrived_obj.set_product_key(path[0][0])

        if len(path) > 0 and len(path[0]) > 1:
            arrived_obj.set_device_key(path[0][1])
        return DecodeResult(arrived_obj, path)

    @classmethod
    def get_class(cls):
        return cls.__name__
