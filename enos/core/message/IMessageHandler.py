from enos.core.constant.ResponseCode import ResponseCode
from enos.core.message.BaseReply import BaseReply


class IMessageHandler:
    """The arrived msg handler to be register to the sdk"""

    def on_message(self, arrived_message, arg_list):
        """ on message callback

        :param arrived_message: the arrived msg instance , it may instanceof class <BaseCommand> or <BaseResponse>
        :param arg_list: the topic args extract from the arrived topic , including productKey , deviceKey ,etc
        :return: the msg you want to reply to the cloud , if you do NOT want send msg , just return None
        """
        reply = BaseReply()
        reply.set_code(ResponseCode.COMMAND_HANDLER_NOT_REGISTERED)
        reply.set_message('downstream command handler not registered')
        return reply
