import time

from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.tsl.EventPostResponse import EventPostResponse
from enos.core.util.CheckUtil import CheckUtil


class EventPostRequest(BaseRequest):

    def __init__(self, event_identifier):
        super(EventPostRequest, self).__init__()
        self.__eventIdentifier = event_identifier

    def check(self):
        super(EventPostRequest,self).check()
        CheckUtil.check_not_empty(self.__eventIdentifier, 'event.identifier')

    def get_message_topic(self):
        return self.get_format_topic().format(self.get_product_key(), self.get_device_key(), self.__eventIdentifier)

    def get_answer_type(self):
        return EventPostResponse()

    def get_qos(self):
        return 0

    def get_format_topic(self):
        return DeliveryTopicFormat.EVENT_POST

    @classmethod
    def builder(cls):
        return Builder()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__event_identifier = ""
        self.__params = dict()
        self.__params['events'] = dict()
        self.__params['time'] = int(time.time() * 1000)

    def set_event_identifier(self, event_identifier):
        self.__event_identifier = event_identifier
        return self

    def add_value(self, point, value):
        values = self.__params.get('events')
        values[point] = value
        return self

    def add_values(self, value):
        values = self.__params.get('events')
        values.update(value)
        return self

    def set_values(self, value):
        self.__params['events'] = value
        return self

    def set_timestamp(self, timestamp):
        self.__params['time'] = timestamp
        return self

    def create_method(self):
        return MethodConstants.EVENT_POST + self.__event_identifier

    def create_params(self):
        return self.__params

    def create_request_instance(self):
        return EventPostRequest(self.__event_identifier)
