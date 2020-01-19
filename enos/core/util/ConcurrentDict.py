import threading


class ConcurrentDict(object):

    def __init__(self):
        self.__lock = threading.Lock()
        self.__concurrent_dict = dict()

    def exists(self, key):
        return key in self.__concurrent_dict.keys()

    def get(self, key):
        return self.__concurrent_dict.get(key, None)

    def add(self, key, value):
        with self.__lock:
            self.__concurrent_dict[key] = value

    def pop(self, key):
        with self.__lock:
            if self.exists(key):
                return self.__concurrent_dict.pop(key)

    def copy(self):
        with self.__lock:
            return self.__concurrent_dict.copy()

    def clear(self):
        with self.__lock:
            self.__concurrent_dict.clear()
