import time

from enos.core.MqttClient import MqttClient
from enos.core.internal.Profile import Profile
from enos.message.upstream.integration.IntModelUpRawRequest import IntModelUpRawRequest
from enos.sample.SampleHelper import SampleHelper


def int_model_up_raw_post():

    int_model_up_raw_request = IntModelUpRawRequest.builder() \
        .set_payload(SampleHelper.RAW_PAYLOAD).build()
    int_model_up_raw_response = up_raw_client.publish(int_model_up_raw_request)
    print(int_model_up_raw_response.get_payload())


if __name__ == '__main__':
    integration_up_raw_profile = Profile.create_instance(SampleHelper.get_message_integration_up_raw_login())
    up_raw_client = MqttClient(profile=integration_up_raw_profile)
    up_raw_client.connect()

    while True:
        int_model_up_raw_post()
        time.sleep(5)
