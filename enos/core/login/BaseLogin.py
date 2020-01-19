class BaseLogin:

    def __init__(self, server_url):
        self.__server_url = server_url

    def get_server_url(self):
        return self.__server_url

    def get_product_key(self):
        pass

    def get_product_secret(self):
        pass

    def get_device_key(self):
        pass

    def get_device_secret(self):
        pass
