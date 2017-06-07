# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# webhooks_delete_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhooks.delete","Description":"Deletes a webhook, by ID.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook to delete.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":null,"ContentType":"application/json","HttpMethod":"DELETE","Path":"/v1/notifications/webhooks/{webhook_id}","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class WebhooksDeleteRequest (HttpRequest):
    """
    Deletes a webhook, by ID.
    """

    def __init__(self):
        super(WebhooksDeleteRequest, self).__init__("/v1/notifications/webhooks/{webhook_id}", "DELETE")
        self.headers["Content-Type"] = "application/json"

    def webhookId(self, webhookId):
        self.url = self.path.replace("{webhook_id}", str(webhookId))
        return self
    
