# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# refund_get_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"refund.get","Description":"Shows details for a refund, by ID.","Parameters":[{"Type":"string","VariableName":"refund_id","Description":"The ID of the refund for which to show details.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Refund","VariableName":"","Description":"A refund transaction.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/payments/refund/{refund_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.payments.request.sale_refund_request_test import createRefund

from paypalrestsdk.payments.request import RefundGetRequest
from tests.testharness import TestHarness

class RefundGetRequestTest(TestHarness):

    def testRefundGetRequestTest(self):
        refund_response = createRefund(self.client)

        request = RefundGetRequest(refund_response.result.id)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
