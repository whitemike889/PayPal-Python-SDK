# This class was generated on Wed, 07 Jun 2017 14:53:47 PDT by version 0.01 of Braintree SDK Generator
# simulate_event_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"simulate.event","Description":"Simulates a webhook event. Specify a sample payload.","Parameters":[],"RequestType":{"Type":"Simulate Event","VariableName":"body","Description":"Uses a sample payload to simulate a mock webhook event.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Event","VariableName":"","Description":"A webhook event notification.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/notifications/simulate-event","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import SimulateEventRequest
from paypal_sdk.test.testharness import TestHarness


class SimulateEventRequestTest(TestHarness):

    def testSimulateEventRequestTest(self):
        request = SimulateEventRequest()
        body = SimulateEvent()
        request.body(body)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
