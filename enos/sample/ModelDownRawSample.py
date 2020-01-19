import time

from enos.core.MqttClient import MqttClient
from enos.message.downstream.tsl.ModelDownRawCommand import ModelDownRawCommand
from enos.message.downstream.tsl.ModelDownRawReply import ModelDownRawReply
from enos.sample.SampleHelper import SampleHelper


def down_raw_handler(arrived_message, arg_list):
    payload = arrived_message.get_payload()
    print('receive model down raw message, payload: {}'.format(payload))

    reply = ModelDownRawReply()
    reply.set_payload(SampleHelper.RAW_PAYLOAD_REPLY)
    reply.set_code(200)
    return reply


if __name__ == '__main__':
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.SUB_PRODUCT_KEY_DOWN_RAW,
                        SampleHelper.SUB_DEVICE_KEY_DOWN_RAW, SampleHelper.SUB_DEVICE_SECRET_DOWN_RAW)

    client.setup_basic_logger('INFO')

    client.register_arrived_message_handler(ModelDownRawCommand.get_class(), down_raw_handler)

    client.connect()  # connect in sync

    while True:
        time.sleep(5)
