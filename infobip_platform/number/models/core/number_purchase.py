from enum import Enum
from typing import Optional

from pydantic.types import constr

from infobip_channels.core.models import CamelCaseModel


class EditPermissions(CamelCaseModel):
    canEditNumber: bool = None
    canEditConfiguration: bool = None


class Price(CamelCaseModel):
    setupPrice: Optional[float] = None
    pricePerMonth: Optional[float] = None
    currency: str = None


# TODO: I don't like this because nobody is updating the list and we keep adding new Channels
class NumberCapability(str, Enum):
    SMS = "SMS"
    VOICE = "VOICE"
    MMS = "MMS"
    WHATSAPP = "WHATSAPP"


class Number(CamelCaseModel):
    numberKey: str = None
    number: str = None
    type: str = None
    capabilities: list[NumberCapability] = None
    shared: bool = None
    keywords: list[str] = None
    additionalSetupRequired: bool = None
    editPermissions: EditPermissions = None
    applicationId: str = None
