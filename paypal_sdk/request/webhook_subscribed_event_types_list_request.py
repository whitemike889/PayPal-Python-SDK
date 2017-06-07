# This class was generated on Wed, 07 Jun 2017 14:53:47 PDT by version 0.01 of Braintree SDK Generator
# webhook_subscribed_event_types_list_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhook.subscribed-event-types.list","Description":"Lists event subscriptions for a webhook, by ID.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook for which to list subscriptions.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"EventTypeList","VariableName":"","Description":"List of webhook events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks/{webhook_id}/event-types","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class WebhookSubscribedEventTypesListRequest (HttpRequest):
    """
    Lists event subscriptions for a webhook, by ID.
    """

    def __init__(self):
        super(WebhookSubscribedEventTypesListRequest, self).__init__("/v1/notifications/webhooks/{webhook_id}/event-types", "GET")
        self.headers["Content-Type"] = "application/json"

    def webhookId(self, webhookId):
        self.path = self.path.replace("{webhook_id}", str(webhookId))
        return self
    
