# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_get_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.get","Description":"Shows details for an invoice, by ID.","Parameters":[{"Type":"string","VariableName":"invoice_id","Description":"The ID of the invoice for which to show details.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Invoice","VariableName":"","Description":"Invoice details.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/invoicing/invoices/{invoice_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.test.testharness import TestHarness
from test_util import createInvoice, getInvoice


class InvoiceGetRequestTest(TestHarness):
    def testInvoiceGetRequestTest(self):
        invoice_response = createInvoice(self.client)

        response = getInvoice(self.client, invoice_response.result.id)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)


if __name__ == "__main__":
    unittest.main()
