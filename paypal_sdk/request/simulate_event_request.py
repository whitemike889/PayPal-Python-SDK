# This class was generated on Wed, 07 Jun 2017 14:53:47 PDT by version 0.01 of Braintree SDK Generator
# simulate_event_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"simulate.event","Description":"Simulates a webhook event. Specify a sample payload.","Parameters":[],"RequestType":{"Type":"Simulate Event","VariableName":"body","Description":"Uses a sample payload to simulate a mock webhook event.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Event","VariableName":"","Description":"A webhook event notification.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/notifications/simulate-event","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class SimulateEventRequest (HttpRequest):
    """
    Simulates a webhook event. Specify a sample payload.
    """

    def __init__(self):
        super(SimulateEventRequest, self).__init__("/v1/notifications/simulate-event", "POST")
        self.headers["Content-Type"] = "application/json"
    
    
    def body(self, body):
        self.data = body
