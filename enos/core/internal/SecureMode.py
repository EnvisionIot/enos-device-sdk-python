from enos.core.exception.EnvisionException import EnvisionException
from enos.core.util.StringUtil import StringUtil

VIA_DEVICE_SECRET = 2
VIA_PRODUCT_SECRET = 3
VIA_PRODUCT_SECRET_FOR_INTEGRATION = 4

INTEGRATION_DK = "%channel%"


class SecureMode:

    def __init__(self, mode_id, client_id, secret):
        self.__mode_id = mode_id
        # This would server as the mqtt client id
        self.__client_id = client_id
        # Secret that's used to generate the signature
        self.__secret = secret

    def get_mode_id(self):
        return self.__mode_id

    def get_client_id(self):
        return self.__client_id

    def get_secret(self):
        return self.__secret

    @staticmethod
    def get_secure_mode(product_key, product_secret, device_key, device_secret):
        if StringUtil.is_not_empty(device_secret):
            return SecureMode(VIA_DEVICE_SECRET, device_key, device_secret)

        if StringUtil.is_not_empty(product_secret):
            if INTEGRATION_DK == device_key:
                # integration use product key as client id
                return SecureMode(VIA_PRODUCT_SECRET_FOR_INTEGRATION, product_key, product_secret)
            return SecureMode(VIA_PRODUCT_SECRET, device_key, product_secret)

        raise EnvisionException("<device_secret> or <product_secret> should be provided")
