import time

from enos.core.MqttClient import MqttClient
from enos.message.downstream.tsl.ServiceInvocationCommand import ServiceInvocationCommand
from enos.message.downstream.tsl.ServiceInvocationReply import ServiceInvocationReply
from enos.sample.SampleHelper import SampleHelper


def service_command_handler(arrived_message, arg_list):
    print('receive service invocation command: {}, args: {}'.format(arrived_message, arg_list))
    product_key = arg_list[0]
    device_key = arg_list[1]
    service_name = arg_list[2]
    params = arrived_message.get_params()

    print('service params: {}'.format(params))

    if service_name == 'multiply':
        left = params.get('left')
        right = params.get('right')
        return ServiceInvocationReply.builder()\
            .add_output_data('result', left*right)\
            .set_code(200)\
            .build()
    else:
        return ServiceInvocationReply.builder().set_message('unknown service:').set_code(220).build()


if __name__ == '__main__':
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW_PRODUCT_KEY,
                        SampleHelper.GW_DEVICE_KEY, SampleHelper.GW_DEVICE_SECRET)

    client.register_arrived_message_handler(ServiceInvocationCommand.get_class(), service_command_handler)

    client.connect()  # connect in sync

    while True:
        time.sleep(5)


