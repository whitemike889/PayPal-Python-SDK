import unittest
import json

from paypalrestsdk.vault import CreditCardGetRequest
from tests.testharness import TestHarness
from tests.vault.credit_card_create_test import create_credit_card

class CreditCardGetTest(TestHarness):

    def testCreditCardGetTest(self):
        create_response = create_credit_card(self.client)
        self.assertEqual(201, create_response.status_code)

        get_request = CreditCardGetRequest(create_response.result.id)

        get_response = self.client.execute(get_request)
        self.assertEqual(200, get_response.status_code)
        self.assertIsNotNone(get_response.result)

        self.assertEqual(create_response.result.id, get_response.result.id)
        self.assertEqual(create_response.result.first_name, get_response.result.first_name)
        self.assertEqual(create_response.result.last_name, get_response.result.last_name)
        self.assertEqual(create_response.result.billing_address.city, get_response.result.billing_address.city)

if __name__ == "__main__":
    unittest.main()
