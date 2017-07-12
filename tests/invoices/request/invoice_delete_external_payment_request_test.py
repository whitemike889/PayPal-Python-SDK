# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_delete_external_payment_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.delete_external_payment","Description":"Deletes an external payment, by invoice ID and transaction ID.","Parameters":[{"Type":"string","VariableName":"invoice_id","Description":"The ID of the invoice from which to delete a payment transaction.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"},{"Type":"string","VariableName":"transaction_id","Description":"The ID of the payment transaction to delete.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":null,"ContentType":"application/json","HttpMethod":"DELETE","Path":"/v1/invoicing/invoices/{invoice_id}/payment-records/{transaction_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.invoices.request.test_util import createInvoicePayment, getInvoice

from paypalrestsdk.invoices.request import InvoiceDeleteExternalPaymentRequest
from tests.testharness import TestHarness


class InvoiceDeleteExternalPaymentRequestTest(TestHarness):

    def testInvoiceDeleteExternalPaymentRequestTest(self):
        invoice_payment_response, invoice_id = createInvoicePayment(self.client)

        invoice_get_response = getInvoice(self.client, invoice_id)
        request = InvoiceDeleteExternalPaymentRequest(invoice_id, invoice_get_response.result.payments[0].transaction_id)

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

if __name__ == "__main__":
    unittest.main()
