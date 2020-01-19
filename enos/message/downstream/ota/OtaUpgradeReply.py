from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.message.BaseReply import BaseReply, BaseBuilder


class OtaUpgradeReply(BaseReply):
    @classmethod
    def builder(cls):
        return Builder()

    def get_format_topic(self):
        return DeliveryTopicFormat.DEVICE_OTA_REPLY


class Builder(BaseBuilder):
    def create_data(self):
        return ""

    def create_reply_instance(self):
        return OtaUpgradeReply()
