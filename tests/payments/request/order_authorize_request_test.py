# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# order_authorize_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"order.authorize","Description":"Authorizes an order, by ID. In the JSON request body, include an `amount` object.","Parameters":[{"Type":"string","VariableName":"order_id","Description":"The ID of the order to authorize.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Order","VariableName":"body","Description":"An order transaction.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Authorization","VariableName":"","Description":"An authorization.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/orders/{order_id}/authorize","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.payments.request.order_get_request_test import ID

from paypalrestsdk.payments.request import OrderAuthorizeRequest
from tests.testharness import TestHarness

class OrderAuthorizeRequestTest(TestHarness):

    def testOrderAuthorizeRequestTest(self):
        self.skipTest("Tests that use this class must be ignored when run in an automated environment because executing an order will require approval via the executed payment's approval_url")

        request = OrderAuthorizeRequest(ID)
        request.body({
            "amount": {
                "currency": "USD",
                "total": "10"
            }
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
