# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# webhook_subscribed_event_types_list_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"webhook.subscribed-event-types.list","Description":"Lists event subscriptions for a webhook, by ID.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook for which to list subscriptions.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"EventTypeList","VariableName":"","Description":"List of webhook events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks/{webhook_id}/event-types","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import WebhookSubscribedEventTypesListRequest
from paypal_sdk.test.testharness import TestHarness


class WebhookSubscribedEventTypesListRequestTest(TestHarness):

    def testWebhookSubscribedEventTypesListRequestTest(self):
        request = WebhookSubscribedEventTypesListRequest()

        response = self.client().execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
