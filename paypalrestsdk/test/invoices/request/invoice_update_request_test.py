# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_update_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.update","Description":"Fully updates an invoice, by ID. In the JSON request body, include a complete `invoice` object. This call does not support partial updates.","Parameters":[{"Type":"string","VariableName":"invoice_id","Description":"The ID of the invoice to update.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"},{"Type":"boolean","VariableName":"notify_merchant","Description":"Indicates whether to send the invoice update notification to the merchant. Default is `true`.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null,"Location":"query"}],"RequestType":{"Type":"Invoice","VariableName":"body","Description":"Invoice details.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Invoice","VariableName":"","Description":"Invoice details.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"PUT","Path":"/v1/invoicing/invoices/{invoice_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.invoices.request import InvoiceUpdateRequest
from paypalrestsdk.test.testharness import TestHarness
from test_util import createInvoice


class InvoiceUpdateRequestTest(TestHarness):

    def testInvoiceUpdateRequestTest(self):
        response = createInvoice(self.client)

        request = InvoiceUpdateRequest(response.result.id)
        request.notifyMerchant(True)

        request.body({
            "merchant_info": {
                "email": "stevendcoffey-facilitator@gmail.com"
            },
            "terms": "Upon receipt of this invoice, Steve owes Sasha a soda."
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

if __name__ == "__main__":
    unittest.main()
