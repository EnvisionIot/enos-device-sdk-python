""" When you use this login mode, please ensure that you have created message
    integration channel for the product your're using (e.g through portal ui).
"""
from enos.core.login.BaseLogin import BaseLogin

INTEGRATION_DK = '%channel%'


class MessageIntegrationLogin(BaseLogin):

    def __init__(self, server_url, product_key, product_secret):
        super(MessageIntegrationLogin,self).__init__(server_url)
        self.__server_url = server_url
        self.__product_key = product_key
        self.__product_secret = product_secret

    def get_product_key(self):
        return self.__product_key

    def get_product_secret(self):
        return self.__product_secret

    @staticmethod
    def get_device_key():
        return INTEGRATION_DK

    @staticmethod
    def get_device_secret():
        return None
