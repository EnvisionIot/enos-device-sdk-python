# coding=utf-8
class ResponseCode:

    # 成功
    SUCCESS = 200

    # 内部服务错误， 处理时发生内部错误
    INTERNAL_ERR = 400

    # 请求参数错误， 设备入参校验失败
    PARAMETER_ERR = 460

    DEVICE_NOT_EXISTS = 402

    AUTH_ERR = 401

    # 请求过于频繁，设备端处理不过来时可以使用
    TOO_MANY_REQUESTS = 429

    # 设备端注册服务执行错误
    COMMAND_HANDLER_EXECUTION_FAILED = 500

    COMMAND_HANDLER_NOT_REGISTERED = 1101

    USER_DEFINED_ERR_CODE = 2000

    PAYLOAD_MUST_BE_JSON_FORMAT = 6207

    # 服务器端超时，返回的响应码
    TIME_OUT = 6205

    # 设备端等待响应超时
    LOCAL_TIME_OUT = 6305

    # RRPC的响应服务没有提供
    RRPC_HANDLER_NOT_FOUND = 10001

    # 从100000到110000用于设备自定义错误信息，和云端错误信息加以区分
    DEVICE_DEFINED_ERR = 100000