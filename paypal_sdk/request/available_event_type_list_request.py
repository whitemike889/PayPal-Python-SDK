# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# available_event_type_list_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"available-event-type.list","Description":"Lists available events to which any webhook can subscribe. For a list of supported events, see [Webhook event names](/docs/integration/direct/webhooks/event-names/).","Parameters":[],"RequestType":null,"ResponseType":{"Type":"EventTypeList","VariableName":"","Description":"List of webhook events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/notifications/webhooks-event-types","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class AvailableEventTypeListRequest (HttpRequest):
    """
    Lists available events to which any webhook can subscribe. For a list of supported events, see [Webhook event names](/docs/integration/direct/webhooks/event-names/).
    """

    def __init__(self):
        super(AvailableEventTypeListRequest, self).__init__("/v1/notifications/webhooks-event-types", "GET")
        self.headers["Content-Type"] = "application/json"
    
