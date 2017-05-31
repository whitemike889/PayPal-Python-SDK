# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# event_resend.py
# DO NOT EDIT
# @type request
# @json {"Name":"event.resend","Description":"Resends a webhook event notification, by ID. Any pending notifications are not resent.","Parameters":[{"Type":"string","VariableName":"event_id","Description":"The ID of the webhook event notification to resend.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Event Resend","VariableName":"body","Description":"Resends a webhook event notification, by ID.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"SuccessResponseType":{"Type":"Event","VariableName":"","Description":"A webhook event notification.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"POST","Path":"/v1/notifications/webhooks-events/{event_id}/resend","Visible":true}

import requests

class EventResendRequest (requests.Request):
    """
    Resends a webhook event notification, by ID. Any pending notifications are not resent.
    """

    def __init__(self):
        super(EventResendRequest, self).__init__(method="POST", url="/v1/notifications/webhooks-events/{event_id}/resend")

    

    def eventId(self, eventId):
        self.url = self.url.replace("{event_id}", str(eventId))
        return self
    
    
    def body(self, body):
        self.data = body
