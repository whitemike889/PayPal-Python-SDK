# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# event_list.py
# DO NOT EDIT
# @type request
# @json {"Name":"event.list","Description":"Lists webhook event notifications. Use query parameters to filter the response.","Parameters":[{"Type":"string","VariableName":"end_time","Description":"Filters the webhook event notifications in the response to those created on or after the `start_time` and on or before this date and time. Both values are in [RFC 3339 Section 5.6](http://tools.ietf.org/html/rfc3339#section-5.6) format. Example: `end_time=2013-03-06T11:00:00Z`.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"event_type","Description":"Filters the response to a single event.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"integer","VariableName":"page_size","Description":"The number of webhook event notifications to return in the response.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"start_time","Description":"Filters the webhook event notifications in the response to those created on or after this date and time and on or before the `end_time` value. Both values are in [RFC 3339 Section 5.6](http://tools.ietf.org/html/rfc3339#section-5.6) format. Example: `start_time=2013-03-06T11:00:00Z`.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"string","VariableName":"transaction_id","Description":"Filters the response to a single transaction, by ID.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null,"Location":"query"}],"RequestType":null,"SuccessResponseType":{"Type":"EventList","VariableName":"","Description":"List of webhooks events.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"GET","Path":"/v1/notifications/webhooks-events","Visible":true}

import unittest
import paypal_core
import paypal_sdk

class EventListRequestTest(unittest.TestCase):

    def testEventListRequest(self):
        paypal = paypal_core.PayPalHttpClient(paypal_core.PayPalEnvironment("AelYYn02_l-ihI2nkHTwPshVIw1_SgqrthwKDjRCwuZJb_RNWhlv0TUvr0SSf1y2cLYlOxyKa7x3QLs9", "EBhm_gir01y0D_d2aIEDQLT5rfXS64q2RtrIZkyewjOidx9qVVJD_D2kxSe8x3YHfkKTHV-K-9Z22Wes", paypal_core.PayPalEnvironment.SANDBOX))

        request = paypal_sdk.AvailableEventTypeListRequest()

        try:
            response = paypal.execute(request)
            print response.result
        except IOError as ioe:
            self.fail(ioe)

if __name__ == "__main__":
    unittest.main()
