# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# sale_refund_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"sale.refund","Description":"Refunds a sale, by ID. For a full refund, include an empty payload in the JSON request body. For a partial refund, include an `amount` object in the JSON request body.","Parameters":[{"Type":"string","VariableName":"sale_id","Description":"The ID of the sale transaction to refund.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Refund Request","VariableName":"body","Description":"A refund request.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Detailed Refund","VariableName":"","Description":"A refund transaction that is returned by `GET /refund`.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/sale/{sale_id}/refund","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.payments.request import SaleRefundRequest
from paypalrestsdk.test.testharness import TestHarness
from payment_create_request_test import createPayment


def createRefund(client):
    response = createPayment(client, "sale")

    saleId = response.result.transactions[0].related_resources[0].sale.id
    request = SaleRefundRequest(saleId)
    request.body({})

    return client.execute(request)


class SaleRefundRequestTest(TestHarness):

    def testSaleRefundRequestTest(self):
        response = createRefund(self.client)
        self.assertEqual(201, response.status_code)

if __name__ == "__main__":
    unittest.main()
