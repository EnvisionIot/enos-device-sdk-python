import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseCommand import BaseCommand
from enos.core.message.IArrivedMessage import DecodeResult
from enos.message.downstream.tsl.ModelDownRawReply import ModelDownRawReply


class ModelDownRawCommand(BaseCommand):

    def __init__(self, payload=bytes()):
        super(ModelDownRawCommand, self).__init__()
        self.__payload = payload

    def set_payload(self, payload):
        self.__payload = payload

    def get_payload(self):
        return self.__payload

    def decode(self, topic, payload):
        path_list = self.match(topic)
        if not path_list:
            return None
        path_list = path_list[0]
        model_down_raw_command = ModelDownRawCommand(payload)
        return DecodeResult(model_down_raw_command, path_list)

    def get_answer_type(self):
        return ModelDownRawReply()

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.MODEL_DOWN_RAW_COMMAND)

    @classmethod
    def get_class(cls):
        return cls.__name__
