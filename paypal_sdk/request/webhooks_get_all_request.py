# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# webhooks_get_all.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhooks.get-all","Description":"Lists all webhooks for an app.","Parameters":[{"Type":"string","VariableName":"anchor_type","Description":"Filters the response by an entity type, `anchor_id`. Value is `APPLICATION` or `ACCOUNT`. Default is `APPLICATION`.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"}],"RequestType":null,"SuccessResponseType":{"Type":"WebhookList","VariableName":"","Description":"List of webhooks.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"GET","Path":"/v1/notifications/webhooks","Visible":true}

import requests

class WebhooksGetAllRequest (requests.Request):
    """
    Lists all webhooks for an app.
    """

    def __init__(self):
        super(WebhooksGetAllRequest, self).__init__(method="GET", url="/v1/notifications/webhooks")

    

    def anchorType(self, anchorType):
        self.url += self.url + "anchor_type=" + str(anchorType) + "&"
        return self
    
