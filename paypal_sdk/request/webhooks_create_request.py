# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# webhooks_create_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhooks.create","Description":"Subscribes your webhook listener to events. A successful call returns a [`webhook`](/docs/api/webhooks/#definition-webhook:v1) object, which includes the webhook ID for later use.","Parameters":[],"RequestType":{"Type":"Webhook","VariableName":"body","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Webhook","VariableName":"","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/notifications/webhooks","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class WebhooksCreateRequest (HttpRequest):
    """
    Subscribes your webhook listener to events. A successful call returns a [`webhook`](/docs/api/webhooks/#definition-webhook:v1) object, which includes the webhook ID for later use.
    """

    def __init__(self):
        super(WebhooksCreateRequest, self).__init__("/v1/notifications/webhooks", "POST")
        self.headers["Content-Type"] = "application/json"
    
    
    def body(self, body):
        self.data = body
