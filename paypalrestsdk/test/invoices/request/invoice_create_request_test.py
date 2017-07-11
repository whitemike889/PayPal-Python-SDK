# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_create_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.create","Description":"Creates a draft invoice. You can optionally create an invoice [template](/docs/api/invoicing/#templates). Then, when you create an invoice from a template, the invoice is populated with the predefined data that the source template contains. To move the invoice from a draft to payable state, you must [send the invoice](/docs/api/invoicing/#invoices_send). In the JSON request body, include invoice details including merchant information. The `invoice` object must include an `items` array.\u003cblockquote\u003e\u003cstrong\u003eNote:\u003c/strong\u003e The merchant specified in an invoice must have a PayPal account in good standing.\u003c/blockquote\u003e","Parameters":[],"RequestType":{"Type":"Invoice","VariableName":"body","Description":"Invoice details.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Invoice","VariableName":"","Description":"Invoice details.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/invoicing/invoices","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.test.testharness import TestHarness
from test_util import createInvoice


class InvoiceCreateRequestTest(TestHarness):
    def testInvoiceCreateRequestTest(self):
        response = createInvoice(self.client)
        self.assertEqual(201, response.status_code)
        self.assertIsNotNone(response.result)


if __name__ == "__main__":
    unittest.main()
