# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_cancel_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.cancel","Description":"Cancels a sent invoice, by ID, and, optionally, sends a notification about the cancellation to the payer, merchant, and Cc: emails.","Parameters":[{"Type":"string","VariableName":"invoice_id","Description":"The ID of the invoice to cancel.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Cancel Notification","VariableName":"body","Description":"Cancels an email or SMS notification.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":null,"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/invoicing/invoices/{invoice_id}/cancel","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.invoices.request.test_util import sendInvoice

from paypalrestsdk.invoices.request import InvoiceCancelRequest
from tests.testharness import TestHarness


class InvoiceCancelRequestTest(TestHarness):

    def testInvoiceCancelRequestTest(self):
        invoice_response, id = sendInvoice(self.client)
        self.assertEqual(202, invoice_response.status_code)

        request = InvoiceCancelRequest(id)
        request.body({
            "subject": "Past Due",
            "note": "Nevermind!",
            "send_to_merchant": True,
            "send_to_payer": True,
        })

        response = self.client.execute(request)
        self.assertEqual(204, response.status_code)
        self.assertIsNone(response.result)

if __name__ == "__main__":
    unittest.main()
