import hashlib

from enos.core.exception.EnvisionException import EnvisionException
from enos.core.util.StringUtil import StringUtil


class SignUtil(object):
    DEFAULT_SIGN_METHOD = 'hmacsha256'
    SHA256 = 'hmacsha256'
    MD5 = 'hmacmd5'
    SHA1 = 'hmacsha1'

    @classmethod
    def sign(cls, app_secret, params, sign_method):
        if StringUtil.is_empty(sign_method):
            raise EnvisionException('sign method is empty')
        content = SignUtil.__make_string(app_secret, params)
        if sign_method == cls.SHA256:
            return cls.sha256_sign(content)
        if sign_method == cls.MD5:
            return cls.md5_sign(content)
        if sign_method == cls.SHA1:
            return cls.sha1_sign(content)
        else:
            raise EnvisionException('invalid sign method')

    @staticmethod
    def __make_string(app_secret, params):
        sign_str = ''
        if params:
            # Dictionary sort the parameter names
            keys = sorted(params.keys())
            for key in keys:
                sign_str += key + str(params[key])

        sign_str += app_secret
        return sign_str

    @staticmethod
    def sha1_sign(content):
        sha1 = hashlib.sha1()
        sha1.update(content.encode('utf8'))
        # to upper case for compatibility of historical reason
        return sha1.hexdigest().upper()

    @staticmethod
    def sha256_sign(content):
        sha256 = hashlib.sha256()
        sha256.update(content.encode('utf8'))
        return sha256.hexdigest()

    @staticmethod
    def md5_sign(content):
        md5 = hashlib.md5()
        md5.update(content.encode('utf8'))
        return md5.hexdigest()
