# This class was generated on Tue, 30 May 2017 15:10:07 PDT by version 0.01 of Braintree SDK Generator
# verify_webhook_signature_post.py
# DO NOT EDIT
# @type request
# @json {"Name":"verify.webhook.signature.post","Description":"Verifies a webhook signature.","Parameters":[],"RequestType":{"Type":"Verify Webhook Signature","VariableName":"body","Description":"Verify the webhook signature.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"SuccessResponseType":{"Type":"Verify Webhook Signature Response","VariableName":"","Description":"The verify webhook signature response.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"DefaultResponseType":{"Type":"error","VariableName":"","Description":"Details about an error.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"HttpMethod":"POST","Path":"/v1/notifications/verify-webhook-signature","Visible":true}

import requests

class VerifyWebhookSignaturePostRequest (requests.Request):
    """
    Verifies a webhook signature.
    """

    def __init__(self):
        super(VerifyWebhookSignaturePostRequest, self).__init__(method="POST", url="/v1/notifications/verify-webhook-signature")

    
    
    
    def body(self, body):
        self.data = body
