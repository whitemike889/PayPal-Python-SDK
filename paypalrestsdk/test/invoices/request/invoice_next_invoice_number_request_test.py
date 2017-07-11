# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_next_invoice_number_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.next_invoice_number","Description":"Generates the next invoice number that is available to the merchant.","Parameters":[],"RequestType":null,"ResponseType":{"Type":"Invoice number","VariableName":"","Description":"","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/invoicing/invoices/next-invoice-number","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.invoices.request import InvoiceNextInvoiceNumberRequest
from paypalrestsdk.test.testharness import TestHarness


class InvoiceNextInvoiceNumberRequestTest(TestHarness):

    def testInvoiceNextInvoiceNumberRequestTest(self):
        request = InvoiceNextInvoiceNumberRequest()

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result.number)

if __name__ == "__main__":
    unittest.main()
