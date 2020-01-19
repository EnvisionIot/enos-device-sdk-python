import time

from enos.message.upstream.status.SubDeviceLoginBatchRequest import SubDeviceLoginBatchRequest
from enos.message.upstream.status.SubDeviceLogoutRequest import SubDeviceLogoutRequest
from enos.sample.SampleHelper import SampleHelper
from enos.core.MqttClient import MqttClient
from enos.message.upstream.status.SubDeviceLoginRequest import SubDeviceLoginRequest


def login_sub_device():
    """ sub_device login"""
    sub_device_login_request = SubDeviceLoginRequest.builder() \
        .set_sub_device_info(SampleHelper.SUB2_PRODUCT_KEY,
                             SampleHelper.SUB2_DEVICE_KEY,
                             SampleHelper.SUB2_DEVICE_SECRET) \
        .build()
    sub_device_login_response = client.publish(sub_device_login_request)
    if sub_device_login_response:
        print('sub_device_login_response:  %s' % sub_device_login_response.get_code())


def logout_sub_device():
    """sub_device logout"""
    sub_device_logout_request = SubDeviceLogoutRequest.builder() \
        .set_sub_product_key(SampleHelper.SUB2_PRODUCT_KEY) \
        .set_sub_device_key(SampleHelper.SUB2_DEVICE_KEY) \
        .build()
    sub_device_logout_response = client.publish(sub_device_logout_request)
    if sub_device_logout_response:
        print('sub_device_logout_response:  %s' % sub_device_logout_response.get_code())


def login_batch_sub_device():
    """ sub_device login in batch"""
    sub_device_login_batch_request = SubDeviceLoginBatchRequest.builder() \
        .add_sub_device_info(SampleHelper.SUB2_PRODUCT_KEY,
                             SampleHelper.SUB2_DEVICE_KEY,
                             SampleHelper.SUB2_DEVICE_SECRET) \
        .build()
    sub_device_login_batch_response = client.publish(sub_device_login_batch_request)
    if sub_device_login_batch_response:
        print('login_batch_sub_device_response: %s' % sub_device_login_batch_response.get_code())


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW3_PRODUCT_KEY, SampleHelper.GW3_DEVICE_KEY,
                        SampleHelper.GW3_DEVICE_SECRET)
    client.get_profile().set_auto_reconnect(True)  # if connection interrupted, the client can automaticlly reconnect
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync
    login_sub_device()
    logout_sub_device()
    login_batch_sub_device()
    while True:
        time.sleep(1000)
