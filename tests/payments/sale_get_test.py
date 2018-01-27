import unittest
import json

from tests.payments.payment_create_test import createPayment
from paypalrestsdk.payments import SaleGetRequest
from tests.testharness import TestHarness

class SaleGetTest(TestHarness):

    def testSaleGetRequestTest(self):
        payment_response = createPayment(self.client, "sale")
        saleId = payment_response.result.transactions[0].related_resources[0].sale.id

        request = SaleGetRequest(saleId)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
