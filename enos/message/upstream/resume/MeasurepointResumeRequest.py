import time

from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.resume.MeasurepointResumeResponse import MeasurepointResumeResponse


class MeasurepointResumeRequest(BaseRequest):
    def __init__(self):
        super(MeasurepointResumeRequest, self).__init__()

    @classmethod
    def builder(cls):
        return Builder()

    def get_answer_type(self):
        return MeasurepointResumeResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.MEASUREPOINT_RESUME


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__params = dict()
        self.__params['measurepoints'] = dict()
        self.__params['time'] = int(time.time() * 1000)

    def add_measure_point(self, key, value):
        values = self.__params.get('measurepoints')
        values[key] = value
        return self

    def add_measure_point_with_quality(self, key, value, quality):
        values = self.__params.get('measurepoints')
        value_with_qualities = dict()
        value_with_qualities['value'] = value
        value_with_qualities['quality'] = quality
        values[key] = value_with_qualities
        return self

    def add_measure_points(self, values):
        for value in values:
            self.__params['measurepoints'][value] = values[value]
        return self

    def set_measure_points(self, value):
        self.__params['measurepoints'] = value
        return self

    def set_timestamp(self, timestamp):
        self.__params['time'] = timestamp
        return self

    def create_method(self):
        return MethodConstants.MEASUREPOINT_RESUME

    def create_params(self):
        return self.__params

    def create_request_instance(self):
        return MeasurepointResumeRequest()
