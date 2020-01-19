import time

from enos.core.MqttClient import MqttClient
from enos.message.upstream.topo.SubDeviceInfo import SubDeviceInfo
from enos.message.upstream.topo.TopoAddRequest import TopoAddRequest
from enos.message.upstream.topo.TopoDeleteRequest import TopoDeleteRequest
from enos.message.upstream.topo.TopoGetRequest import TopoGetRequest
from enos.sample.SampleHelper import SampleHelper


def add_topo():
    """this sample is to add topo"""
    add_topo_request = TopoAddRequest.builder() \
        .add_sub_device(SubDeviceInfo(SampleHelper.SUB_PRODUCT_KEY,
                                      SampleHelper.SUB_DEVICE_KEY,
                                      SampleHelper.SUB_DEVICE_SECRET)) \
        .build()
    add_topo_response = client.publish(add_topo_request)
    if add_topo_response:
        print('topo_add_response: %s' % add_topo_response.get_code())
        print('topo_add_response: %s' % add_topo_response.get_message())


def delete_topo():
    """this sample is to delete topo"""
    delete_topo_request = TopoDeleteRequest.builder() \
        .delete_sub_device(SampleHelper.SUB_PRODUCT_KEY, SampleHelper.SUB_DEVICE_KEY)\
        .build()
    delete_topo_response = client.publish(delete_topo_request)
    if delete_topo_response:
        print('topo_delete_response: %s' % delete_topo_response.get_code())
        print('topo_delete_response: %s' % delete_topo_response.get_message())


def get_topo():
    """ this sample is to get topo"""
    get_topo_request = TopoGetRequest.builder().build()
    get_topo_response = client.publish(get_topo_request)
    if get_topo_response:
        print('topo_get_response: %s' % get_topo_response.get_code())
        print('topo_get_response: %s' % get_topo_response.get_data())


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW_PRODUCT_KEY, SampleHelper.GW_DEVICE_KEY,
                        SampleHelper.GW_DEVICE_SECRET)
    client.get_profile().set_auto_reconnect(True)
    client.setup_basic_logger('INFO')
    client.connect()  # connect in sync
    get_topo()
    # add_topo()
    get_topo()
    time.sleep(5)
    delete_topo()
    get_topo()

