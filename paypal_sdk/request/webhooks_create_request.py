# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# webhooks_create.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhooks.create","Description":"Subscribes your webhook listener to events. A successful call returns a [`webhook`](/docs/api/webhooks/#definition-webhook:v1) object, which includes the webhook ID for later use.","Parameters":[],"RequestType":{"Type":"Webhook","VariableName":"body","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"SuccessResponseType":{"Type":"Webhook","VariableName":"","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"POST","Path":"/v1/notifications/webhooks","Visible":true}

import requests

class WebhooksCreateRequest (requests.Request):
    """
    Subscribes your webhook listener to events. A successful call returns a [`webhook`](/docs/api/webhooks/#definition-webhook:v1) object, which includes the webhook ID for later use.
    """

    def __init__(self):
        super(WebhooksCreateRequest, self).__init__(method="POST", url="/v1/notifications/webhooks")

    
    
    
    def body(self, body):
        self.data = body
