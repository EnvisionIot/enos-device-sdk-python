from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.integration.IntEventPostResponse import IntEventPostResponse


class IntEventPostRequest(BaseRequest):
    @classmethod
    def builder(cls):
        return Builder()

    def __init__(self):
        super(IntEventPostRequest, self).__init__()

    def get_message_topic(self):
        return self.get_format_topic().format(self.get_product_key())

    def get_answer_type(self):
        return IntEventPostResponse()

    def get_qos(self):
        return 0

    def get_format_topic(self):
        return DeliveryTopicFormat.INTEGRATION_EVENT_POST

    def create_method(self):
        return MethodConstants.INTEGRATION_EVENT_POST


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        # {[device_key, time]: {event_id: {str: obj} } }
        self.__events = dict()

    def set_events(self, events):
        self.__events = events
        return self

    def add_event(self, device_key, time, event_id, event_outputs):
        key = (device_key, time)
        event_dict = dict()
        if key not in self.__events:
            self.__events[key] = event_dict
        event_dict[event_id] = event_outputs
        return self

    def create_params(self):
        params = list()
        for key, value in self.__events.items():
            param = dict()
            param['deviceKey'] = key[0]
            param['time'] = key[1]
            param['events'] = value
            params.append(param)
        return params

    def create_request_instance(self):
        return IntEventPostRequest()

    def create_method(self):
        return MethodConstants.INTEGRATION_EVENT_POST
