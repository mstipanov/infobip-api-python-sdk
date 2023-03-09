from enum import Enum
from typing import Optional

from pydantic.types import constr

from infobip_channels.core.models import CamelCaseModel
from infobip_platform.number.models.core.number_purchase import NumberCapability


class PaginationQueryParameters(CamelCaseModel):
    limit: Optional[int] = None
    page: int = 0


class GetAvailableNumbersQueryParameters(PaginationQueryParameters):
    capabilities: list[NumberCapability] = []
    country: str = None
    npa: int = None
    nxx: int = None
    extras: list[str] = []
    number: str = None


class GetPurchasedNumbersQueryParameters(PaginationQueryParameters):
    number: Optional[str] = None
