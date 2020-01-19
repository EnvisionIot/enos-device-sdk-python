from enos.core.message.BaseReply import BaseReply, BaseBuilder
from enos.core.constant.DeliveryTopicFormat import DeliveryTopicFormat
from enos.core.exception.EnvisionException import EnvisionException
from enos.core.util.CheckUtil import CheckUtil


class ServiceInvocationReply(BaseReply):

    def __init__(self):
        super(ServiceInvocationReply, self).__init__()
        self.__service_identifier = ''

    @classmethod
    def builder(cls):
        return Builder()

    def get_format_topic(self):
        return DeliveryTopicFormat.SERVICE_INVOKE_REPLY

    def set_topic_args(self, args):
        if len(args) != 3:
            raise EnvisionException('topic args size not match!')
        self.set_product_key(args[0])
        self.set_device_key(args[1])
        self.set_service_identifier(args[2])

    def check(self):
        super(ServiceInvocationReply, self).check()
        CheckUtil.check_not_empty(self.__service_identifier, 'service.identifier')

    def get_message_topic(self):
        return self.get_format_topic().format(self.get_product_key(), self.get_device_key(), self.__service_identifier)

    def set_service_identifier(self, service_identifier):
        self.__service_identifier = service_identifier

    def get_service_identifier(self):
        return self.__service_identifier


class Builder(BaseBuilder):

    def __init__(self):
        super(Builder, self).__init__()
        self.__dict = dict()

    def add_output_data(self, point, values):
        self.__dict[point] = values
        return self

    def add_output_datas(self, values):
        self.__dict.update(values)

    def set_output_datas(self, values):
        self.__dict = values

    def create_data(self):
        return self.__dict

    def create_reply_instance(self):
        return ServiceInvocationReply()

