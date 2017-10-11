# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# order_capture_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"order.capture","Description":"Captures a payment for an order, by ID. To use this call, the original payment call must specify an `order` intent. In the JSON request body, include the payment amount and indicate whether this capture is the final capture for the authorization.","Parameters":[{"Type":"string","VariableName":"order_id","Description":"The ID of the order to capture.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Capture","VariableName":"body","Description":"A capture transaction.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Capture","VariableName":"","Description":"A capture transaction.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/orders/{order_id}/capture","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.payments.request.order_get_request_test import FAKE_ID

from braintreehttp.http_error import HttpError
from paypalrestsdk.payments.request import OrderCaptureRequest
from tests.testharness import TestHarness


class OrderCaptureRequestTest(TestHarness):

    def testOrderCaptureRequestTest(self):

        request = OrderCaptureRequest(FAKE_ID)
        request.requestBody({
            "amount": {
                "total":"10",
                "currency": "USD"
            },
            "is_final_capture": True,
        })

        try:
            self.client.execute(request)
            self.fail()
        except HttpError as he:
            # Fails with an internal service error, order does not exist
            self.assertTrue("debug_id" in he.message)

if __name__ == "__main__":
    unittest.main()
