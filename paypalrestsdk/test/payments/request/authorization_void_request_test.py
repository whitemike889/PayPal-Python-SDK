# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# authorization_void_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"authorization.void","Description":"Voids, or cancels, an authorization, by ID. You cannot void a fully captured authorization.","Parameters":[{"Type":"string","VariableName":"authorization_id","Description":"The ID of the authorization to void.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Authorization","VariableName":"","Description":"An authorization.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/authorization/{authorization_id}/void","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.payments.request import AuthorizationVoidRequest
from paypalrestsdk.test.testharness import TestHarness
from payment_create_request_test import createPayment


class AuthorizationVoidRequestTest(TestHarness):

    def testAuthorizationVoidRequestTest(self):
        payment_response = createPayment(self.client, "authorize")
        authId = payment_response.result.transactions[0].related_resources[0].authorization.id

        request = AuthorizationVoidRequest(authId)
        request.headers["Content-Type"] = "application/json"

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
