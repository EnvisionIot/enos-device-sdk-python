from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest
from enos.core.message.BaseRequest import BaseBuilder
import time

from enos.core.util.Deprecation import deprecated
from enos.message.upstream.tsl.MeasurepointPostResponse import MeasurepointPostResponse


class MeasurepointPostRequest(BaseRequest):

    @classmethod
    def builder(cls):
        return Builder()

    def check(self):
        super(MeasurepointPostRequest, self).check()

    def get_format_topic(self):
        return DeliveryTopicFormat.MEASUREPOINT_POST

    def get_answer_type(self):
        return MeasurepointPostResponse()

    @deprecated
    def _getPK_DK_FormatTopic(self):
        return self.get_format_topic()

    @deprecated
    def getAnswerType(self):
        return self.get_answer_type()


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__params = dict()
        self.__params['measurepoints'] = dict()
        self.__params['time'] = int(time.time() * 1000)

    # this function is to add measurepoint directly
    def add_measurepoint(self, key, value):
        self.__params['measurepoints'][key] = value
        return self

    # this function is to add measurepoint by dict
    def add_measurepoints(self, values):
        for value in values:
            self.__params['measurepoints'][value] = values[value]
        return self

    def set_measurepoints(self, value):
        self.__params['measurepoints'] = value
        return self

    def set_timestamp(self, timestamp):
        self.__params['time'] = timestamp
        return self

    def create_method(self):
        return MethodConstants.MEASUREPOINT_POST

    def create_params(self):
        return self.__params

    def create_request_instance(self):
        return MeasurepointPostRequest()

    @deprecated
    def addMeasurePoint(self, key, value):
        return self.add_measurepoint(key, value)

    @deprecated
    def addMeasurePoints(self, values):
        self.add_measurepoints(values)

    @deprecated
    def setMeasurePoints(self, value):
        self.set_measurepoints(value)

    @deprecated
    def setTimestamp(self, timestamp):
        return self.set_timestamp(timestamp)

    @deprecated
    def createMethod(self):
        self.create_method()

    @deprecated
    def createParams(self):
        self.create_method()

    @deprecated
    def createRequestInstance(self):
        self.create_request_instance()
