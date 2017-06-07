# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# available_event_type_list_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"available-event-type.list","Description":"Lists available events to which any webhook can subscribe. For a list of supported events, see [Webhook event names](/docs/integration/direct/webhooks/event-names/).","Parameters":[],"RequestType":null,"ResponseType":{"Type":"EventTypeList","VariableName":"","Description":"List of webhook events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks-event-types","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import AvailableEventTypeListRequest
from paypal_sdk.test.testharness import TestHarness


class AvailableEventTypeListRequestTest(TestHarness):

    def testAvailableEventTypeListRequestTest(self):
        request = AvailableEventTypeListRequest()

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
