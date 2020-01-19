import ssl
import time

from enos.core.exception.EnvisionException import EnvisionException
from enos.core.internal.SecureMode import SecureMode
from enos.core.util.Deprecation import deprecated
from enos.core.util.SignUtil import SignUtil


class Profile(object):
    VERSION = "1.1"
    MQTTv3_1 = 3
    MQTTv3_1_1 = 4

    def __init__(self, server_url, product_key, device_key, device_secret, product_secret=None):
        self.__server_url = server_url
        self.__product_key = product_key
        self.__product_secret = product_secret
        self.__device_key = device_key
        self.__device_secret = device_secret

        self.__protocol = None
        self.__host = None
        self.__port = None
        self.__parse_url()

        self.__sign_method = SignUtil.DEFAULT_SIGN_METHOD

        self.__keep_alive_interval = 60
        self.__connection_timeout = 30
        self.__operation_timeout = 30
        self.__timestamp = str(time.time() * 1000)

        self.__max_inflight_message = 20
        self.__max_queued_message = 40
        self.__auto_reconnect_min_sec = 1
        self.__auto_reconnect_max_sec = 60

        self.__ssl_secured = False
        self.__ssl_jks_path = ''
        self.__ssl_algorithm = 'SunX509'
        self.__ssl_password = ''
        self.__ssl_root_ca_path = ''
        self.__ssl_private_key_path = ''
        self.__ssl_private_key_pass = None
        self.__ssl_certificate_path = ''

        self.__mqtt_clean_session = True
        self.__auto_reconnect = True
        self.__auto_login_sub_device = True

    @classmethod
    def create_instance(cls, base_input):
        return cls(base_input.get_server_url(), base_input.get_product_key(),
                   base_input.get_device_key(), base_input.get_device_secret(), base_input.get_product_secret())

    def __parse_url(self):
        regions = self.__server_url.split(':')
        if len(regions) == 3:
            self.__protocol = regions[0]
            self.__host = regions[1].replace('//', '')
            self.__port = int(regions[2])
        else:
            raise EnvisionException('invalid uri!')

    def get_server_url(self):
        return self.__server_url

    def set_server_url(self, server_url):
        self.__server_url = server_url

    def get_protocol(self):
        return self.__protocol

    def get_host(self):
        return self.__host

    def get_port(self):
        return self.__port

    def get_product_key(self):
        return self.__product_key

    def set_product_key(self, product_key):
        self.__product_key = product_key

    def get_device_key(self):
        return self.__device_key

    def set_device_key(self, device_key):
        self.__device_key = device_key

    def get_device_secret(self):
        return self.__device_secret

    def set_device_secret(self, device_secret):
        self.__device_secret = device_secret

    def get_keep_alive_interval(self):
        return self.__keep_alive_interval

    def set_keep_alive(self, keep_alive_interval):
        self.__keep_alive_interval = keep_alive_interval
        return self

    def get_connection_timeout(self):
        return self.__connection_timeout

    def set_connection_timeout(self, connection_timeout):
        self.__connection_timeout = connection_timeout
        return self

    def get_operation_timeout(self):
        return self.__operation_timeout

    def set_operation_timeout(self, operation_timeout):
        self.__operation_timeout = operation_timeout
        return self

    def get_max_inflight_message(self):
        return self.__max_inflight_message

    def set_max_inflight_message(self, max_inflight_message):
        self.__max_inflight_message = max_inflight_message
        return self

    def get_max_queued_message(self):
        return self.__max_queued_message

    def set_max_queued_message(self, mqtt_max_queued_message):
        self.__max_queued_message = mqtt_max_queued_message
        return self

    def get_auto_reconnect_min_sec(self):
        return self.__auto_reconnect_min_sec

    def set_auto_reconnect_min_sec(self, mqtt_auto_reconnect_min_sec):
        self.__auto_reconnect_min_sec = mqtt_auto_reconnect_min_sec
        return self

    def get_auto_reconnect_max_sec(self):
        return self.__auto_reconnect_max_sec

    def set_auto_reconnect_max_sec(self, mqtt_auto_reconnect_max_sec):
        self.__auto_reconnect_max_sec = mqtt_auto_reconnect_max_sec
        return self

    def get_client_id(self):
        return self.get_secure_mode().get_client_id() \
               + '|securemode=' + str(self.get_secure_mode().get_mode_id()) \
               + ',signmethod=' + self.__sign_method \
               + ',timestamp=' + self.__timestamp + '|'

    def get_secure_mode(self):
        return SecureMode.get_secure_mode(self.__product_key, self.__product_secret,
                                          self.__device_key, self.__device_secret)

    def get_ssl_secured(self):
        return self.__ssl_secured

    def set_ssl_secured(self, ssl_secured):
        self.__ssl_secured = ssl_secured
        return self

    def set_ssl_jks_path(self, ssl_jks_path, ssl_password):
        self.__ssl_jks_path = ssl_jks_path
        self.__ssl_password = ssl_password
        return self

    def set_ssl_algorithm(self, ssl_algorithm):
        self.__ssl_algorithm = ssl_algorithm
        return self

    def get_ssl_root_ca_path(self):
        return self.__ssl_root_ca_path

    def set_ssl_root_ca_path(self, ssl_root_ca_path):
        self.__ssl_root_ca_path = ssl_root_ca_path
        return self

    def get_ssl_private_key_path(self):
        return self.__ssl_private_key_path

    def set_ssl_private_key_path(self, ssl_private_key_path):
        self.__ssl_private_key_path = ssl_private_key_path
        return self

    def get_ssl_certificate_path(self):
        return self.__ssl_certificate_path

    def set_ssl_certificate_path(self, ssl_certificate_path):
        self.__ssl_certificate_path = ssl_certificate_path
        return self

    def get_ssl_private_key_pass(self):
        return self.__ssl_private_key_pass

    def set_ssl_private_key_pass(self, ssl_private_key_pass):
        self.__ssl_private_key_pass = ssl_private_key_pass
        return self

    def set_ssl_context(self, ssl_root_ca_path, ssl_certificate_path, ssl_private_key_path, ssl_private_key_pass=None):
        self.__ssl_root_ca_path = ssl_root_ca_path
        self.__ssl_certificate_path = ssl_certificate_path
        self.__ssl_private_key_path = ssl_private_key_path
        self.__ssl_private_key_pass = ssl_private_key_pass
        self.__ssl_secured = True
        return self

    def get_mqtt_username(self):
        return self.__device_key + '&' + self.__product_key

    def get_mqtt_password(self):
        params = dict()
        params['productKey'] = self.get_product_key()
        params['deviceKey'] = self.get_device_key()
        params['clientId'] = self.get_secure_mode().get_client_id()
        params['timestamp'] = self.__timestamp

        return SignUtil.sign(self.get_secure_mode().get_secret(), params, self.__sign_method)

    def get_sign_method(self):
        return self.__sign_method

    def set_sign_method(self, sign_method):
        self.__sign_method = sign_method

    def get_mqtt_clean_session(self):
        return self.__mqtt_clean_session

    def set_mqtt_clean_session(self, mqtt_clean_session):
        self.__mqtt_clean_session = mqtt_clean_session

    def set_auto_reconnect(self, auto_reconnect):
        if isinstance(auto_reconnect, bool):
            self.__auto_reconnect = auto_reconnect

    def get_auto_reconnect(self):
        return self.__auto_reconnect

    def set_auto_login_sub_device(self, auto_login_sub_device):
        if isinstance(auto_login_sub_device, bool):
            self.__auto_login_sub_device = auto_login_sub_device

    def get_auto_login_sub_device(self):
        return self.__auto_login_sub_device

    def create_ssl_context(self, ciphers=None):
        ca_certs = self.__ssl_root_ca_path
        cert_file = self.__ssl_certificate_path
        key_file = self.__ssl_private_key_path
        key_pass = self.__ssl_private_key_pass
        cert_reqs = ssl.CERT_REQUIRED
        tls_version = ssl.PROTOCOL_SSLv23

        if ssl is None:
            raise ValueError('This platform has no SSL/TLS.')

        if not hasattr(ssl, 'SSLContext'):
            # Require Python version that has SSL context support in standard library
            raise ValueError('Python 2.7.9 and 3.2 are the minimum supported versions for TLS.')

        if ca_certs is None and not hasattr(ssl.SSLContext, 'load_default_certs'):
            raise ValueError('ca_certs must not be None.')

        # Create SSLContext object
        if tls_version is None:
            tls_version = ssl.PROTOCOL_TLSv1
            # If the python version supports it, use highest TLS version automatically
            if hasattr(ssl, "PROTOCOL_TLS"):
                tls_version = ssl.PROTOCOL_TLS
        context = ssl.SSLContext(tls_version)

        # Configure context
        if cert_file is not None:
            context.load_cert_chain(cert_file, key_file, key_pass)

        if cert_reqs == ssl.CERT_NONE and hasattr(context, 'check_hostname'):
            context.check_hostname = False

        context.verify_mode = ssl.CERT_REQUIRED if cert_reqs is None else cert_reqs

        if ca_certs is not None:
            context.load_verify_locations(ca_certs)
        else:
            context.load_default_certs()

        if ciphers is not None:
            context.set_ciphers(ciphers)

        return context

    """ The following function only for compatibility with older versions before 0.0.8"""
    @deprecated
    def getRegionURL(self):
        return self.get_server_url()

    @deprecated
    def getProductKey(self):
        return self.get_product_key()

    @deprecated
    def getDeviceKey(self):
        return self.get_device_key()

    @deprecated
    def getDeviceSecret(self):
        return self.get_device_secret()

    @deprecated
    def getKeepAlive(self):
        return self.get_keep_alive_interval()

    @deprecated
    def setKeepAlive(self, keep_alive_interval):
        self.set_keep_alive(keep_alive_interval)

    @deprecated
    def getConnectionTimeout(self):
        return self.get_connection_timeout()

    @deprecated
    def setConnectionTimeout(self, connection_timeout):
        return self.set_connection_timeout(connection_timeout)

    @deprecated
    def getTimeToWait(self):
        return self.get_operation_timeout()

    @deprecated
    def setTimeToWait(self, operation_timeout):
        return self.set_operation_timeout(operation_timeout)

    @deprecated
    def getClientId(self):
        return self.get_client_id()

    @deprecated
    def getSSLSecured(self):
        return self.get_ssl_secured()

    @deprecated
    def setSSLSecured(self, ssl_secured):
        return self.set_ssl_secured(ssl_secured)

    @deprecated
    def setSSLJksPath(self, ssl_jks_path, ssl_password):
        return self.set_ssl_jks_path(ssl_jks_path, ssl_password)

    @deprecated
    def setSSLAlgorithm(self, ssl_algorithm):
        return self.set_ssl_algorithm(ssl_algorithm)

    @deprecated
    def getSSLRootCAPath(self):
        return self.get_ssl_root_ca_path()

    @deprecated
    def setSSLRootCAPath(self, ssl_root_ca_path):
        return self.set_ssl_root_ca_path(ssl_root_ca_path)

    @deprecated
    def getSSLPrivateKeyPath(self):
        return self.get_ssl_private_key_path()

    @deprecated
    def setSSLPrivateKeyPath(self, ssl_private_key_path):
        return self.set_ssl_private_key_path(ssl_private_key_path)

    @deprecated
    def getSSLCertificatePath(self):
        return self.get_ssl_certificate_path()

    @deprecated
    def setSSLCertificatePath(self, ssl_certificate_path):
        return self.set_ssl_certificate_path(ssl_certificate_path)

    @deprecated
    def getSSLPrivateKeyPass(self):
        return self.get_ssl_private_key_pass()

    @deprecated
    def setSSLPrivateKeyPass(self, ssl_private_key_pass):
        return self.set_ssl_private_key_pass(ssl_private_key_pass)

    @deprecated
    def setSSLContext(self, ssl_root_ca_path, ssl_certificate_path, ssl_private_key_path, ssl_private_key_pass=None):
        return self.set_ssl_context(ssl_root_ca_path, ssl_certificate_path, ssl_private_key_path, ssl_private_key_pass)

    @deprecated
    def getMqttUser(self):
        return self.get_mqtt_username()

    @deprecated
    def getMqttPassword(self):
        return self.get_mqtt_password()

    @deprecated
    def setAutoReconnect(self, auto_reconnect):
        return self.set_auto_reconnect(auto_reconnect)

    @deprecated
    def getAutoReconnect(self):
        return self.get_auto_reconnect()





