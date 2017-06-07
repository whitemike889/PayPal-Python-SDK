# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# webhooks_get_all_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"webhooks.get-all","Description":"Lists all webhooks for an app.","Parameters":[{"Type":"string","VariableName":"anchor_type","Description":"Filters the response by an entity type, `anchor_id`. Value is `APPLICATION` or `ACCOUNT`. Default is `APPLICATION`.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"}],"RequestType":null,"ResponseType":{"Type":"WebhookList","VariableName":"","Description":"List of webhooks.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import WebhooksGetAllRequest
from paypal_sdk.test.testharness import TestHarness


class WebhooksGetAllRequestTest(TestHarness):

    def testWebhooksGetAllRequestTest(self):
        request = WebhooksGetAllRequest()

        response = self.client().execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
