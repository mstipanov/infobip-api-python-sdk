from typing import List

from infobip_channels.core.models import ResponseBase
from infobip_platform.number.models.core.number_purchase import Number


class GetPurchasedNumbersResponse(ResponseBase):
    numbers: List[Number]
    numberCount: int


class GetPurchasedNumberResponse(ResponseBase, Number):
    pass
