import unittest
import json

from tests.payments.order_get_test import FAKE_ID
from braintreehttp.http_error import HttpError
from paypalrestsdk.payments import OrderAuthorizeRequest
from tests.testharness import TestHarness

class OrderAuthorizeTest(TestHarness):

    def testOrderAuthorizeRequestTest(self):
        request = OrderAuthorizeRequest(FAKE_ID)
        request.request_body({
            "amount": {
                "currency": "USD",
                "total": "10"
            }
        })

        try:
            self.client.execute(request)
            self.fail()
        except HttpError as he:
            # Fails with an internal service error, order does not exist
            self.assertTrue("debug_id" in he.message)

if __name__ == "__main__":
    unittest.main()
