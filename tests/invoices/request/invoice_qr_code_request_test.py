# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_qr_code_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.qr_code","Description":"Generates a QR code for an invoice, by ID.\u003cbr/\u003e\u003cbr/\u003eThe QR code is a PNG image in [Base64-encoded](https://www.base64encode.org/) format that corresponds to the invoice ID. You can generate a QR code for an invoice and add it to a paper or PDF invoice. When a customer uses their mobile device to scan the QR code, he or she is redirected to the PayPal mobile payment flow where he or she can pay online with PayPal or a credit card.\u003cbr/\u003e\u003cbr/\u003eBefore you get a QR code, you must:\u003col\u003e\u003cli\u003e\u003cp\u003e[Create an invoice](#invoices_create). Specify `qrinvoice@paypal.com` as the recipient email address in the `billing_info` object. Use a customer email address only if you want to email the invoice.\u003c/p\u003e\u003c/li\u003e\u003cli\u003e\u003cp\u003e[Send an invoice](#invoices_send) to move the invoice from a draft to payable state. If you specify `qrinvoice@paypal.com` as the recipient email address, the invoice is not emailed.\u003c/p\u003e\u003c/li\u003e\u003c/ol\u003e","Parameters":[{"Type":"string","VariableName":"action","Description":"The type of URL for which to generate a QR code. Default is `pay` and is the only supported value.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"integer","VariableName":"height","Description":"The height, in pixels, of the QR code image. Valid value is from 150 to 500. Default is 500.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"invoice_id","Description":"The ID of the invoice for which to generate a QR code.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"},{"Type":"integer","VariableName":"width","Description":"The width, in pixels, of the QR code image. Valid value is from 150 to 500. Default is 500.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null,"Location":"query"}],"RequestType":null,"ResponseType":{"Type":"QR Code","VariableName":"","Description":"base64 encoded image of type image/png","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/invoicing/invoices/{invoice_id}/qr-code","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.invoices.request.test_util import createInvoice

from paypalrestsdk.invoices.request import InvoiceQrCodeRequest
from tests.testharness import TestHarness


class InvoiceQrCodeRequestTest(TestHarness):

    def testInvoiceQrCodeRequestTest(self):
        invoice_response = createInvoice(self.client)

        request = InvoiceQrCodeRequest(invoice_response.result.id) \
            .height(500) \
            .width(500)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result.image)

if __name__ == "__main__":
    unittest.main()
