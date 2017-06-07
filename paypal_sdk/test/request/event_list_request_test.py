# This class was generated on Wed, 07 Jun 2017 14:53:47 PDT by version 0.01 of Braintree SDK Generator
# event_list_request_test.py
# DO NOT EDIT
# @type request-test
# @json {"Name":"event.list","Description":"Lists webhook event notifications. Use query parameters to filter the response.","Parameters":[{"Type":"string","VariableName":"end_time","Description":"Filters the webhook event notifications in the response to those created on or after the `start_time` and on or before this date and time. Both values are in [RFC 3339 Section 5.6](http://tools.ietf.org/html/rfc3339#section-5.6) format. Example: `end_time=2013-03-06T11:00:00Z`.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"event_type","Description":"Filters the response to a single event.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"integer","VariableName":"page_size","Description":"The number of webhook event notifications to return in the response.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"start_time","Description":"Filters the webhook event notifications in the response to those created on or after this date and time and on or before the `end_time` value. Both values are in [RFC 3339 Section 5.6](http://tools.ietf.org/html/rfc3339#section-5.6) format. Example: `start_time=2013-03-06T11:00:00Z`.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"transaction_id","Description":"Filters the response to a single transaction, by ID.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"}],"RequestType":null,"ResponseType":{"Type":"EventList","VariableName":"","Description":"List of webhooks events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks-events","Visible":true,"ExpectedStatusCode":200}



import unittest

from paypal_sdk.request import EventListRequest
from paypal_sdk.test.testharness import TestHarness


class EventListRequestTest(TestHarness):

    def testEventListRequestTest(self):
        request = EventListRequest()

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()
