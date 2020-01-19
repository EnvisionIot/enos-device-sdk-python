from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.message.BaseReply import BaseReply, BaseBuilder


class DeviceActivateReply(BaseReply):
    @classmethod
    def builder(cls):
        return Builder()

    def get_format_topic(self):
        return DeliveryTopicFormat.ACTIVATE_INFO_REPLY


class Builder(BaseBuilder):

    def create_data(self):
        return None

    def create_reply_instance(self):
        return DeviceActivateReply()
