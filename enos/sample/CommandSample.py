from time import sleep

from enos.message.downstream.tsl.MeasurepointGetReply import MeasurepointGetReply

from enos.message.downstream.tsl.MeasurepointGetCommand import MeasurepointGetCommand

from enos.message.downstream.tsl.MeasurepointSetReply import MeasurepointSetReply

from enos.core.MqttClient import MqttClient
from enos.message.downstream.tsl.MeasurepointSetCommand import MeasurepointSetCommand
from enos.sample.SampleHelper import SampleHelper


def set_measurepoint_command_handler(arrived_message, arg_list):
    """ message callback, handle the received downstream message and implement your logic

    :param arrived_message: the arrived msg instance , it may instanceof class <BaseCommand> or <BaseResponse>
    :param arg_list: the topic args extract from the arrived topic , including productKey , deviceKey ,etc
    :return: the msg you want to reply to the cloud , if you do NOT want send msg , just return None
    """
    print('receive measurepoint set command, params: {}'.format(arrived_message.get_params()))

    print('product key = {}, device key= {}'.format(arg_list[0], arg_list[1]))

    return MeasurepointSetReply().builder()\
        .set_code(200)\
        .set_message('measurepoints set success')\
        .build()


def get_measurepoint_command_handler(arrived_message, arg_list):
    print('receive measurepoint get command, params: {}'.format(arrived_message.get_params()))

    print('product key = {}, device key= {}'.format(arg_list[0], arg_list[1]))

    return MeasurepointGetReply().builder()\
        .set_code(200) \
        .add_measurepoint('wwww0001', 2) \
        .set_message('measurepoints get success')\
        .build()


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW_PRODUCT_KEY, SampleHelper.GW_DEVICE_KEY,
                        SampleHelper.GW_DEVICE_SECRET)
    client.get_profile().set_auto_reconnect(True)  # if connection interrupted, the client can automaticlly reconnect
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync

    # register a msg handler to handle the downstream measurepoint set command
    client.register_arrived_message_handler(MeasurepointSetCommand.get_class(), set_measurepoint_command_handler)
    client.register_arrived_message_handler(MeasurepointGetCommand.get_class(), get_measurepoint_command_handler)

    while True:
        sleep(5)
