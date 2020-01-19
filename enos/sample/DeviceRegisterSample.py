from enos.core.MqttClient import MqttClient
from enos.message.upstream.register.DeviceRegisterRequest import DeviceRegisterRequest
from enos.sample.SampleHelper import SampleHelper


def device_register():
    """this sample is to register a sub_device in cloud"""
    device_register_request = DeviceRegisterRequest.builder() \
        .add_register_information(SampleHelper.SUB1_PRODUCT_KEY, 'device_key_test_1',
                                  SampleHelper.SUB_DEVICE_NAME, "dev desc", '+08:00') \
        .add_register_information(SampleHelper.SUB1_PRODUCT_KEY, 'device_key_test_attr',
                                  SampleHelper.SUB_DEVICE_NAME, "dev desc", '+08:00', SampleHelper.ATTRIBUTES)\
        .build()
    device_register_response = client.publish(device_register_request)
    if device_register_response:
        print('device_register_response: %s' % device_register_response.get_code())
        print('device_register_response: %s' % device_register_response.get_message())


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW1_PRODUCT_KEY,
                        SampleHelper.GW1_DEVICE_KEY, SampleHelper.GW1_DEVICE_SECRET)
    client.connect()
    device_register()
