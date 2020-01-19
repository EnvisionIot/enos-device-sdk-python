import time
from random import random
from enos.core.MqttClient import MqttClient
import random

from enos.message.upstream.resume.MeasurepointResumeBatchRequest import MeasurepointResumeBatchRequest
from enos.message.upstream.resume.MeasurepointResumeRequest import MeasurepointResumeRequest
from enos.message.upstream.status.SubDeviceLoginBatchRequest import SubDeviceLoginBatchRequest
from enos.message.upstream.status.SubDeviceLoginRequest import SubDeviceLoginRequest
from enos.sample.SampleHelper import SampleHelper


def post_measure_point_resume():
    """this sample is to resume report one measurepoint"""
    login_sub_device_request = SubDeviceLoginRequest.builder() \
        .set_sub_device_info(SampleHelper.SUB1_PRODUCT_KEY,
                             SampleHelper.SUB1_DEVICE_KEY,
                             SampleHelper.SUB1_DEVICE_SECRET) \
        .build()
    login_sub_device_response = client.publish(login_sub_device_request)
    if login_sub_device_response:
        print('login_sub_device_response:  %s' % login_sub_device_response.get_code())

    post_measure_point_request_resume = MeasurepointResumeRequest.builder() \
        .set_product_key(SampleHelper.SUB1_PRODUCT_KEY).set_device_key(SampleHelper.SUB1_DEVICE_KEY) \
        .add_measure_point('wywpoint1', random.randint(100, 200)) \
        .add_measure_points(SampleHelper.MEASURE_POINTS) \
        .build()
    post_measure_point_resume_response = client.publish(post_measure_point_request_resume)
    if post_measure_point_resume_response:
        print('post_measure_point_resume_response: %s' % post_measure_point_resume_response.get_code())


def post_measure_point_resume_batch(allow, skip):
    """this sample is to resume report batch measurepoint"""
    login_batch_sub_device_request = SubDeviceLoginBatchRequest.builder() \
        .add_sub_device_info(SampleHelper.SUB1_PRODUCT_KEY,
                             SampleHelper.SUB1_DEVICE_KEY,
                             SampleHelper.SUB1_DEVICE_SECRET) \
        .add_sub_device_info(SampleHelper.SUB3_PRODUCT_KEY,
                             SampleHelper.SUB3_DEVICE_KEY,
                             SampleHelper.SUB3_DEVICE_SECRET) \
        .build()
    login_batch_sub_device_response = client.publish(login_batch_sub_device_request)
    if login_batch_sub_device_response:
        print('login_sub_batch_response:  %s' % login_batch_sub_device_response.get_code())

    post_measure_point_resume_requests = list()
    post_measure_point_resume_requests.append(
        MeasurepointResumeRequest.builder().set_product_key(SampleHelper.SUB_DEVICES[0].get_product_key())
            .set_device_key(SampleHelper.SUB_DEVICES[0].get_device_key())
            .add_measure_point('wywpoint2', random.randint(100, 200))
            .build())
    post_measure_point_resume_requests.append(
        MeasurepointResumeRequest.builder().set_product_key(SampleHelper.SUB_DEVICES[1].get_product_key())
            .set_device_key(SampleHelper.SUB_DEVICES[1].get_device_key())
            .add_measure_point('wywpoint1', random.randint(100, 200))
            .add_measure_points(SampleHelper.MEASURE_POINTS)
            .build())

    post_measure_point_resume_batch_request = MeasurepointResumeBatchRequest.builder() \
        .add_request(post_measure_point_resume_requests[0]) \
        .add_request(post_measure_point_resume_requests[1]) \
        .add_requests(post_measure_point_resume_requests) \
        .set_allow_offline_sub_device(allow) \
        .set_skip_invalid_measurepoints(skip) \
        .build()
    post_measure_point_resume_batch_response = client.publish(post_measure_point_resume_batch_request)
    if post_measure_point_resume_batch_response:
        print('Measurepoint_Resume_Batch_response: %s' % post_measure_point_resume_batch_response.get_code())
        print('Measurepoint_Resume_Batch_response: %s' % post_measure_point_resume_batch_response.get_message())


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW1_PRODUCT_KEY, SampleHelper.GW1_DEVICE_KEY,
                        SampleHelper.GW1_DEVICE_SECRET)
    client.get_profile().set_auto_reconnect(True)  # if connection interrupted, the client can automaticlly reconnect
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync
    while True:
        post_measure_point_resume()
        timestamp = int(time.time() * 1000)
        post_measure_point_resume_batch(True, False)
        time.sleep(10)
