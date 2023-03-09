import unittest
from http import HTTPStatus

from infobip_platform.number.models.body.number_purchase import PurchaseNumberBody
from infobip_platform.number.models.core.number_purchase import NumberCapability
from infobip_platform.number.purchase import NumberStore


# @pytest.mark.skip(reason="credentials needed, server state dependent")
class NumbersTestCase(unittest.TestCase):
    channel = NumberStore.from_env()

    def test_get_available_numbers(self):
        response = NumbersTestCase.channel.get_available_numbers()

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.raw_response)

        numbers = response.numbers
        self.assertEqual(len(numbers), 50)

    def test_get_purchased_numbers(self):
        response = NumbersTestCase.channel.get_purchased_numbers()

        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIsNotNone(response.raw_response)

        numbers = response.numbers
        self.assertEqual(len(numbers), 3)
        self.assertEqual(numbers[0].type, "VIBER")
        self.assertEqual(numbers[1].type, "WHATSAPP")
        self.assertEqual(numbers[2].type, "VIRTUAL_LONG_NUMBER")
        self.assertEqual(numbers[0].capabilities, [NumberCapability.SMS])
        self.assertEqual(numbers[1].capabilities, [NumberCapability.SMS])
        self.assertEqual(numbers[2].capabilities, [NumberCapability.SMS])

    def test_get_single_purchased_number(self):
        number = NumbersTestCase.channel.get_single_purchased_number('3CA99AB3B566AFEC74FB98187BDE0B8F')

        self.assertEqual(HTTPStatus.OK, number.status_code)
        self.assertIsNotNone(number.raw_response)

        self.assertEqual(number.type, "VIRTUAL_LONG_NUMBER")
        self.assertEqual(number.capabilities, [NumberCapability.SMS])

    def test_purchase_number(self):
        number = NumbersTestCase.channel.purchase_number(
            PurchaseNumberBody(numberKey='7FDEF872FC0176A09A516BEF3A6928E0'))

        self.assertEqual(HTTPStatus.OK, number.status_code)
        self.assertIsNotNone(number.raw_response)

        self.assertEqual(number.type, "VIRTUAL_LONG_NUMBER")
        self.assertEqual(number.capabilities, [NumberCapability.SMS])

    def test_cancel_number(self):
        response = NumbersTestCase.channel.cancel_number("7FDEF872FC0176A09A516BEF3A6928E0")

        self.assertEqual(HTTPStatus.NO_CONTENT, response.status_code)
        self.assertIsNotNone(response.raw_response)
