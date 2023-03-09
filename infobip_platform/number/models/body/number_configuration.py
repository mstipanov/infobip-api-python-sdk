from infobip_channels.core.models import MessageBodyBase
from infobip_platform.number.models.core.number_configuration import NumberConfiguration


class CreateNumberConfigurationBody(MessageBodyBase, NumberConfiguration):
    pass


class UpdateNumberConfigurationBody(MessageBodyBase, NumberConfiguration):
    pass
