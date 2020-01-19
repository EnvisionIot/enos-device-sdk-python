from enos.core.MqttClient import MqttClient
from enos.sample.SampleHelper import SampleHelper

from enos.message.upstream.tsl.EventPostRequest import EventPostRequest


def event_post():
    """this sample is to post not only one event"""
    event_post_request = EventPostRequest.builder().set_event_identifier('Error') \
        .add_value("power", 124) \
        .add_values(SampleHelper.EVENTS_VALUE) \
        .build()
    event_post_response = client.publish(event_post_request)
    if event_post_response:
        print('event_post_response: %s' % event_post_response.get_code())


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW1_PRODUCT_KEY, SampleHelper.GW1_DEVICE_KEY,
                        SampleHelper.GW1_DEVICE_SECRET)
    client.get_profile().set_auto_reconnect(True)  # if connection interrupted, the client can automaticlly reconnect
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync
    event_post()
