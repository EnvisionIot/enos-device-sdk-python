from enos.core.MqttClient import MqttClient
from enos.message.upstream.tsl.ModelUpRawRequest import ModelUpRawRequest
from enos.sample.SampleHelper import SampleHelper


def post_model_up_raw():
    """ Device can report raw data (such as binary data stream) """
    post_model_up_raw_request = ModelUpRawRequest.builder() \
        .set_payload(SampleHelper.RAW_PAYLOAD) \
        .build()
    post_model_up_raw_response = client.publish(post_model_up_raw_request)
    print(post_model_up_raw_response.get_payload())


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW_PRODUCT_KEY_RAW,
                        SampleHelper.GW_DEVICE_KEY_RAW, SampleHelper.GW_DEVICE_SECRET_RAW)
    client.get_profile().set_auto_reconnect(True)
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync
    post_model_up_raw()
