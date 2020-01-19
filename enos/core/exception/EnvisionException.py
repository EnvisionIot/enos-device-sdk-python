

class EnvisionException(Exception):
    def __init__(self, message, code=None):
        self.__message = message
        self.__code = code

    @classmethod
    def build(cls, envision_error):
        exception = cls(envision_error.get_error_message, envision_error.get_error_code)
        return exception
