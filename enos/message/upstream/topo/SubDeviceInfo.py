import time
from enos.core.util.Deprecation import deprecated
from enos.core.util.SignUtil import SignUtil


class SubDeviceInfo(object):

    def __init__(self, product_key, device_key, device_secret, sign_method=SignUtil.DEFAULT_SIGN_METHOD):
        self.__product_key = product_key
        self.__device_key = device_key
        self.__device_secret = device_secret

        self.__timestamp = int(time.time() * 1000)
        self.__client_id = self.get_default_client_id(product_key, device_key)
        self.__sign_method = sign_method

        sign_params = dict()
        sign_params['productKey'] = product_key
        sign_params['deviceKey'] = device_key
        sign_params['clientId'] = self.__client_id
        sign_params['timestamp'] = str(self.__timestamp)
        self.sign = SignUtil.sign(device_secret, sign_params, self.__sign_method)

    def get_default_client_id(self, product_key, device_key):
        return "{}.{}.{}".format(product_key, device_key, str(self.__timestamp))

    def get_client_id(self):
        return self.__client_id

    def get_timestamp(self):
        return self.__timestamp

    def get_sign_method(self):
        return self.__sign_method

    def set_sign_method(self, sign_method):
        self.__sign_method = sign_method

    def get_sign(self):
        return self.sign

    def create_sign_map(self):
        params = dict()
        params['productKey'] = self.__product_key
        params['deviceKey'] = self.__device_key
        params['clientId'] = self.__client_id
        params['timestamp'] = str(self.__timestamp)
        params['signMethod'] = self.__sign_method
        params['sign'] = self.sign
        return params

    def get_product_key(self):
        return self.__product_key

    def get_device_key(self):
        return self.__device_key

    def set_product_key(self, product_key):
        self.__product_key = product_key
        return self

    def set_device_key(self, device_key):
        self.__device_key = device_key
        return self

    @deprecated
    def getDefaultClientId(self, product_key, device_key):
        return self.get_default_client_id(product_key, device_key)

    @deprecated
    def getClientId(self):
        return self.get_client_id()

    @deprecated
    def getTimestamp(self):
        return self.get_timestamp()

    @deprecated
    def getSignMethod(self):
        return self.get_sign_method()

    @deprecated
    def setSignMethod(self, sign_method):
        self.set_sign_method(sign_method)

    @deprecated
    def getSign(self):
        return self.get_sign()

    @deprecated
    def createSignMap(self):
        return self.create_sign_map()

    @deprecated
    def getProductKey(self):
        return self.get_product_key()

    @deprecated
    def setProductKey(self, product_key):
        return self.set_product_key(product_key)

    @deprecated
    def setDeviceKey(self, device_key):
        return self.set_device_key(device_key)
