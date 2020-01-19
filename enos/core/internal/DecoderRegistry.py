from enos.core.exception.EnvisionException import EnvisionException


class DecoderRegistry(object):
    decoder_list = list()

    packages = {
        'enos.message.upstream.tsl.MeasurepointPostResponse': 'MeasurepointPostResponse',
        'enos.message.upstream.tsl.MeasurepointPostBatchResponse': 'MeasurepointPostBatchResponse',
        'enos.message.upstream.tsl.AttributeQueryResponse': 'AttributeQueryResponse',
        'enos.message.upstream.tsl.AttributeDeleteResponse': 'AttributeDeleteResponse',
        'enos.message.upstream.tsl.AttributeUpdateResponse': 'AttributeUpdateResponse',
        'enos.message.upstream.tsl.EventPostResponse': 'EventPostResponse',
        'enos.message.upstream.tsl.ModelUpRawResponse': 'ModelUpRawResponse',
        'enos.message.upstream.tsl.TslTemplateGetResponse': 'TslTemplateGetResponse',

        'enos.message.upstream.integration.IntMeaturepointPostResponse': 'IntMeaturepointPostResponse',
        'enos.message.upstream.integration.IntEventPostResponse': 'IntEventPostResponse',
        'enos.message.upstream.integration.IntAttributePostResponse': 'IntAttributePostResponse',
        'enos.message.upstream.integration.IntModelUpRawResponse': 'IntModelUpRawResponse',

        'enos.message.upstream.tag.TagDeleteResponse': 'TagDeleteResponse',
        'enos.message.upstream.tag.TagQueryResponse': 'TagQueryResponse',
        'enos.message.upstream.tag.TagUpdateResponse': 'TagUpdateResponse',

        'enos.message.upstream.status.SubDeviceLoginResponse': 'SubDeviceLoginResponse',
        'enos.message.upstream.status.SubDeviceLogoutResponse': 'SubDeviceLogoutResponse',
        'enos.message.upstream.status.SubDeviceLoginBatchResponse': 'SubDeviceLoginBatchResponse',

        'enos.message.upstream.topo.TopoAddResponse': 'TopoAddResponse',
        'enos.message.upstream.topo.TopoGetResponse': 'TopoGetResponse',
        'enos.message.upstream.topo.TopoDeleteResponse': 'TopoDeleteResponse',

        'enos.message.upstream.resume.MeasurepointResumeBatchResponse': 'MeasurepointResumeBatchResponse',
        'enos.message.upstream.resume.MeasurepointResumeResponse': 'MeasurepointResumeResponse',

        'enos.message.upstream.ota.OtaGetVersionResponse': 'OtaGetVersionResponse',
        'enos.message.upstream.ota.OtaVersionReportResponse': 'OtaVersionReportResponse',
        'enos.message.upstream.ota.OtaProgressReportResponse': 'OtaProgressReportResponse',
        'enos.message.downstream.ota.OtaUpgradeCommand': 'OtaUpgradeCommand',

        'enos.message.upstream.register.DeviceRegisterResponse': 'DeviceRegisterResponse',

        'enos.message.downstream.activate.DeviceActivateCommand': 'DeviceActivateCommand',

        'enos.message.downstream.tsl.MeasurepointGetCommand': 'MeasurepointGetCommand',
        'enos.message.downstream.tsl.MeasurepointSetCommand': 'MeasurepointSetCommand',
        'enos.message.downstream.tsl.ServiceInvocationCommand': 'ServiceInvocationCommand',
        'enos.message.downstream.tsl.ModelDownRawCommand': 'ModelDownRawCommand',

        'enos.message.downstream.device.SubDeviceDeleteCommand': 'SubDeviceDeleteCommand',
        'enos.message.downstream.device.SubDeviceEnableCommand': 'SubDeviceEnableCommand',
        'enos.message.downstream.device.SubDeviceDisableCommand': 'SubDeviceDisableCommand',

    }
    @classmethod
    def __import_decoder(cls):
        try:
            for package in cls.packages.items():
                model = __import__(package[0], fromlist=['mode'])
                if hasattr(model, package[1]):
                    clazz = getattr(model, package[1])
                    if hasattr(clazz(), 'decode'):
                        func = getattr(clazz(), 'decode')
                        cls.decoder_list.append(func)

        except Exception as e:
            raise EnvisionException(e)

    @classmethod
    def get_decoder_list(cls):
        if cls.decoder_list:
            return cls.decoder_list
        else:
            cls.__import_decoder()
            return cls.decoder_list

