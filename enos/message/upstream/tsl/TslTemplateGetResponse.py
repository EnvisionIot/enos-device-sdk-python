import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse


class TslTemplateGetResponse(BaseResponse):

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.TSL_TEMPLATE_GET_REPLY)

    def decode_to_object(self, msg):
        base = TslTemplateGetResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__

    def get_attributes(self):
        data = self.get_data()
        return data.get('tslAttributeMap')

    def get_measure_points(self):
        data = self.get_data()
        return data.get('tslMeasurepointMap')

    def get_events(self):
        data = self.get_data()
        return data.get('tslEventMap')

    def get_services(self):
        data = self.get_data()
        return data.get('tslServiceMap')
