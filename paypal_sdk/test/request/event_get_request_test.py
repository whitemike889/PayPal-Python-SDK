# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# event_get.py
# DO NOT EDIT
# @type request
# @json {"Name":"event.get","Description":"Shows details for a webhook event notification, by ID.","Parameters":[{"Type":"string","VariableName":"event_id","Description":"The ID of the webhook event notification for which to show details.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"SuccessResponseType":{"Type":"Event","VariableName":"","Description":"A webhook event notification.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"GET","Path":"/v1/notifications/webhooks-events/{event_id}","Visible":true}

import unittest

class EventGetRequestTest(unittest.TestCase):

    def testEventGetRequest(self):
        self.fail("Not implemented")

if __name__ == "__main__":
    unittest.main()
