from enos.message.upstream.tsl.AttributeDeleteRequest import AttributeDeleteRequest
from enos.message.upstream.tsl.AttributeQueryRequest import AttributeQueryRequest
from enos.message.upstream.tsl.AttributeUpdateRequest import AttributeUpdateRequest
from enos.sample.SampleHelper import SampleHelper

from enos.core.MqttClient import MqttClient


def attribute_delete():
    """this sample is to delete attribute"""
    attribute_delete_request = AttributeDeleteRequest.builder() \
        .delete_attribute("wywpoint3") \
        .delete_attributes(SampleHelper.ATTRIBUTES_KEY) \
        .build()
    attribute_delete_response = client.publish(attribute_delete_request)
    if attribute_delete_response:
        print('attribute_delete_response: %s' % attribute_delete_response.get_code())


def attribute_query():
    """this sample is to query attribute value"""
    attribute_query_request = AttributeQueryRequest.builder() \
        .add_attribute("wywattribute") \
        .add_attributes(SampleHelper.ATTRIBUTES_KEY) \
        .query_all() \
        .build()
    attribute_query_response = client.publish(attribute_query_request)
    if attribute_query_response:
        print('attribute_query_response: %s' % attribute_query_response.get_code())


def attribute_update():
    """this sample is to update attribute value"""
    attribute_update_request = AttributeUpdateRequest.builder() \
        .add_attribute("wywpoint3", 6) \
        .add_attributes(SampleHelper.ATTR) \
        .build()
    attribute_update_response = client.publish(attribute_update_request)
    if attribute_update_response:
        print('attribute_update_response: %s' % attribute_update_response.get_code())


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW1_PRODUCT_KEY, SampleHelper.GW1_DEVICE_KEY,
                        SampleHelper.GW1_DEVICE_SECRET)
    client.get_profile().set_auto_reconnect(True)  # if connection interrupted, the client can automaticlly reconnect
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync
    attribute_delete()
    attribute_query()
    attribute_update()
