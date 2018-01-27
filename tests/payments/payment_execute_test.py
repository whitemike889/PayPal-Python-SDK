import unittest
import json

from tests.payments.payment_create_test import createPayment
from braintreehttp.http_error import HttpError
from paypalrestsdk.payments import PaymentExecuteRequest
from tests.testharness import TestHarness

class PaymentExecuteTest(TestHarness):

    def testPaymentExecuteRequestTest(self):

        response = createPayment(self.client, "order", payment_method="paypal")

        request = PaymentExecuteRequest(response.result.id)
        request.request_body({
            "payer_id": "some_payer_id"
        })

        try:
            response = self.client.execute(request)
            self.fail()
        except HttpError as he:
            self.assertTrue("PAYMENT_NOT_APPROVED_FOR_EXECUTION" in he.message)

if __name__ == "__main__":
    unittest.main()

