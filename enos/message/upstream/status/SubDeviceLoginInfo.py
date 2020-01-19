import time

from enos.core.internal.SecureMode import SecureMode
from enos.core.util.Deprecation import deprecated
from enos.core.util.SignUtil import SignUtil


class SubDeviceLoginInfo(object):

    def __init__(self, product_key, product_secret, device_key, device_secret,
                 sign_method=None, timestamp=None, client_id=None, clean_session=None):
        self.__product_key = product_key
        self.__device_key = device_key

        if timestamp:
            self.__timestamp = timestamp
        else:
            self.__timestamp = int(time.time() * 1000)

        if client_id:
            self.__client_id = client_id
        else:
            self.__client_id = self.get_default_client_id(product_key, device_key)

        if clean_session:
            self.__clean_session = clean_session
        else:
            self.__clean_session = False

        if sign_method:
            self.__sign_method = sign_method
        else:
            self.__sign_method = SignUtil.DEFAULT_SIGN_METHOD

        self.__sign_params = dict()
        self.__sign_params['productKey'] = self.__product_key
        self.__sign_params['deviceKey'] = self.__device_key
        self.__sign_params['clientId'] = self.__client_id
        self.__sign_params['timestamp'] = str(self.__timestamp)

        self.__secure_mode = SecureMode.get_secure_mode(product_key, product_secret, device_key, device_secret)
        self.__sign = SignUtil.sign(self.__secure_mode.get_secret(), self.__sign_params, self.__sign_method)

        self.__params = self.__sign_params.copy()
        self.__params['sign'] = self.__sign
        self.__params['secureMode'] = str(self.__secure_mode.get_mode_id())
        self.__params['signMethod'] = self.__sign_method
        self.__params['cleanSession'] = str(self.__clean_session)

    def get_params(self):
        return self.__params

    def get_product_key(self):
        return self.__product_key

    def get_device_key(self):
        return self.__device_key

    def get_sign_method(self):
        return self.__sign_method

    def get_sign(self):
        return self.__sign

    def get_secure_mode(self):
        return self.__secure_mode

    @staticmethod
    def get_default_client_id(product_key, device_key):
        return product_key + device_key + str(int(time.time() * 1000))

    @deprecated
    def getSignParams(self):
        return self.get_params()

    @deprecated
    def getDefaultClientId(self, product_key, device_key):
        return self.get_default_client_id(product_key, device_key)

    @deprecated
    def getProductKey(self):
        return self.get_product_key()

    @deprecated
    def getDeviceKey(self):
        return self.get_device_key()
