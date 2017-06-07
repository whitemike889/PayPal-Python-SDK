# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# event_get_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"event.get","Description":"Shows details for a webhook event notification, by ID.","Parameters":[{"Type":"string","VariableName":"event_id","Description":"The ID of the webhook event notification for which to show details.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Event","VariableName":"","Description":"A webhook event notification.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks-events/{event_id}","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import EventGetRequest
from paypal_sdk.test.testharness import TestHarness


class EventGetRequestTest(TestHarness):

    def testEventGetRequestTest(self):
        request = EventGetRequest()

        response = self.client().execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
