import re

from enos.core.constant.ArrivedTopicPattern import ArrivedTopicPattern
from enos.core.message.BaseResponse import BaseResponse
from enos.core.util.CheckUtil import CheckUtil


class SubDeviceLoginBatchResponse(BaseResponse):

    def __init__(self):
        super(SubDeviceLoginBatchResponse, self).__init__()
        self._successResults = list()
        self._failureResults = list()

    def get_match_topic_pattern(self):
        return re.compile(ArrivedTopicPattern.SUB_DEVICE_LOGIN_BATCH_REPLY)

    def decode_to_object(self, msg):
        base = SubDeviceLoginBatchResponse()
        base.__dict__ = msg
        return base

    @classmethod
    def get_class(cls):
        return cls.__name__

    def has_severe_error(self):
        return super(SubDeviceLoginBatchResponse, self).is_success() is False \
               and self.get_success_results() is not None \
               and self.get_failure_results() is not None

    def get_success_results(self):
        if self._successResults is not None:
            return self._successResults
        success_results = self.get_results('loginedSubDevices')
        return success_results

    def get_failure_results(self):
        if self._failureResults is not None:
            return self._failureResults
        self._failureResults = self.get_results("loginedSubDevices")
        return self._failureResults

    def get_results(self, field):
        results = list()
        data = self.get_data()
        if data is None or data.__contains__(field) is None:
            return results
        sub_services = data.get(field)
        for sub_dict in sub_services:
            result = LoginSuccessResult(sub_dict.get['productKey'],
                                        sub_dict.get['deviceKey'],
                                        sub_dict.get['assetId'],
                                        sub_dict.get['deviceSecret'])
            results.append(result)
        return results


class LoginSuccessResult:
    # This is only available when dynamic activation is applied
    def __init__(self, product_key, device_key, asset_id, device_secret):
        CheckUtil.check_not_empty(product_key, 'product_key')
        CheckUtil.check_not_empty(device_key, 'device_key')
        CheckUtil.check_not_empty(asset_id, 'asset_id')
        self.product_key = product_key
        self.device_key = device_key
        self.assert_id = asset_id
        self.device_secret = device_secret


class LoginFailureResult:
    def __init__(self, product_key, device_key):
        CheckUtil.check_not_empty(device_key, 'device_key')
        self.product_key = product_key
        self.device_key = device_key
