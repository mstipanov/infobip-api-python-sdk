from enum import Enum
from typing import Optional

from pydantic.types import constr

from infobip_channels.core.models import CamelCaseModel


class HttpMethod(str, Enum):
    GET = "GET"
    POST = "POST"


class ContentType(str, Enum):
    JSON = "JSON"
    XML = "XML"


class ActionType(str, Enum):
    PULL = "PULL"
    HTTP_FORWARD = "HTTP_FORWARD"
    SMPP_FORWARD = "SMPP_FORWARD"
    MAIL_FORWARD = "MAIL_FORWARD"
    NO_ACTION = "NO_ACTION"


class Action(CamelCaseModel):
    type: ActionType = None
    description: Optional[str] = None
    url: str = None
    httpMethod: HttpMethod = None
    contentType: ContentType = None


class UseConversation(CamelCaseModel):
    enabled: bool = None


class NumberConfiguration(CamelCaseModel):
    key: str = None
    keyword: Optional[constr(max_length=50)] = None
    action: Action = None
    useConversation: UseConversation = None
    applicationId: Optional[constr(max_length=255)] = None
    entityId: Optional[constr(max_length=255)] = None


