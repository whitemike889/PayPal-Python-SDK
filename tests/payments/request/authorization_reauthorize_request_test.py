# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# authorization_reauthorize_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"authorization.reauthorize","Description":"Re-authorizes a PayPal account payment, by authorization ID. To ensure that funds are still available, re-authorize a payment after the initial three-day honor period. Supports only the `amount` request parameter. You can re-authorize a payment only once from four to 29 days after three-day honor period for the original authorization expires. If 30 days have passed from the original authorization, you must create a new authorization instead. A re-authorized payment itself has a new three-day honor period. You can re-authorize a transaction once for up to 115% of the originally authorized amount, not to exceed an increase of $75 USD.","Parameters":[{"Type":"string","VariableName":"authorization_id","Description":"The ID of the authorization to re-authorize.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Authorization","VariableName":"body","Description":"An authorization.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Authorization","VariableName":"","Description":"An authorization.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/authorization/{authorization_id}/reauthorize","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.payments.request import AuthorizationReauthorizeRequest
from tests.payments.request.payment_create_request_test import createPayment
from tests.testharness import TestHarness


class AuthorizationReauthorizeRequestTest(TestHarness):

    def testAuthorizationReauthorizeRequestTest(self):
        payment_response = createPayment(self.client, "authorize")
        authId = payment_response.result.transactions[0].related_resources[0].authorization.id

        request = AuthorizationReauthorizeRequest(authId)

        body = {
            "amount": {
                "total": "10",
                "currency": "USD"
            }
        }
        request.body(body)

        try:
            response = self.client.execute(request)
        except IOError as ioe:
            self.assertTrue("DCC_REAUTHORIZATION_NOT_ALLOWED" in ioe.message)

if __name__ == "__main__":
    unittest.main()
