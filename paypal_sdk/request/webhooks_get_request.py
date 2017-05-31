# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# webhooks_get.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhooks.get","Description":"Shows details for a webhook, by ID.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook for which to show details.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"SuccessResponseType":{"Type":"Webhook","VariableName":"","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"GET","Path":"/v1/notifications/webhooks/{webhook_id}","Visible":true}

import requests

class WebhooksGetRequest (requests.Request):
    """
    Shows details for a webhook, by ID.
    """

    def __init__(self):
        super(WebhooksGetRequest, self).__init__(method="GET", url="/v1/notifications/webhooks/{webhook_id}")

    

    def webhookId(self, webhookId):
        self.url = self.url.replace("{webhook_id}", str(webhookId))
        return self
    
