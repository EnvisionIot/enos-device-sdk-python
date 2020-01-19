class DeviceRegOption(object):

    def __init__(self, device_key, device_name, device_desc, timezone, device_attributes=None):
        self.device_key = device_key
        self.device_name = device_name
        self.device_desc = device_desc
        self.timezone = timezone
        if not device_attributes:
            self.device_attributes = dict()
        self.device_attributes = device_attributes
