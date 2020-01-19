import datetime
from datetime import datetime

from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.tsl.MeasurepointPostBatchResponse import MeasurepointPostBatchResponse


class MeasurepointPostBatchRequest(BaseRequest):
    def __init__(self):
        super(MeasurepointPostBatchRequest,self).__init__()
        self.__allow_offline_sub_device = ''
        self.__skip_invalid_measurepoints = ''

    @classmethod
    def builder(cls):
        return Builder()

    def get_answer_type(self):
        return MeasurepointPostBatchResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.MEASUREPOINT_POST_BATCH

    def get_json_payload(self):
        payload = super(MeasurepointPostBatchRequest,self).get_json_payload()
        payload['allowOfflineSubDevice'] = self.get_allow_offline_sub_device()
        payload['skipInvalidMeasurepoints'] = self.get_skip_invalid_measurepoints()
        return payload

    def get_allow_offline_sub_device(self):
        return self.__allow_offline_sub_device

    def get_skip_invalid_measurepoints(self):
        return self.__skip_invalid_measurepoints

    def set_allow_offline_sub_device(self, allow_offline_sub_device):
        self.__allow_offline_sub_device = allow_offline_sub_device

    def set_skip_invalid_measurepoints(self, skip_invalid_measurepoints):
        self.__skip_invalid_measurepoints = skip_invalid_measurepoints


class Builder(BaseBuilder):
    def __init__(self):
        super(Builder, self).__init__()
        self.__requests = list()
        self.__allow_offline_sub_device = ''
        self.__skip_invalid_measurepoints = ''

    def set_requests(self, requests):
        self.__requests = requests
        return self

    def add_request(self, request):
        self.__requests.append(request)
        return self

    def add_requests(self, requests):
        self.__requests.extend(requests)
        return self

    def set_allow_offline_sub_device(self, allow_offline_sub_device):
        self.__allow_offline_sub_device = allow_offline_sub_device
        return self

    def set_skip_invalid_measurepoints(self, skip_invalid_measurepoints):
        self.__skip_invalid_measurepoints = skip_invalid_measurepoints
        return self

    def create_method(self):
        return MethodConstants.MEASUREPOINT_POST_BATCH

    def create_params(self):
        params = list()
        for request in self.__requests:
            param = dict()
            if request.get_product_key() is not None:
                param['productKey'] = request.get_product_key()
            if request.get_device_key() is not None:
                param['deviceKey'] = request.get_device_key()
            param_dict = request.get_params()
            if param_dict.__contains__('measurepoints'):
                param['measurepoints'] = param_dict.get('measurepoints')
            if param_dict.__contains__('time'):
                param['time'] = param_dict.get('time')
            else:
                param['time'] = datetime.utcnow()
            params.append(param)
        return params

    def create_request_instance(self):
        return MeasurepointPostBatchRequest()

    def build(self):
        request = super(Builder, self).build()
        request.set_allow_offline_sub_device(self.__allow_offline_sub_device)
        request.set_skip_invalid_measurepoints(self.__skip_invalid_measurepoints)
        return request
