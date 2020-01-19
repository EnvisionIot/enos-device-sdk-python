from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.message.BaseReply import BaseReply, BaseBuilder


class MeasurepointGetReply(BaseReply):
    @classmethod
    def builder(cls):
        return Builder()

    def get_format_topic(self):
        return DeliveryTopicFormat.MEASUREPOINT_GET_REPLY


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__data = dict()

    def add_measureponit(self, point_key, value):
        self.__data[point_key] = value
        return self

    def add_measureponits(self, points):
        self.__data.update(points)
        return self

    def set_measureponits(self, points):
        self.__data = points
        return self

    def create_data(self):
        return self.__data

    def create_reply_instance(self):
        return MeasurepointGetReply()
