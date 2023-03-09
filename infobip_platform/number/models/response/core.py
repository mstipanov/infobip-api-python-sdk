from infobip_channels.core.models import CamelCaseModel, ResponseBase
from infobip_channels.sms.models.response.core import RequestError


class PlatformResponseError(ResponseBase):
    request_error: RequestError
