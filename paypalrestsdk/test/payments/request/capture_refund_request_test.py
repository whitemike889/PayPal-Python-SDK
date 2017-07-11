# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# capture_refund_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"capture.refund","Description":"Refunds a captured payment, by ID. In the JSON request body, include an `amount` object.","Parameters":[{"Type":"string","VariableName":"capture_id","Description":"The ID of the captured payment to refund.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Refund Request","VariableName":"body","Description":"A refund request.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Detailed Refund","VariableName":"","Description":"A refund transaction that is returned by `GET /refund`.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/capture/{capture_id}/refund","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.payments.request import CaptureRefundRequest
from paypalrestsdk.test.testharness import TestHarness
from authorization_capture_request_test import createAuthorizationCapture


class CaptureRefundRequestTest(TestHarness):

    def testCaptureRefundRequestTest(self):
        response = createAuthorizationCapture(self.client)

        request = CaptureRefundRequest(response.result.id)
        body = {
            "amount": {
                "total": "10",
                "currency": "USD"
            }
        }
        request.body(body)

        response = self.client.execute(request)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
