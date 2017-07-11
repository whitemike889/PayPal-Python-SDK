# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# authorization_capture_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"authorization.capture","Description":"Captures and processes an authorization, by ID. To use this call, the original payment call must specify an intent of `authorize`.","Parameters":[{"Type":"string","VariableName":"authorization_id","Description":"The ID of the authorization to capture.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Capture","VariableName":"body","Description":"A capture transaction.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Capture","VariableName":"","Description":"A capture transaction.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/authorization/{authorization_id}/capture","ExpectedStatusCode":200,"FileSuffix":"Test"}

import unittest

from paypalrestsdk.payments.request import AuthorizationCaptureRequest
from paypalrestsdk.test.testharness import TestHarness
from payment_create_request_test import createPayment


def createAuthorizationCapture(client):
    response = createPayment(client, "authorize")
    authId = response.result.transactions[0].related_resources[0].authorization.id

    capture = {
        "amount": {
            "total": "10",
            "currency": "USD"
        },
        "is_final_capture": True
    }

    request = AuthorizationCaptureRequest(authId)
    request.body(capture)

    return client.execute(request)


class AuthorizationCaptureRequestTest(TestHarness):

    def testAuthorizationCaptureRequestTest(self):
        response = createAuthorizationCapture(self.client)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()