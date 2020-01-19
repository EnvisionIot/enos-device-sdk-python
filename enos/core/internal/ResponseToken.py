import threading
import time

from enos.core.exception.EnvisionException import EnvisionException


class ResponseToken:

    def __init__(self, response_id, callback=None):
        self.__response_id = response_id
        self.__callback = callback
        self.__condition = threading.Condition()
        self.__response = None
        self.__exception = None
        self.__callback_invoked = False

    def get_response_id(self):
        return self.__response_id

    def wait_for_response(self, timeout):
        timestamp = int(round(time.time() * 1000))
        with self.__condition:
            while self.__is_completed() is False:
                try:
                    self.__condition.wait(timeout)
                except Exception as e:
                    self.__exception = e

                if self.__is_completed() is False and timeout > 0 and timestamp + timeout * 1000 <= int(
                        round(time.time() * 1000)):
                    self.__exception = EnvisionException('synchronize request timeout')

        self.__invoke_callback()

        if self.__exception is not None:
            raise self.__exception

        return self.__response

    def mark_success(self, response):
        if response is None:
            raise EnvisionException('response is null')
        self.__response = response
        self.__do_notify()

    def mark_failure(self, exception):
        if exception is None:
            raise EnvisionException('exception is null')
        self.__exception = exception
        self.__do_notify()

    def __do_notify(self):
        self.__invoke_callback()
        with self.__condition:
            self.__condition.notify_all()

    def __invoke_callback(self):
        if self.__callback is not None and self.__callback_invoked is False:
            if self.__response is not None:
                self.__callback.on_response(self.__response)
            else:
                self.__callback.on_failure(self.__exception)

            self.__callback_invoked = True

    def __is_completed(self):
        return self.__response is not None or self.__exception is not None
