# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# available_event_type_list.py
# DO NOT EDIT
# @type request
# @json {"Name":"available-event-type.list","Description":"Lists available events to which any webhook can subscribe. For a list of supported events, see [Webhook event names](/docs/integration/direct/webhooks/event-names/).","Parameters":[],"RequestType":null,"SuccessResponseType":{"Type":"EventTypeList","VariableName":"","Description":"List of webhook events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"GET","Path":"/v1/notifications/webhooks-event-types","Visible":true}

import requests

class AvailableEventTypeListRequest (requests.Request):
    """
    Lists available events to which any webhook can subscribe. For a list of supported events, see [Webhook event names](/docs/integration/direct/webhooks/event-names/).
    """

    def __init__(self):
        super(AvailableEventTypeListRequest, self).__init__(method="GET", url="/v1/notifications/webhooks-event-types")

    
    
