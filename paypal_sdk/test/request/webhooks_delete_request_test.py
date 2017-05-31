# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# webhooks_delete.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhooks.delete","Description":"Deletes a webhook, by ID.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook to delete.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"SuccessResponseType":null,"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"DELETE","Path":"/v1/notifications/webhooks/{webhook_id}","Visible":true}

import unittest

class WebhooksDeleteRequestTest(unittest.TestCase):

    def testWebhooksDeleteRequest(self):
        self.fail("Not implemented")

if __name__ == "__main__":
    unittest.main()
