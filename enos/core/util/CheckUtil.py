from enos.core.exception.EnvisionError import *
from enos.core.exception.EnvisionException import EnvisionException
from enos.core.util.StringUtil import StringUtil


class CheckUtil(object):

    @staticmethod
    def check_not_empty(value, field_name):
        if value is None:
            raise EnvisionException("parameter check error: " + field_name + " is mandatory",
                                    CODE_ERROR_MISSING_ARGS.get_error_code())
        if isinstance(value, str) and StringUtil.is_empty(value):
            raise EnvisionException("parameter check error: " + field_name + " is mandatory",
                                    CODE_ERROR_MISSING_ARGS.get_error_code())
        if isinstance(value, list) and not value:
            raise EnvisionException("parameter check error: " + field_name + " is mandatory",
                                    CODE_ERROR_MISSING_ARGS.get_error_code())
        if isinstance(value, dict) and not value:
            raise EnvisionException("parameter check error: " + field_name + " is mandatory",
                                    CODE_ERROR_MISSING_ARGS.get_error_code())

    @staticmethod
    def check_max_size(params, maxsize, field_name):
        if len(params) > maxsize:
            raise EnvisionException(CODE_ERROR_ARG_INVALID.getErrorCode(),
                                    "parameter check error: " + field_name + " is invalid, size cannot be large than " + maxsize)
