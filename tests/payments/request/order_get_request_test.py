# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# order_get_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"order.get","Description":"Shows details for an order, by ID.","Parameters":[{"Type":"string","VariableName":"order_id","Description":"The ID of the order for which to show details.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Order","VariableName":"","Description":"An order transaction.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/payments/orders/{order_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from braintreehttp.http_exception import HttpException
from paypalrestsdk.payments.request.order_get_request import OrderGetRequest
from tests.testharness import TestHarness


FAKE_ID = "O-2FK09787H36911800"


class OrderGetRequestTest(TestHarness):

    def testOrderGetRequestTest_failsForNonexistentOrder(self):
        try:
            orderGetResponse = self.client.execute(OrderGetRequest(FAKE_ID))
            self.fail()
        except HttpException as he:
            # Fails with invalid resource ID, order does not exist
            self.assertTrue("INVALID_RESOURCE_ID" in he.message)


if __name__ == "__main__":
    unittest.main()
