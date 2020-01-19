from enos.core.login.BaseLogin import BaseLogin


class DynamicActivationLogin(BaseLogin):

    def __init__(self, server_url, product_key, product_secret, device_key):
        super(DynamicActivationLogin, self).__init__(server_url)
        self.__server_url = server_url
        self.__product_key = product_key
        self.__product_secret = product_secret
        self.__device_key = device_key

    def get_product_key(self):
        return self.__product_key

    def get_product_secret(self):
        return self.__product_secret

    def get_device_key(self):
        return self.__device_key

    '''No need for the device secret for dynamically activating the device.
       Device secret would be returned from broker after this login.
    '''
    @staticmethod
    def get_device_secret():
        return None
