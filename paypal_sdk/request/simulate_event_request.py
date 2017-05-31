# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# simulate_event.py
# DO NOT EDIT
# @type request
# @json {"Name":"simulate.event","Description":"Simulates a webhook event. Specify a sample payload.","Parameters":[],"RequestType":{"Type":"Simulate Event","VariableName":"body","Description":"Uses a sample payload to simulate a mock webhook event.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"SuccessResponseType":{"Type":"Event","VariableName":"","Description":"A webhook event notification.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"POST","Path":"/v1/notifications/simulate-event","Visible":true}

import requests

class SimulateEventRequest (requests.Request):
    """
    Simulates a webhook event. Specify a sample payload.
    """

    def __init__(self):
        super(SimulateEventRequest, self).__init__(method="POST", url="/v1/notifications/simulate-event")

    
    
    
    def body(self, body):
        self.data = body
