# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_remind_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.remind","Description":"Sends a reminder to the payer about an invoice, by ID. In the JSON request body, include a `notification` object that defines the subject of the reminder and other details.","Parameters":[{"Type":"string","VariableName":"invoice_id","Description":"The ID of the invoice for which to send a reminder.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Notification","VariableName":"body","Description":"The email or SMS notification.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":null,"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/invoicing/invoices/{invoice_id}/remind","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.invoices.request.test_util import sendInvoice

from paypalrestsdk.invoices.request import InvoiceRemindRequest
from tests.testharness import TestHarness


class InvoiceRemindRequestTest(TestHarness):

    def testInvoiceRemindRequestTest(self):
        invoice_response, id = sendInvoice(self.client)
        self.assertEqual(202, invoice_response.status_code)

        request = InvoiceRemindRequest(id)
        request.body({
            "subject": "Past due",
            "note": "Please pay soon",
            "send_to_merchant": True
        })

        response = self.client.execute(request)
        self.assertEqual(202, response.status_code)
        self.assertIsNone(response.result)

if __name__ == "__main__":
    unittest.main()
