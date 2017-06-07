# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# event_resend_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"event.resend","Description":"Resends a webhook event notification, by ID. Any pending notifications are not resent.","Parameters":[{"Type":"string","VariableName":"event_id","Description":"The ID of the webhook event notification to resend.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Event Resend","VariableName":"body","Description":"Resends a webhook event notification, by ID.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Event","VariableName":"","Description":"A webhook event notification.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/notifications/webhooks-events/{event_id}/resend","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class EventResendRequest (HttpRequest):
    """
    Resends a webhook event notification, by ID. Any pending notifications are not resent.
    """

    def __init__(self):
        super(EventResendRequest, self).__init__("/v1/notifications/webhooks-events/{event_id}/resend", "POST")
        self.headers["Content-Type"] = "application/json"

    def eventId(self, eventId):
        self.url = self.path.replace("{event_id}", str(eventId))
        return self
    
    
    def body(self, body):
        self.data = body
