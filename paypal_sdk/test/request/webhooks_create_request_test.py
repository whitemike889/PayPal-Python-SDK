# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# webhooks_create_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"webhooks.create","Description":"Subscribes your webhook listener to events. A successful call returns a [`webhook`](/docs/api/webhooks/#definition-webhook:v1) object, which includes the webhook ID for later use.","Parameters":[],"RequestType":{"Type":"Webhook","VariableName":"body","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Webhook","VariableName":"","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/notifications/webhooks","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import WebhooksCreateRequest
from paypal_sdk.test.testharness import TestHarness


class WebhooksCreateRequestTest(TestHarness):

    def testWebhooksCreateRequestTest(self):
        request = WebhooksCreateRequest()
        body = Webhook()
        request.body(body)

        response = self.client().execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
