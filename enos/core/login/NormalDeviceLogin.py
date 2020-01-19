from enos.core.login.BaseLogin import BaseLogin


class NormalDeviceLogin(BaseLogin):

    def __init__(self, server_url, product_key, device_key, device_secret):
        super(NormalDeviceLogin,self).__init__(server_url)
        self.__server_url = server_url
        self.__product_key = product_key
        self.__device_key = device_key
        self.__device_secret = device_secret

    def get_product_key(self):
        return self.__product_key

    def get_device_key(self):
        return self.__device_key

    def get_device_secret(self):
        return self.__device_secret
