from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.integration.IntMeaturepointPostResponse import IntMeaturepointPostResponse


class IntMeaturepointPostRequest(BaseRequest):

    @classmethod
    def builder(cls):
        return Builder()

    def get_format_topic(self):
        return DeliveryTopicFormat.INTEGRATION_MEASUREPOINT_POST

    def get_answer_type(self):
        return IntMeaturepointPostResponse()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        # {(device_key, time), {point_id: value} }
        self.__measurepoints = dict()

    def get_measurepoints(self):
        return self.__measurepoints

    def set_measurepoints(self, measurepoints):
        self.__measurepoints = measurepoints
        return self

    def add_meaturepoint(self, device_key, time, measurepoint_values):
        key = (device_key, time)
        if key not in self.__measurepoints:
            self.__measurepoints[key] = measurepoint_values
        else:
            self.__measurepoints[key].update(measurepoint_values)
        return self

    def create_method(self):
        return MethodConstants.ININTEGRATION_MEASUREPOINT_POST

    def create_params(self):
        params = list()
        if self.__measurepoints:
            for key, value in self.__measurepoints.items():
                param = dict()
                param['deviceKey'] = key[0]
                param['time'] = key[1]
                param['measurepoints'] = value
                params.append(param)
        return params

    def create_request_instance(self):
        return IntMeaturepointPostRequest()