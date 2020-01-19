import time

from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.constant.MethodConstants import MethodConstants
from enos.core.message.BaseRequest import BaseRequest, BaseBuilder
from enos.message.upstream.resume.MeasurepointResumeBatchResponse import MeasurepointResumeBatchResponse


class MeasurepointResumeBatchRequest(BaseRequest):

    def __init__(self):
        super(MeasurepointResumeBatchRequest,self).__init__()
        self.__allow_offline_sub_device = ''
        self.__skip_invalid_measurepoints = ''

    @classmethod
    def builder(cls):
        return Builder()

    def get_answer_type(self):
        return MeasurepointResumeBatchResponse()

    def get_format_topic(self):
        return DeliveryTopicFormat.MEASUREPOINT_RESUME_BATCH

    def get_json_payload(self):
        payload = super(MeasurepointResumeBatchRequest,self).get_json_payload()
        payload['allowOfflineSubDevice'] = self.get_allow_offline_sub_device()
        payload['skipInvalidMeasurepoints'] = self.get_skip_invalid_measurepoints()
        return payload

    def set_allow_offline_sub_device(self, allow_offline_subdevice):
        self.__allow_offline_sub_device = allow_offline_subdevice

    def set_skip_invalid_measurepoints(self, skip_invalid_measurepoints):
        self.__skip_invalid_measurepoints = skip_invalid_measurepoints

    def get_allow_offline_sub_device(self):
        return self.__allow_offline_sub_device

    def get_skip_invalid_measurepoints(self):
        return self.__skip_invalid_measurepoints


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__requests = list()
        self.__allow_offline_sub_device = ''
        self.__skip_invalid_measurepoints = ''

    def set_requests(self, requests):
        self.__requests = requests
        return self

    def add_requests(self, requests):
        self.__requests.extend(requests)
        return self

    def add_request(self, request):
        self.__requests.append(request)
        return self

    def set_allow_offline_sub_device(self, allow_offline_sub_device):
        self.__allow_offline_sub_device = allow_offline_sub_device
        return self

    def set_skip_invalid_measurepoints(self, skip_invalid_measurepoints):
        self.__skip_invalid_measurepoints = skip_invalid_measurepoints
        return self

    def create_method(self):
        return MethodConstants.MEASUREPOINT_RESUME_BATCH

    def create_params(self):
        params = list()
        for request in self.__requests:
            param = dict()
            if request.get_product_key():
                param['productKey'] = request.get_product_key()
            if request.get_device_key() is not None:
                param['deviceKey'] = request.get_device_key()
            params_dict = request.get_params()
            if params_dict.__contains__('measurepoints'):
                param['measurepoints'] = params_dict.get('measurepoints')
            if params_dict.__contains__('time'):
                param['time'] = params_dict.get('time')
            else:
                param['time'] = time.time()
            params.append(param)
        return params

    def create_request_instance(self):
        return MeasurepointResumeBatchRequest()

    def build(self):
        request = super(Builder,self).build()
        request.set_allow_offline_sub_device(self.__allow_offline_sub_device)
        request.set_skip_invalid_measurepoints(self.__skip_invalid_measurepoints)
        return request
