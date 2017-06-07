# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# webhooks_get_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhooks.get","Description":"Shows details for a webhook, by ID.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook for which to show details.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Webhook","VariableName":"","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks/{webhook_id}","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class WebhooksGetRequest (HttpRequest):
    """
    Shows details for a webhook, by ID.
    """

    def __init__(self):
        super(WebhooksGetRequest, self).__init__("/v1/notifications/webhooks/{webhook_id}", "GET")
        self.headers["Content-Type"] = "application/json"

    def webhookId(self, webhookId):
        self.url = self.path.replace("{webhook_id}", str(webhookId))
        return self
    
