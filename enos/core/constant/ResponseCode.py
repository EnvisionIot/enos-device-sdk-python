# coding=utf-8
class ResponseCode:

    """ success"""
    SUCCESS = 200

    """ server error when process internal"""
    INTERNAL_ERR = 400

    """ request parameter error, device parameter validation failed"""
    PARAMETER_ERR = 460

    """ device not exist"""
    DEVICE_NOT_EXISTS = 402

    """auth failed"""
    AUTH_ERR = 401

    """ request are too frequency"""
    TOO_MANY_REQUESTS = 429

    """ device service execution error"""
    COMMAND_HANDLER_EXECUTION_FAILED = 500

    """ device handler not registered"""
    COMMAND_HANDLER_NOT_REGISTERED = 1101

    """ user define error code"""
    USER_DEFINED_ERR_CODE = 2000

    """ payload must be json format"""
    PAYLOAD_MUST_BE_JSON_FORMAT = 6207

    """ server timeout"""
    TIME_OUT = 6205

    """ local timeout"""
    LOCAL_TIME_OUT = 6305

    """ rrpc response service is not provided"""
    RRPC_HANDLER_NOT_FOUND = 10001

    """ device customized error code"""
    DEVICE_DEFINED_ERR = 100000