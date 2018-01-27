import unittest
import json

from paypalrestsdk.payments import AuthorizationVoidRequest
from tests.payments.payment_create_test import createPayment
from tests.testharness import TestHarness

class AuthorizationVoidTest(TestHarness):

    def testAuthorizationVoidRequestTest(self):
        payment_response = createPayment(self.client, "authorize")
        authId = payment_response.result.transactions[0].related_resources[0].authorization.id

        request = AuthorizationVoidRequest(authId)
        request.headers["Content-Type"] = "application/json"

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
