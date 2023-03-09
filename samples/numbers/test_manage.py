import unittest
from http import HTTPStatus

from infobip_platform.number.manage import NumberManagement
from infobip_platform.number.models.body.number_configuration import CreateNumberConfigurationBody
from infobip_platform.number.models.core.number_configuration import Action, ActionType


# @pytest.mark.skip(reason="credentials needed, server state dependent")
class NumbersTestCase(unittest.TestCase):
    channel = NumberManagement.from_env()

    def find_by_number_key_and_keyword(number_key: str, keyword: str):
        response = NumbersTestCase.channel.get_number_configurations(number_key)
        for configuration in response.configurations:
            if configuration.keyword == keyword:
                return configuration
        return None

    def test_get_number_configurations(self):
        number_key = '3CA99AB3B566AFEC74FB98187BDE0B8F'
        response = NumbersTestCase.channel.get_number_configurations(number_key)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.raw_response)
        self.assertIsNotNone(response.configurations)

    def test_get_single_number_configuration(self):
        number_key = '3CA99AB3B566AFEC74FB98187BDE0B8F'
        configuration_key = '4C1F7CBA3C34FE691DA93E847247267C'
        number = NumbersTestCase.channel.get_single_number_configuration(number_key, configuration_key)
        self.assertEqual(HTTPStatus.OK, number.status_code)
        self.assertIsNotNone(number.raw_response)
        self.assertIsNotNone(number.key)

    def test_create_number_configuration(self):
        number_key = '3CA99AB3B566AFEC74FB98187BDE0B8F'
        number = CreateNumberConfigurationBody(keyword="MSTIPANOV2023_2", action=Action(type=ActionType.PULL))
        response = NumbersTestCase.channel.create_number_configuration(number_key, number)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.raw_response)
        self.assertIsNotNone(response.key)

    def test_update_number_configuration(self):
        number_key = '3CA99AB3B566AFEC74FB98187BDE0B8F'
        configuration = NumbersTestCase.channel.get_number_configurations(number_key).configurations[0]

        response = NumbersTestCase.channel.update_number_configuration(number_key, configuration)
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.raw_response)

    def test_delete_number_configuration(self):
        number_key = '3CA99AB3B566AFEC74FB98187BDE0B8F'
        configuration = NumbersTestCase.find_by_number_key_and_keyword(number_key, "MSTIPANOV2023_2")
        configuration_key = configuration.key
        response = NumbersTestCase.channel.delete_number_configuration(number_key, configuration_key)
        self.assertEqual(HTTPStatus.NO_CONTENT, response.status_code)
        self.assertIsNotNone(response.raw_response)
