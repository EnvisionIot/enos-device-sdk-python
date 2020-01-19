import json
from enos.core.util.Deprecation import deprecated


class AnswerableMessageBody(object):
    """ This class describes a message that can be answered/replied by the receiver.
        This could be a an up-stream request <BaseRequest> from client to broker or
        a down-stream command <BaseCommand> from broker to client.
    """

    def __init__(self):
        self.id = ''
        self.version = '1.0'
        self.method = ''
        self.params = dict()
        self.__message_size = 0

    def encode(self):
        json_string = json.dumps(self.get_json_payload())
        self.__message_size = len(json_string)
        return json_string

    def get_json_payload(self):
        payload = {
            "id": self.get_id(),
            "version": self.get_version(),
            "method": self.get_method(),
            "params": self.get_params(),
        }
        return payload

    def get_message_size(self):
        return self.__message_size

    def get_id(self):
        return self.id

    def set_id(self, message_id):
        self.id = message_id

    def get_method(self):
        return self.method

    def set_method(self, method):
        self.method = method

    def get_version(self):
        return self.version

    def set_version(self, version):
        self.version = version

    def get_params(self):
        return self.params

    def set_params(self, params):
        self.params = params

    @deprecated
    def getId(self):
        return self.get_id()

    @deprecated
    def setId(self, id):
        self.set_id(id)

    @deprecated
    def getMethod(self):
        return self.get_method()

    @deprecated
    def setMethod(self, method):
        self.set_method(method)

    @deprecated
    def getVersion(self):
        return self.version

    @deprecated
    def setVersion(self, version):
        self.set_version(version)

    @deprecated
    def getParams(self):
        return self.get_params()

    @deprecated
    def setParams(self, params):
        self.set_params(params)
