# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# webhooks_get_all_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"webhooks.get-all","Description":"Lists all webhooks for an app.","Parameters":[{"Type":"string","VariableName":"anchor_type","Description":"Filters the response by an entity type, `anchor_id`. Value is `APPLICATION` or `ACCOUNT`. Default is `APPLICATION`.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"}],"RequestType":null,"ResponseType":{"Type":"WebhookList","VariableName":"","Description":"List of webhooks.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class WebhooksGetAllRequest (HttpRequest):
    """
    Lists all webhooks for an app.
    """

    def __init__(self):
        super(WebhooksGetAllRequest, self).__init__("/v1/notifications/webhooks", "GET")
        self.headers["Content-Type"] = "application/json"

    def anchorType(self, anchorType):
        self.url += self.path + "anchor_type=" + str(anchorType) + "&"
        return self
    
