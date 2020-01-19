import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseCommand import BaseCommand
from enos.message.downstream.tsl.ServiceInvocationReply import ServiceInvocationReply


class ServiceInvocationCommand(BaseCommand):

    def get_answer_type(self):
        return ServiceInvocationReply()

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.SERVICE_INVOKE_COMMAND)

    def decode_to_object(self, msg):
        base = ServiceInvocationCommand()
        base.__dict__ = msg
        return base

    def match(self, topic):
        args = self.get_match_topic_pattern().findall(topic)
        # topic match conflict with measurepoint set and measurepoint get
        if len(args) == 3 and ('measurepoint/set' == args[2] or 'measurepoint/get' == args[2]):
            return None
        return args

    @classmethod
    def get_class(cls):
        return cls.__name__
