import json
from abc import ABCMeta, abstractmethod

from enos.core.exception.EnvisionException import EnvisionException


class IArrivedMessage:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_match_topic_pattern(self):
        pass

    @abstractmethod
    def decode_to_object(self, msg):
        pass

    @abstractmethod
    def get_class(self):
        pass

    def match(self, topic):
        return self.get_match_topic_pattern().findall(topic)

    def decode(self, topic, payload):
        # format of match result: [(product_key, device_key),...]
        path_list = self.match(topic)
        if not path_list:
            return None
        try:
            path_list = path_list[0]
            arrived_msg = json.loads(payload)
            arrived_object = self.decode_to_object(arrived_msg)
        except Exception as e:
            raise EnvisionException(e)

        arrived_object.set_message_topic(topic)

        if len(path_list) > 0:
            arrived_object.set_product_key(path_list[0])

        if len(path_list) > 1:
            arrived_object.set_device_key(path_list[1])

        return DecodeResult(arrived_object, path_list)


class DecodeResult(object):

    def __init__(self, arrived_msg, path_value_list):
        self.__arrived_msg = arrived_msg
        self.__path_list = path_value_list

    def get_path_list(self):
        return self.__path_list

    def get_topic_path(self, index):
        return self.__path_list[index]

    def get_arrived_msg(self):
        return self.__arrived_msg
