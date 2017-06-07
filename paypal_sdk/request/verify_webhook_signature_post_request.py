# This class was generated on Wed, 07 Jun 2017 14:36:02 PDT by version 0.01 of Braintree SDK Generator
# verify_webhook_signature_post_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"verify.webhook.signature.post","Description":"Verifies a webhook signature.","Parameters":[],"RequestType":{"Type":"Verify Webhook Signature","VariableName":"body","Description":"Verify the webhook signature.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Verify Webhook Signature Response","VariableName":"","Description":"The verify webhook signature response.","IsArray":false,"ReadOnly":false,"Visible":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/notifications/verify-webhook-signature","Visible":true,"ExpectedStatusCode":200}

from braintreehttp import HttpRequest

class VerifyWebhookSignaturePostRequest (HttpRequest):
    """
    Verifies a webhook signature.
    """

    def __init__(self):
        super(VerifyWebhookSignaturePostRequest, self).__init__("/v1/notifications/verify-webhook-signature", "POST")
        self.headers["Content-Type"] = "application/json"
    
    
    def body(self, body):
        self.data = body
