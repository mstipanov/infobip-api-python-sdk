from infobip_channels.core.models import CamelCaseModel, MessageBodyBase


class PurchaseNumberBody(MessageBodyBase, CamelCaseModel):
    numberKey: str = None
    number: str = None
    applicationId: str = None
    entityId: str = None
