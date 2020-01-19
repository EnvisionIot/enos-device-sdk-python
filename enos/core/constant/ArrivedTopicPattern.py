class ArrivedTopicPattern(object):
    GET_VERSION_TOPIC_REPLY = "/sys/(.*)/(.*)/ota/device/getversion_reply"
    INTEGRATION_MODEL_UP_RAW_REPLY = "/sys/(.*)/integration/model/up_raw_reply"
    INTEGRATION_MEASUREPOINT_POST_REPLY = "/sys/(.*)/integration/measurepoint/post_reply"
    INTEGRATION_ATTRIBUTE_POST_REPLYLY = "/sys/(.*)/integration/attribute/post_reply"
    INTEGRATION_EVENT_POST_REPLY = "/sys/(.*)/integration/event/post_reply"
    MEASUREPOINT_RESUME_REPLY = "/sys/(.*)/(.*)/thing/measurepoint/resume_reply"
    MEASUREPOINT_RESUME_BATCH_REPLY = "/sys/(.*)/(.*)/thing/measurepoint/resume/batch_reply"
    MEASUREPOINT_POST_BATCH_REPLY = "/sys/(.*)/(.*)/thing/measurepoint/post/batch_reply"
    DEVICE_REGISTER_REPLY = "/sys/(.*)/(.*)/thing/device/register_reply"
    SUB_DEVICE_LOGIN_BATCH_REPLY = "/ext/session/(.*)/(.*)/combine/login/batch_reply"
    MEASUREPOINT_POST_REPLY = "/sys/(.*)/(.*)/thing/measurepoint/post_reply"
    EVENT_POST_REPLY = "/sys/(.*)/(.*)/thing/event/(.*)/post_reply"

    TSL_TEMPLATE_GET_REPLY = "/sys/(.*)/(.*)/thing/tsltemplate/get_reply"
    MODEL_UP_RAW_REPLY = "/sys/(.*)/(.*)/thing/model/up_raw_reply"

    SUB_DEVICE_REGISTER_REPLY = "/sys/(.*)/(.*)/thing/device/register_reply"

    TOPO_ADD_REPLY = "/sys/(.*)/(.*)/thing/topo/add_reply"
    TOPO_DELETE_REPLY = "/sys/(.*)/(.*)/thing/topo/delete_reply"
    TOPO_GET_REPLY = "/sys/(.*)/(.*)/thing/topo/get_reply"

    SUB_DEVICE_LOGIN_REPLY = "/ext/session/(.*)/(.*)/combine/login_reply"
    SUB_DEVICE_LOGOUT_REPLY = "/ext/session/(.*)/(.*)/combine/logout_reply"

    TAG_UPDATE_REPLY = "/sys/(.*)/(.*)/thing/tag/update_reply"
    TAG_DELETE_REPLY = "/sys/(.*)/(.*)/thing/tag/delete_reply"

    TAG_QUERY_REPLY = "/sys/(.*)/(.*)/thing/tag/query_reply"
    ATTRIBUTE_UPDATE_REPLY = "/sys/(.*)/(.*)/thing/attribute/update_reply"
    ATTRIBUTE_QUERY_REPLY = "/sys/(.*)/(.*)/thing/attribute/query_reply"
    ATTRIBUTE_DELETE_REPLY = "/sys/(.*)/(.*)/thing/attribute/delete_reply"

    ACTIVATE_INFO = "/ext/session/(.*)/(.*)/thing/activate/info"

    SERVICE_INVOKE_COMMAND = "/sys/(.*)/(.*)/thing/service/(.*)"
    MEASUREPOINT_SET_COMMAND = "/sys/(.*)/(.*)/thing/service/measurepoint/set"
    MEASUREPOINT_GET_COMMAND = "/sys/(.*)/(.*)/thing/service/measurepoint/get"
    MODEL_DOWN_RAW_COMMAND = "/sys/(.*)/(.*)/thing/model/down_raw"
    RRPC_COMMAND = "/sys/(.*)/(.*)/rrpc/request/(.*)"

    DELETE_DEVICE_COMMAND = "/sys/(.*)/(.*)/thing/delete"
    ENABLE_DEVICE_COMMAND = "/sys/(.*)/(.*)/thing/enable"
    DISABLE_DEVICE_COMMAND = "/sys/(.*)/(.*)/thing/disable"

    SUB_DEVICE_DELETE_COMMAND = "/ext/session/(.*)/(.*)/combine/delete"
    SUB_DEVICE_ENABLE_COMMAND = "/ext/session/(.*)/(.*)/combine/enable"
    SUB_DEVICE_DISABLE_COMMAND = "/ext/session/(.*)/(.*)/combine/disable"

    DEVICE_OTA_COMMAND = "/sys/(.*)/(.*)/ota/device/upgrade"
    PROGRESS_REPORT_TOPIC_REPLY = "/sys/(.*)/(.*)/ota/device/progress_reply"
    VERSION_REPORT_TOPIC_REPLY = "/sys/(.*)/(.*)/ota/device/inform_reply"
    UPDATE_REQUEST_TOPIC_REPLY = "/sys/(.*)/(.*)/ota/device/request_reply"
