from enos.core.MqttClient import MqttClient
from enos.message.upstream.tsl.TslTemplateGetRequest import TslTemplateGetRequest
from enos.sample.SampleHelper import SampleHelper


def get_tsl_templete():
    """this sample is to get model template,such as model id、ou etc."""
    get_tsl_template_request = TslTemplateGetRequest.builder().build()
    get_tsl_template_response = client.publish(get_tsl_template_request)
    if get_tsl_template_response:
        print('get_tsl_template_response: %s' % get_tsl_template_response.get_code())


def get_sub_tsl_templete():
    """this sample is to get model sub device template,such as modelid、ou etc."""
    get_tsl_sub_template_request = TslTemplateGetRequest.builder() \
        .set_product_key(SampleHelper.SUB_PRODUCT_KEY_TSL_TEMPLATE)\
        .set_device_key(SampleHelper.SUB_DEVICE_KEY_TSL_TEMPLATE)\
        .build()
    get_tsl_sub_template_response = client.publish(get_tsl_sub_template_request)
    if get_tsl_sub_template_response:
        print('tsl_sub_template_response:  %s' % get_tsl_sub_template_response.get_code())


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW1_PRODUCT_KEY,
                        SampleHelper.GW1_DEVICE_KEY, SampleHelper.GW1_DEVICE_SECRET)
    client.get_profile().set_auto_reconnect(True)
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync
    get_tsl_templete()
    get_sub_tsl_templete()
