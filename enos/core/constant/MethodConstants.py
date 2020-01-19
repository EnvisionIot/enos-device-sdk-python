class MethodConstants(object):
    OTA_GETVERSION = "Ota.device.getversion"

    ININTEGRATION_MEASUREPOINT_POST = "integration.measurepoint.post"
    INTEGRATION_MODEL_UP_RAW = "integration.model.up_raw"
    INTEGRATION_EVENT_POST = "integration.event.post"
    INTEGRATION_ATTRIBUTE_POST = "integration.attribute.post"

    MEASUREPOINT_RESUME = "thing.measurepoint.resume"
    MEASUREPOINT_RESUME_BATCH = "thing.measurepoint.resume.batch"
    MEASUREPOINT_POST_BATCH = "thing.measurepoint.post.batch"
    SUB_DEVICE_LOGIN_BATCH = "combine.login.batch"
    SUB_DEVICE_LOGIN = "combine.login"
    SUB_DEVICE_LOGOUT = "combine.logout"

    THING_LOGIN = "thing.login"

    THING_DISABLE = "thing.disable"
    THING_ENABLE = "thing.enable"
    THING_DELETE = "thing.delete"

    THING_MODEL_UP_RAW = "thing.model.up_raw"

    MEASUREPOINT_POST = "thing.measurepoint.post"

    MEASUREPOINT_SET = "thing.service.measurepoint.set"

    EVENT_POST = "thing.event.%s.post"

    TSL_TEMPLATE_GET = "thing.tsltemplate.get"

    DEVICE_REGISTER = "thing.device.register"

    TAG_DELETE = "thing.tag.delete"
    TAG_UPDATE = "thing.tag.update"
    TAG_QUERY = "thing.tag.query"

    TOPO_ADD = "thing.topo.add"
    TOPO_DELETE = "thing.topo.delete"
    TOPO_GET = "thing.topo.get"

    SERVICE_INOVKE = "thing.service.%s"

    OTA_PROGRESS = "ota.progress"

    OTA_INFORM = "ota.inform"

    OTA_REQUEST = "ota.request"

    SUB_DEVICE_DISABLE = "combine.disable"
    SUB_DEVICE_ENABLE = "combine.enable"
    SUB_DEVICE_DELETE = "combine.delete"

    ATTRIBUTE_UPDATE = "thing.attribute.update"
    ATTRIBUTE_QUERY = "thing.attribute.query"
    ATTRIBUTE_DELETE = "thing.attribute.delete"
