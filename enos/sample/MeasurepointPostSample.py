import random
import time

from enos.message.upstream.tsl.MeasurepointPostBatchRequest import MeasurepointPostBatchRequest

from enos.message.upstream.status.SubDeviceLoginRequest import SubDeviceLoginRequest
from enos.message.upstream.tsl.MeasurepointPostRequest import MeasurepointPostRequest
from enos.sample.SampleHelper import SampleHelper

from enos.core.MqttClient import MqttClient


def post_measure_points():
    measure_point_request = MeasurepointPostRequest.builder() \
        .add_measurepoint('wywpoint2', random.randint(100, 200)) \
        .set_timestamp(int(time.time())) \
        .build()

    measure_point_response = client.publish(measure_point_request)
    if measure_point_response:
        print('measurepoint post response code: {}'.format(measure_point_response.get_code()))


def post_measure_points_batch(allow, skip):
    """Directly connected devices report data with different timestamps"""
    measure_point_post_requests = list()
    measure_point_post_requests.append(MeasurepointPostRequest.builder()
                                       .set_product_key(SampleHelper.GW1_PRODUCT_KEY)
                                       .set_device_key(SampleHelper.GW1_DEVICE_KEY)
                                       .add_measurepoint('wywpoint2', random.randint(100, 200))
                                       .set_timestamp(int(time.time() * 1000))
                                       .build())
    measure_point_post_requests.append(MeasurepointPostRequest.builder()
                                       .set_product_key(SampleHelper.GW1_PRODUCT_KEY)
                                       .set_device_key(SampleHelper.GW1_DEVICE_KEY)
                                       .add_measurepoints(SampleHelper.MEASURE_POINTS)
                                       .set_timestamp(1573061486173)
                                       .build())

    measure_point_post_batch_request = MeasurepointPostBatchRequest.builder() \
        .set_requests(measure_point_post_requests) \
        .set_allow_offline_sub_device(allow) \
        .set_skip_invalid_measurepoints(skip) \
        .build()
    measure_point_post_batch_response = client.publish(measure_point_post_batch_request)
    if measure_point_post_batch_response:
        print('post_measure_batch_point_response: %s' % measure_point_post_batch_response.get_code())


def post_measure_points_batch_sub(allow, skip):
    """This sample shows how sub-devices login and publish  measure points to broker.
       The gateway device be the proxy to make sub-device reports data in batches"""
    sub_device_login_request = SubDeviceLoginRequest.builder() \
        .set_sub_device_info(SampleHelper.SUB3_PRODUCT_KEY,
                             SampleHelper.SUB3_DEVICE_KEY,
                             SampleHelper.SUB3_DEVICE_SECRET) \
        .build()
    sub_device_login_response = client.publish(sub_device_login_request)
    if sub_device_login_response:
        print('sub_device_login_response: %s' % sub_device_login_response.get_code())

    sub_device_login_request = SubDeviceLoginRequest.builder() \
        .set_sub_device_info(SampleHelper.SUB1_PRODUCT_KEY,
                             SampleHelper.SUB1_DEVICE_KEY,
                             SampleHelper.SUB1_DEVICE_SECRET) \
        .build()
    sub_device_login_response = client.publish(sub_device_login_request)
    if sub_device_login_response:
        print('sub_device_login_response: %s' % sub_device_login_response.get_code())

    measure_point_post_requests = list()
    measure_point_post_requests.append(MeasurepointPostRequest.builder()
                                       .set_product_key(SampleHelper.SUB_DEVICES[0]
                                                        .get_product_key())
                                       .set_device_key(SampleHelper.SUB_DEVICES[0].get_device_key())
                                       .add_measurepoint('wywpoint2', random.randint(100, 200))
                                       .add_measurepoints(SampleHelper.MEASURE_POINTS)
                                       .build())

    measure_point_post_batch_request = MeasurepointPostBatchRequest.builder() \
        .set_requests(measure_point_post_requests) \
        .set_allow_offline_sub_device(allow) \
        .set_skip_invalid_measurepoints(skip) \
        .build()

    measure_point_post_batch_response = client.publish(measure_point_post_batch_request)
    if measure_point_post_batch_response:
        print('post_measure_batch_points_response: %s' % measure_point_post_batch_response.get_code())


if __name__ == '__main__':
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW1_PRODUCT_KEY, SampleHelper.GW1_DEVICE_KEY,
                        SampleHelper.GW1_DEVICE_SECRET)
    client.get_profile().set_auto_reconnect(True)  # if connection interrupted, the client can automaticlly reconnect
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync

    post_measure_points()
    post_measure_points_batch_sub(False, False)
    post_measure_points_batch(False, False)
