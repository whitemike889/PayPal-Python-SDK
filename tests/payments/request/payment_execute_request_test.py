# This class was generated on Thu, 06 Jul 2017 16:03:30 PDT by version 0.01 of Braintree SDK Generator
# payment_execute_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"payment.execute","Description":"Executes a PayPal payment that the customer has approved. You can optionally update one or more transactions when you execute the payment.\u003cblockquote\u003e\u003cstrong\u003eImportant:\u003c/strong\u003e This call works only after a customer has approved the payment. For more information, learn about [PayPal payments](/docs/integration/direct/payments/paypal-payments/).\u003c/blockquote\u003e","Parameters":[{"Type":"string","VariableName":"payment_id","Description":"The ID of the payment to execute.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Payment Execution","VariableName":"body","Description":"Executes a PayPal account-based payment with the `payer_id` obtained from the web approval URL.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Payment","VariableName":"","Description":"A payment. Use this object to create, process, and manage payments.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/payment/{payment_id}/execute","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.payments.request.payment_create_request_test import createPayment

from braintreehttp.http_exception import HttpException
from paypalrestsdk.payments.request import PaymentExecuteRequest
from tests.testharness import TestHarness

class PaymentExecuteRequestTest(TestHarness):

    def testPaymentExecuteRequestTest(self):

        response = createPayment(self.client, "order", payment_method="paypal")

        request = PaymentExecuteRequest(response.result.id)
        request.requestBody({
            "payer_id": "some_payer_id"
        })

        try:
            response = self.client.execute(request)
            self.fail()
        except HttpException as he:
            self.assertTrue("PAYMENT_NOT_APPROVED_FOR_EXECUTION" in he.message)

if __name__ == "__main__":
    unittest.main()
