import threading


class ConcurrentSet(object):

    def __init__(self):
        self.__lock = threading.Lock()
        self.__concurrent_set = set()

    def exists(self, item):
        return item in self.__concurrent_set

    def add(self, item):
        with self.__lock:
            self.__concurrent_set.add(item)

    def discard(self, item):
        with self.__lock:
            self.__concurrent_set.discard(item)

    def copy(self):
        with self.__lock:
            return self.__concurrent_set.copy()

    def clear(self):
        with self.__lock:
            self.__concurrent_set.clear()
