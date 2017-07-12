# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_record_payment_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.record-payment","Description":"Marks the status of an invoice, by ID, as paid. Include a payment detail object that defines the payment method and other details in the JSON request body.","Parameters":[{"Type":"string","VariableName":"invoice_id","Description":"The ID of the invoice to mark as paid.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Payment Detail","VariableName":"body","Description":"Payment details.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":null,"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/invoicing/invoices/{invoice_id}/record-payment","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.invoices.request.test_util import createInvoicePayment

from tests.testharness import TestHarness


class InvoiceRecordPaymentRequestTest(TestHarness):

    def testInvoiceRecordPaymentRequestTest(self):
        response, invoice_id = createInvoicePayment(self.client)
        self.assertEqual(204, response.status_code)
        self.assertIsNone(response.result)

if __name__ == "__main__":
    unittest.main()
