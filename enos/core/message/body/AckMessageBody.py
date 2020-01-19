import json
from enos.core.util.Deprecation import deprecated


class AckMessageBody(object):
    """ This class describes the message that's used to acknowledge
        This could be a command reply {BaseReply} from client to broker or
        a request response {BaseResponse} from broker to client.
    """

    def __init__(self):
        self.qos = 1
        self.id = ''
        self.code = 0
        self.message = ''
        self.data = dict()

    def encode(self):
        payload = {
            "id": self.id,
            "code": self.code,
            "data": self.data,
            "message": self.message
        }
        return json.dumps(payload)

    def get_qos(self):
        return self.qos

    def set_qos(self, qos):
        self.qos = qos

    def get_id(self):
        if hasattr(self, 'id'):
            return self.id

    def set_id(self, message_id):
        self.id = message_id

    def get_code(self):
        if hasattr(self, 'code'):
            return self.code

    def set_code(self, code):
        self.code = code

    def get_data(self):
        if hasattr(self, 'data'):
            return self.data

    def set_data(self, data):
        self.data = data

    def get_message(self):
        if hasattr(self, 'message'):
            return self.message

    def set_message(self, message):
        self.message = message

    @deprecated
    def getQos(self):
        return self.get_qos()

    @deprecated
    def setQos(self, qos):
        self.set_qos(qos)

    @deprecated
    def getId(self):
        return self.get_id()

    @deprecated
    def setId(self, id):
        self.set_id(id)

    @deprecated
    def getCode(self):
        return self.get_code()

    @deprecated
    def setCode(self, code):
        self.set_code(code)

    @deprecated
    def getData(self):
        return self.get_data()

    @deprecated
    def setData(self, data):
        self.set_data(data)

    @deprecated
    def getMessage(self):
        return self.get_message()

    @deprecated
    def setMessage(self, message):
        self.set_message(message)
