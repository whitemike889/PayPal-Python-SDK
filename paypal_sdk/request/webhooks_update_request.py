# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# webhooks_update_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhooks.update","Description":"Replaces webhook fields with new values. Pass a `json_patch` object with `replace` operation and `path`, which is `/url` for a URL or `/event_types` for events. The `value` is either the URL or a list of events.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook to update.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"JSON Patch","VariableName":"body","Description":"A JSON patch request.","IsArray":true,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Webhook","VariableName":"","Description":"One or more webhook objects.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"PATCH","Path":"/v1/notifications/webhooks/{webhook_id}","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class WebhooksUpdateRequest (HttpRequest):
    """
    Replaces webhook fields with new values. Pass a `json_patch` object with `replace` operation and `path`, which is `/url` for a URL or `/event_types` for events. The `value` is either the URL or a list of events.
    """

    def __init__(self):
        super(WebhooksUpdateRequest, self).__init__("/v1/notifications/webhooks/{webhook_id}", "PATCH")
        self.headers["Content-Type"] = "application/json"

    def webhookId(self, webhookId):
        self.url = self.path.replace("{webhook_id}", str(webhookId))
        return self
    
    
    def body(self, body):
        self.data = body
