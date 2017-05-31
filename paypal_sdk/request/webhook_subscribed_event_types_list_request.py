# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# webhook_subscribed_event_types_list.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhook.subscribed-event-types.list","Description":"Lists event subscriptions for a webhook, by ID.","Parameters":[{"Type":"string","VariableName":"webhook_id","Description":"The ID of the webhook for which to list subscriptions.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"SuccessResponseType":{"Type":"EventTypeList","VariableName":"","Description":"List of webhook events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"GET","Path":"/v1/notifications/webhooks/{webhook_id}/event-types","Visible":true}

import requests

class WebhookSubscribedEventTypesListRequest (requests.Request):
    """
    Lists event subscriptions for a webhook, by ID.
    """

    def __init__(self):
        super(WebhookSubscribedEventTypesListRequest, self).__init__(method="GET", url="/v1/notifications/webhooks/{webhook_id}/event-types")

    

    def webhookId(self, webhookId):
        self.url = self.url.replace("{webhook_id}", str(webhookId))
        return self
    
