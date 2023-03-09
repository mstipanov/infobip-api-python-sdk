from http import HTTPStatus
from typing import Any, Dict, Type, Union

import requests

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import ResponseBase
from infobip_platform.number.models.body.number_purchase import PurchaseNumberBody
from infobip_platform.number.models.query_parameters.number_purchase import (GetPurchasedNumbersQueryParameters,
                                                                             GetAvailableNumbersQueryParameters)
from infobip_platform.number.models.response.core import PlatformResponseError
from infobip_platform.number.models.response.get_numbers import GetPurchasedNumbersResponse, GetPurchasedNumberResponse


class NumberStore(Channel):
    """Class used for interaction with the Infobip Application and Entity Management API."""

    NUMBERS_PATH_VERSION_1 = "/numbers/1/"
    NUMBERS_PATH_VERSION_2 = "/numbers/2/"

    def _get_custom_response_class(
            self,
            raw_response: Union[requests.Response, Any],
            response_class: Type[ResponseBase],
            *args,
            **kwargs,
    ) -> Type[ResponseBase]:
        if raw_response.status_code in (HTTPStatus.OK, HTTPStatus.NO_CONTENT):
            return response_class
        elif raw_response.status_code in (
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.UNAUTHORIZED,
                HTTPStatus.FORBIDDEN,
                HTTPStatus.TOO_MANY_REQUESTS,
                HTTPStatus.INTERNAL_SERVER_ERROR,
                HTTPStatus.NOT_FOUND,
        ):
            return PlatformResponseError

        raise ValueError

    def get_available_numbers(self, query_parameters: Union[GetAvailableNumbersQueryParameters, Dict] = None) -> Union[
        ResponseBase, Any]:
        """When you're looking for a new number, this method will return all available numbers filtered by the specified
        parameters.
        https://www.infobip.com/docs/api/platform/numbers/phone-numbers/get-available-numbers

        :param query_parameters: Query parameters to send with the request
        :return Response with a list of Number objects.
        """

        query_parameters = self.validate_query_parameter(
            query_parameters or {}, GetPurchasedNumbersQueryParameters
        )

        response = self._client.get(self.NUMBERS_PATH_VERSION_1 + "numbers/available",
                                    params=query_parameters.dict(by_alias=True))
        return self._construct_response(response, GetPurchasedNumbersResponse)

    def get_purchased_numbers(self, query_parameters: Union[GetPurchasedNumbersQueryParameters, Dict] = None) -> Union[
        ResponseBase, Any]:
        """Use this method to get all the numbers purchased for the account.
        https://www.infobip.com/docs/api/platform/numbers/phone-numbers/list-purchased-numbers

        :param query_parameters: Query parameters to send with the request
        :return Response with a list of Number objects.
        """

        query_parameters = self.validate_query_parameter(
            query_parameters or {}, GetPurchasedNumbersQueryParameters
        )

        response = self._client.get(self.NUMBERS_PATH_VERSION_1 + "numbers",
                                    params=query_parameters.dict(by_alias=True))
        return self._construct_response(response, GetPurchasedNumbersResponse)

    def get_single_purchased_number(self, number_key: str) -> Union[ResponseBase, Any]:
        """Get information about a single purchased number by the number key.
        https://www.infobip.com/docs/api/platform/numbers/phone-numbers/get-single-purchased-number

        :param number_key: The unique ID of the number for which information is requested.
        :return Response with a Number object if it exists.
        """

        response = self._client.get(self.NUMBERS_PATH_VERSION_1 + f"numbers/{number_key}")
        return self._construct_response(response, GetPurchasedNumberResponse)

    def purchase_number(self, number: PurchaseNumberBody) -> Union[ResponseBase, Any]:
        """Using the number ID or number, this method enables you to buy a new number. For buying a US number, only the number should be provided. For all other purchases, only the numberKey must be provided.
        https://www.infobip.com/docs/api/platform/numbers/phone-numbers/purchase-number

        :param number: Number object.
        :return Response with a Number object if it exists.
        """

        response = self._client.post(self.NUMBERS_PATH_VERSION_1 + "numbers", number.dict(by_alias=False))
        return self._construct_response(response, GetPurchasedNumberResponse)

    def cancel_number(self, number_key: str) -> Union[ResponseBase, Any]:
        """This method will cancel your purchased number. The number you cancel will become available in the numbers pool for anyone to buy.
        https://www.infobip.com/docs/api/platform/numbers/phone-numbers/cancel-number

        :param number_key: Unique ID of a number.
        :return Http response.
        """

        response = self._client.delete(self.NUMBERS_PATH_VERSION_1 + f"numbers/{number_key}")
        return self._construct_response(response, ResponseBase)
