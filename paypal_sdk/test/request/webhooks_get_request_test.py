# This class was generated on Wed, 07 Jun 2017 14:53:47 PDT by version 0.01 of Braintree SDK Generator
# webhooks_get_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"webhooks.get","Description":"Shows details for a webhook, by ID.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook for which to show details.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Webhook","VariableName":"","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks/{webhook_id}","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import WebhooksGetRequest
from paypal_sdk.test.testharness import TestHarness


class WebhooksGetRequestTest(TestHarness):

    def testWebhooksGetRequestTest(self):
        request = WebhooksGetRequest()

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
