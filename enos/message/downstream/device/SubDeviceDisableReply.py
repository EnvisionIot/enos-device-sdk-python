from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.message.BaseReply import BaseReply, BaseBuilder


class SubDeviceDisableReply(BaseReply):
    @classmethod
    def builder(cls):
        return Builder()

    def get_format_topic(self):
        return DeliveryTopicFormat.SUB_DEVICE_DISABLE_REPLY


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__data = ''

    def set_data(self, data):
        self.__data = data
        return self

    def create_data(self):
        return self.__data

    def create_reply_instance(self):
        return SubDeviceDisableReply()

