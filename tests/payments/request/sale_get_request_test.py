# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# sale_get_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"sale.get","Description":"Shows details for a sale, by ID. Returns only sales that were created through the REST API.","Parameters":[{"Type":"string","VariableName":"sale_id","Description":"The ID of the sale for which to show details.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Sale","VariableName":"","Description":"A sale transaction. Returned as a part of payment-related resources.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/payments/sale/{sale_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.payments.request.payment_create_request_test import createPayment

from paypalrestsdk.payments.request import SaleGetRequest
from tests.testharness import TestHarness


class SaleGetRequestTest(TestHarness):

    def testSaleGetRequestTest(self):
        payment_response = createPayment(self.client, "sale")
        saleId = payment_response.result.transactions[0].related_resources[0].sale.id

        request = SaleGetRequest(saleId)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
