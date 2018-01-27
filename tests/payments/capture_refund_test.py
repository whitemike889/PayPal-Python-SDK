import unittest
import json

from tests.payments.authorization_capture_test import createAuthorizationCapture
from paypalrestsdk.payments import CaptureRefundRequest
from tests.testharness import TestHarness

class CaptureRefundTest(TestHarness):

    def testCaptureRefundRequestTest(self):
        response = createAuthorizationCapture(self.client)

        request = CaptureRefundRequest(response.result.id)
        body = {
            "amount": {
                "total": "10",
                "currency": "USD"
            }
        }
        request.request_body(body)

        response = self.client.execute(request)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
