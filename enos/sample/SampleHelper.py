import locale
from enos.core.MqttClient import MqttClient
from enos.core.constant.DeviceCredential import DeviceCredential
from enos.core.login.DynamicActivationLogin import DynamicActivationLogin
from enos.core.login.MessageIntegrationLogin import MessageIntegrationLogin
from enos.core.login.NormalDeviceLogin import NormalDeviceLogin
from enos.core.util.StringI18n import StringI18n
from enos.message.upstream.topo.SubDeviceInfo import SubDeviceInfo


class SampleHelper:
    TCP_SERVER_URL = "tcp://xxx:11883"  # for beta tcp connection

    SSL_SERVER_URL = "ssl://xxx:18883"  # for beta ssl connection

    GW_PRODUCT_KEY = "gw_product_key"
    GW_PRODUCT_SECRET = "gw_product_secret"

    GW_DEVICE_KEY = "gw_device_key"
    GW_DEVICE_SECRET = "gw_device_secret"

    # measurepoint_resume/device_register/report_measurepoint
    GW1_PRODUCT_KEY = "gw1_product_key"
    GW1_PRODUCT_SECRET = "gw1_product_secret"

    GW1_DEVICE_KEY = "gw1_device_key"
    GW1_DEVICE_SECRET = "gw1_device_secret"

    # get_tsl_template/attribute_query
    GW2_PRODUCT_KEY = "gw2_product_key"
    GW2_PRODUCT_SECRET = "gw2_product_secret"

    GW2_DEVICE_KEY = "gw2_device_key"
    GW2_DEVICE_SECRET = "gw2_device_secret"

    # login_device/ota/topo
    GW3_PRODUCT_KEY = "gw3_product_key"
    GW3_PRODUCT_SECRET = "gw3_product_secret"
    GW3_DEVICE_KEY = "gw3_device_key"
    GW3_DEVICE_SECRET = "gw3_device_secret"

    GW_PRODUCT_KEY_RAW = "gw_product_key_raw"
    GW_PRODUCT_SECRET_RAW = "gw_product_secret_raw"
    GW_DEVICE_KEY_RAW = "gw_device_key_raw"
    GW_DEVICE_SECRET_RAW = "gw_device_secret_raw"

    # sud_device
    SUB_PRODUCT_KEY = "sub_product_key"
    SUB_PRODUCT_SECRET = "sub_product_secret"
    SUB_DEVICE_KEY = "sub_device_key"
    SUB_DEVICE_SECRET = "sub_device_secret"

    # up raw device
    SUB_PRODUCT_KEY_RAW = "sub_product_key_raw"
    SUB_PRODUCT_SECRET_RAW = "sub_product_secret_raw"
    SUB_DEVICE_KEY_RAW = "sub_device_key_raw"
    SUB_DEVICE_SECRET_RAW = "sub_device_secret_raw"

    # down raw device
    SUB_PRODUCT_KEY_DOWN_RAW = "sub_product_key_down_raw"
    SUB_PRODUCT_SECRET_DOWN_RAW = "sub_product_secret_down_raw"
    SUB_DEVICE_KEY_DOWN_RAW = "sub_device_key_down_raw"
    SUB_DEVICE_SECRET_DOWN_RAW = "sub_device_secret_down_raw"

    # get_sub_tsl_template
    SUB_PRODUCT_KEY_TSL_TEMPLATE = "sub_product_key_tsl_template"
    SUB_PRODUCT_SECRET_TSL_TEMPLATE = "sub_product_secret_tsl_template"
    SUB_DEVICE_KEY_TSL_TEMPLATE = "sub_device_key_tsl_template"
    SUB_DEVICE_SECRET_TSL_TEMPLATE = "sub_device_secret_tsl_template"

    # topo request
    SUB_PRODUCT_KEY_TOPO = "sub_product_key_topo"
    SUB_PRODUCT_SECRET_TOPO = "sub_product_secret_topo"
    SUB_DEVICE_KEY_TOPO = "sub_device_key_topo"
    SUB_DEVICE_SECRET_TOPO = "sub_device_secret_topo"

    # device_register/MEASUREPOINT_BATCH_RESUME/report_measurepoint
    SUB1_PRODUCT_KEY = "sub1_product_key"
    SUB1_PRODUCT_SECRET = "sub1_product_secret"
    SUB1_DEVICE_KEY = "sub1_device_key"
    SUB1_DEVICE_SECRET = "sub1_device_secret"

    # loginbatch/Ota
    SUB2_PRODUCT_KEY = "sub2_product_key"
    SUB2_PRODUCT_SECRET = "sub2_product_secret"
    SUB2_DEVICE_KEY = "sub2_device_key"
    SUB2_DEVICE_SECRET = "sub2_device_secret"

    SUB3_PRODUCT_KEY = "sub3_product_key"
    SUB3_PRODUCT_SECRET = "sub3_product_secret"
    SUB3_DEVICE_KEY = "sub3_device_key"
    SUB3_DEVICE_SECRET = "sub3_device_secret"

    EVENT_DICT = {'temp': 120.0, 'desc': 'temp too high'}
    # for model_up_raw
    RAW_PAYLOAD = bytes([0x01, 0x00, 0x00, 0x00, 0x14, 0x01, 0x00, 0x04, 0x00, 0x00, 0x26, 0xf5])
    RAW_PAYLOAD_REPLY = bytes([0x02, 0x00, 0x00, 0x00, 0x14, 0x00, 0xc8])

    DYNAMIC_ACTIVATE_PRODUCT_KEY = "dynamic_activate_product_key"
    DYNAMIC_ACTIVATE_PRODUCT_SECRET = "dynamic_activate_product_secret"
    DYNAMIC_ACTIVATE_DEVICE_KEY = "dynamic_activate_device_key"

    SUB_DEVICE_NAME = (StringI18n("auto_test OldDeviceEnosApiTest device1111"))
    SUB_DEVICE_NAME.set_localized_value(locale.setlocale(locale.LC_ALL, 'zh_CN'), '中文设备01')
    SUB_DEVICE_NAME.set_localized_value(locale.setlocale(locale.LC_ALL, 'en_US'), 'eng_dev_01')

    CLIENT = MqttClient(TCP_SERVER_URL, GW2_PRODUCT_KEY, GW2_DEVICE_KEY, GW2_DEVICE_SECRET)
    SUB_DEVICE = DeviceCredential(SUB_PRODUCT_KEY, None, SUB_DEVICE_KEY, SUB_DEVICE_SECRET)

    # for report measure_points
    MEASURE_POINTS = {'measurepoint1': 99, 'measurepoint2': 00}
    # for attributes query
    ATTR = {'attribute1': 4, 'attribute2': 5}
    ATTRIBUTES_KEY = {'attribute1', 'attribute2'}
    EVENTS_VALUE = {'time': 2, 'weather': 6.0}
    # for  add sub_devices topo test
    SUB_DERVICES_FOR_ADD_TOPO = list()
    SUB_DERVICES_FOR_TOPO1 = SubDeviceInfo(SUB2_PRODUCT_KEY, SUB2_DEVICE_KEY, SUB2_DEVICE_SECRET)
    SUB_DERVICES_FOR_TOPO2 = SubDeviceInfo(SUB_PRODUCT_KEY_RAW, SUB_DEVICE_KEY_RAW, SUB_DEVICE_SECRET_RAW)
    SUB_DERVICES_FOR_ADD_TOPO.append(SUB_DERVICES_FOR_TOPO1)
    SUB_DERVICES_FOR_ADD_TOPO.append(SUB_DERVICES_FOR_TOPO2)
    # for delete sub_devices topo test
    SUB_DERVICES_FOR_DELETE_TOPO = list()
    SUB_DERVICES_FOR_TOPO1 = (SUB2_PRODUCT_KEY, SUB2_DEVICE_KEY)
    SUB_DERVICES_FOR_TOPO2 = (SUB_PRODUCT_KEY_RAW, SUB_DEVICE_KEY_RAW)
    SUB_DERVICES_FOR_DELETE_TOPO.append(SUB_DERVICES_FOR_TOPO1)
    SUB_DERVICES_FOR_DELETE_TOPO.append(SUB_DERVICES_FOR_TOPO2)

    SUB_DEVICES = list()
    SUB_DEVICES.append(DeviceCredential(SUB1_PRODUCT_KEY, "", SUB1_DEVICE_KEY, SUB1_DEVICE_SECRET))
    SUB_DEVICES.append(DeviceCredential(SUB3_PRODUCT_KEY, "", SUB3_DEVICE_KEY, SUB3_DEVICE_SECRET))
    TAGS = {'tag1': 30, 'tag2': 40}

    ATTRIBUTES = {'attribute': 1, 'attribute2': 3}

    @classmethod
    def get_device_static_login(cls):
        return NormalDeviceLogin(cls.TCP_SERVER_URL, cls.GW_PRODUCT_KEY, cls.GW_DEVICE_KEY, cls.GW_DEVICE_SECRET)

    @classmethod
    def get_device_static_ssl_login(cls):
        return NormalDeviceLogin(cls.SSL_SERVER_URL, cls.GW_PRODUCT_KEY, cls.GW_DEVICE_KEY, cls.GW_DEVICE_SECRET)

    @classmethod
    def get_device_dynamic_login(cls):
        return DynamicActivationLogin(cls.TCP_SERVER_URL, cls.DYNAMIC_ACTIVATE_PRODUCT_KEY,
                                      cls.DYNAMIC_ACTIVATE_PRODUCT_SECRET, cls.DYNAMIC_ACTIVATE_DEVICE_KEY)

    @classmethod
    def get_message_integration_login(cls):
        return MessageIntegrationLogin(cls.TCP_SERVER_URL, cls.GW_PRODUCT_KEY, cls.GW_PRODUCT_SECRET)

    @classmethod
    def get_message_integration_up_raw_login(cls):
        return MessageIntegrationLogin(cls.TCP_SERVER_URL, cls.SUB_PRODUCT_KEY_RAW, cls.SUB_PRODUCT_SECRET_RAW)
