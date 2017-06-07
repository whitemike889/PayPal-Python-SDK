# This class was generated on Wed, 07 Jun 2017 14:53:47 PDT by version 0.01 of Braintree SDK Generator
# verify_webhook_signature_post_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"verify.webhook.signature.post","Description":"Verifies a webhook signature.","Parameters":[],"RequestType":{"Type":"Verify Webhook Signature","VariableName":"body","Description":"Verify the webhook signature.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Verify Webhook Signature Response","VariableName":"","Description":"The verify webhook signature response.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/notifications/verify-webhook-signature","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import VerifyWebhookSignaturePostRequest
from paypal_sdk.test.testharness import TestHarness


class VerifyWebhookSignaturePostRequestTest(TestHarness):

    def testVerifyWebhookSignaturePostRequestTest(self):
        request = VerifyWebhookSignaturePostRequest()
        body = VerifyWebhookSignature()
        request.body(body)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
