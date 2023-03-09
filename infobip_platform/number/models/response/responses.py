from typing import List

from infobip_channels.core.models import ResponseBase
from infobip_platform.number.models.core.number_configuration import NumberConfiguration


class GetNumberConfigurationsResponse(ResponseBase):
    configurations: List[NumberConfiguration]
    totalCount: int


class NumberConfigurationResponse(ResponseBase, NumberConfiguration):
    pass