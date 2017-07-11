# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_delete_external_refund_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.delete_external_refund","Description":"Deletes an external refund, by invoice ID and transaction ID.","Parameters":[{"Type":"string","VariableName":"invoice_id","Description":"The ID of the invoice from which to delete the refund transaction.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"},{"Type":"string","VariableName":"transaction_id","Description":"The ID of the refund transaction to delete.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":null,"ContentType":"application/json","HttpMethod":"DELETE","Path":"/v1/invoicing/invoices/{invoice_id}/refund-records/{transaction_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.invoices.request import InvoiceDeleteExternalRefundRequest
from paypalrestsdk.test.testharness import TestHarness
from test_util import createInvoiceRefund, getInvoice


class InvoiceDeleteExternalRefundRequestTest(TestHarness):

    def testInvoiceDeleteExternalRefundRequestTest(self):
        invoice_create_response, invoice_id = createInvoiceRefund(self.client)

        invoice_get_response = getInvoice(self.client, invoice_id)

        request = InvoiceDeleteExternalRefundRequest(invoice_id, invoice_get_response.result.refunds[0].transaction_id)

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)

if __name__ == "__main__":
    unittest.main()
