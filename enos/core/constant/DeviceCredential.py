from enos.core.internal.SecureMode import SecureMode
from enos.core.util.StringUtil import StringUtil


class DeviceCredential:

    def __init__(self, product_key, product_secret, device_key, device_secret):
        self.__product_key = None
        self.__product_secret = None
        self.__device_key = None
        self.__device_secret = None
        if StringUtil.is_not_empty(product_key):
            self.__product_key = product_key.strip()
        if StringUtil.is_not_empty(product_secret):
            self.__product_secret = product_secret.strip()
        if StringUtil.is_not_empty(device_key):
            self.__device_key = device_key.strip()
        if StringUtil.is_not_empty(device_secret):
            self.__device_secret = device_secret.strip()

    def get_product_key(self):
        return self.__product_key

    def get_product_secret(self):
        return self.__product_secret

    def get_device_key(self):
        return self.__device_key

    def get_device_secret(self):
        return self.__device_secret

    def get_secure_mode(self):
        return SecureMode.get_secure_mode(self.__product_key, self.__product_secret,
                                          self.__device_key, self.__device_secret)
