from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.message.BaseReply import BaseReply
from enos.core.message.BaseReply import BaseBuilder


class MeasurepointSetReply(BaseReply):

    def get_format_topic(self):
        return DeliveryTopicFormat.MEASUREPOINT_SET_REPLY

    @classmethod
    def builder(cls):
        return Builder()


class Builder(BaseBuilder):
    def create_data(self):
        return None

    def create_reply_instance(self):
        return MeasurepointSetReply()
