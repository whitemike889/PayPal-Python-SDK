# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# authorization_get_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"authorization.get","Description":"Shows details for an authorization, by ID.","Parameters":[{"Type":"string","VariableName":"authorization_id","Description":"The ID of the authorization for which to show details.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Authorization","VariableName":"","Description":"An authorization.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/payments/authorization/{authorization_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}


import unittest

from paypalrestsdk.payments.request import AuthorizationGetRequest
from tests.payments.request.payment_create_request_test import createPayment
from tests.testharness import TestHarness


class AuthorizationGetRequestTest(TestHarness):

    def testAuthorizationGetRequestTest(self):
        payment_response = createPayment(self.client, "authorize")
        authId = payment_response.result.transactions[0].related_resources[0].authorization.id

        request = AuthorizationGetRequest(authId)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
