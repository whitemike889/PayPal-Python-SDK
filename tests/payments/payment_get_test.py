import unittest
import json

from tests.payments.payment_create_test import createPayment
from paypalrestsdk.payments import PaymentGetRequest
from tests.testharness import TestHarness

class PaymentGetTest(TestHarness):

    def testPaymentGetRequestTest(self):
        response = createPayment(self.client, "sale")

        request = PaymentGetRequest(response.result.id)

        response = self.client.execute(request)

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()

