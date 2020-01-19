import time
from enos.core.MqttClient import MqttClient
from enos.message.downstream.ota.OtaUpgradeCommand import OtaUpgradeCommand
from enos.message.upstream.ota.OtaGetVersionRequest import OtaGetVersionRequest
from enos.message.upstream.ota.OtaProgressReportRequest import OtaProgressReportRequest
from enos.message.upstream.ota.OtaVersionReportRequest import OtaVersionReportRequest
from enos.sample.SampleHelper import SampleHelper


def ota_get_version_report():
    ota_get_version_report_request = OtaGetVersionRequest.builder() \
        .set_product_key(SampleHelper.GW_PRODUCT_KEY)\
        .set_device_key(SampleHelper.GW_DEVICE_KEY) \
        .build()
    ota_get_version_report_response = client.publish(ota_get_version_report_request)
    if ota_get_version_report_response:
        print('ota_get_version_report_response: %s' % ota_get_version_report_response.get_code())


def ota_report_progress(progress, desc):
    ota_report_progress_request = OtaProgressReportRequest.builder() \
        .set_product_key(SampleHelper.GW_PRODUCT_KEY) \
        .set_device_key(SampleHelper.GW_DEVICE_KEY) \
        .set_step(progress) \
        .set_desc(desc) \
        .build()
    ota_report_progress_response = client.publish(ota_report_progress_request)
    if ota_report_progress_response:
        print('ota_report_progress_response: %s' % ota_report_progress_response.get_code())


def ota_version_report(version):
    ota_version_report_request = OtaVersionReportRequest.builder() \
        .set_product_key(SampleHelper.GW_PRODUCT_KEY)\
        .set_device_key(SampleHelper.GW_DEVICE_KEY) \
        .set_version(version) \
        .build()
    ota_version_report_response = client.publish(ota_version_report_request)
    if ota_version_report_response:
        print('ota_version_report_response: %s' % ota_version_report_response.get_code())


def upgrade_firmware_handler(arrived_message, path_list):
    firmware = arrived_message.get_firmware_info()
    print("receive command: ", firmware.file_url, firmware.version)

    # TODO: download firmware from firmware.fileUrl

    # mock reporting progress
    ota_report_progress('35', 'downloading firmware finished')

    ota_report_progress('70', 'decompressing firmware finished')

    ota_report_progress('90', 'running firmware finished')

    ota_report_progress('100', 'upgrading firmware finished')

    # firmware upgrade success, report new version
    ota_version_report(firmware.version)


if __name__ == "__main__":
    client = MqttClient(SampleHelper.TCP_SERVER_URL, SampleHelper.GW_PRODUCT_KEY,
                        SampleHelper.GW_DEVICE_KEY, SampleHelper.GW_DEVICE_SECRET)
    client.get_profile().set_auto_reconnect(True)
    client.connect()  # connect in sync
    # register a handle_msg to implement the Ota function, e.g: upgrade firmware
    client.register_arrived_message_handler(OtaUpgradeCommand().get_class(), upgrade_firmware_handler)
    ota_version_report(1.0)
    ota_get_version_report()

    while True:
        time.sleep(5)
