from http import HTTPStatus
from typing import Any, Type, Union

import requests
from requests import Response

from infobip_channels.core.channel import Channel
from infobip_channels.core.models import ResponseBase
from infobip_platform.number.models.body.number_configuration import (CreateNumberConfigurationBody,
                                                                      UpdateNumberConfigurationBody)
from infobip_platform.number.models.response.core import PlatformResponseError
from infobip_platform.number.models.response.responses import (GetNumberConfigurationsResponse,
                                                               NumberConfigurationResponse)




class NumberManagement(Channel):
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

    def get_number_configurations(self, number_key: str) -> Union[ResponseBase, Any]:
        """Get a paginated list of number configurations.
        https://www.infobip.com/docs/api/platform/numbers/my-numbers/number-management/list-configurations-for-number

        :return Response with a list of NumberConfiguration objects.
        """
        response = self._client.get(self.NUMBERS_PATH_VERSION_2 + f"numbers/{number_key}/sms")
        return self._construct_response(response, GetNumberConfigurationsResponse)

    def get_single_number_configuration(self, number_key: str, configuration_key: str) -> Union[ResponseBase, Any]:
        """This method fetches a single configuration details set up for the number.
        https://www.infobip.com/docs/api/platform/numbers/my-numbers/number-management/get-single-configuration

        :return Response with a single NumberConfiguration object.
        """
        response = self._client.get(self.NUMBERS_PATH_VERSION_2 + f"numbers/{number_key}/sms/{configuration_key}")
        return self._construct_response(response, NumberConfigurationResponse)

    def create_number_configuration(self, number_key: str, number_configuration: CreateNumberConfigurationBody) -> \
    Union[ResponseBase, Any]:
        """Get a paginated list of entities.

        :return Response with a list of Entity objects.
        """
        response = self._client.post(self.NUMBERS_PATH_VERSION_2 + f"numbers/{number_key}/sms",
                                    number_configuration.dict(by_alias=False))
        return self._construct_response(response, NumberConfigurationResponse)

    def update_number_configuration(self, number_key: str, number_configuration: UpdateNumberConfigurationBody) -> \
    Union[ResponseBase, Any]:
        """Get a paginated list of entities.

        :return Response with a list of Entity objects.
        """
        response = self._client.put(self.NUMBERS_PATH_VERSION_2 + f"numbers/{number_key}/sms",
                                    number_configuration.dict(by_alias=False))
        return self._construct_response(response, NumberConfigurationResponse)

    def delete_number_configuration(self, number_key: str, configuration_key: str) -> \
    Union[ResponseBase, Any]:
        """This method will delete the configuration. If there are no configurations, you can still retrieve any incoming message by using a Get received messages method.

        :return Http response.
        """
        response = self._client.delete(self.NUMBERS_PATH_VERSION_2 + f"numbers/{number_key}/sms/{configuration_key}")
        return self._construct_response(response, ResponseBase)
