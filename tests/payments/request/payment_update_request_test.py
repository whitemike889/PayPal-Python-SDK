# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# payment_update_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"payment.update","Description":"Partially updates a payment, by ID. You can update the amount, shipping address, invoice ID, and custom data. You cannot update a payment after the payment executes.","Parameters":[{"Type":"string","VariableName":"payment_id","Description":"The ID of the payment to update.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"JSON Patch","VariableName":"body","Description":"A JSON patch request.","IsArray":true,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":null,"ContentType":"application/json","HttpMethod":"PATCH","Path":"/v1/payments/payment/{payment_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.payments.request.payment_create_request_test import createPayment

from paypalrestsdk.payments.request import PaymentUpdateRequest
from tests.testharness import TestHarness


class PaymentUpdateRequestTest(TestHarness):

    def testPaymentUpdateRequestTest(self):
        payment_response = createPayment(self.client, "sale", payment_method="paypal")

        request = PaymentUpdateRequest(payment_response.result.id)
        request.requestBody([{
            "path": "/transactions/0/amount",
            "op": "replace",
            "value": {
                "currency": "USD",
                "total": "11"
            }
        }])

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
