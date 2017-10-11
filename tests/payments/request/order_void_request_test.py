# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# order_void_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"order.void","Description":"Voids, or cancels, an order, by ID. You cannot void an order if the payment has already been partially or fully captured.","Parameters":[{"Type":"string","VariableName":"order_id","Description":"The ID of the order to void.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Order","VariableName":"","Description":"An order transaction.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/orders/{order_id}/do-void","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.payments.request.order_get_request_test import FAKE_ID

from braintreehttp.http_error import HttpError
from paypalrestsdk.payments.request import OrderVoidRequest
from tests.testharness import TestHarness

class OrderVoidRequestTest(TestHarness):

    def testOrderVoidRequestTest(self):

        request = OrderVoidRequest(FAKE_ID)

        try:
            self.client.execute(request)
            self.fail()
        except HttpError as he:
            self.assertTrue("debug_id" in he.message)

if __name__ == "__main__":
    unittest.main()
