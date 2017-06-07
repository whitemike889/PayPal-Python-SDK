# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# webhooks_delete_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"webhooks.delete","Description":"Deletes a webhook, by ID.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook to delete.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":null,"ContentType":"application/json","HttpMethod":"DELETE","Path":"/v1/notifications/webhooks/{webhook_id}","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import WebhooksDeleteRequest
from paypal_sdk.test.testharness import TestHarness


class WebhooksDeleteRequestTest(TestHarness):

    def testWebhooksDeleteRequestTest(self):
        request = WebhooksDeleteRequest()

        response = self.client().execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
