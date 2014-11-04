"""Verify received webhook payload on merchant server. 
Recommended first step before starting to parse the message e.g.
get_webhook_event_resource.py in the samples folder

Helpful link https://developer.paypal.com/docs/integration/direct/rest-webhooks-overview/
"""
from paypalrestsdk.notifications import WebhookEvent
import logging
logging.basicConfig(level=logging.INFO)

# The payload body sent in the webhook event
event_body = "{\"id\":\"WH-8UH59159LY570081N-5FX3594634324213T\",\"create_time\":\"2014-10-10T17:36:15Z\",\"resource_type\":\"authorization\",\"event_type\":\"PAYMENT.AUTHORIZATION.CREATED\",\"summary\":\"A successful payment authorization was created for 0.60 USD\",\"resource\":{\"id\":\"2LP967258V024852T\",\"create_time\":\"2014-10-10T17:34:11Z\",\"update_time\":\"2014-10-10T17:35:16Z\",\"amount\":{\"total\":\"0.60\",\"currency\":\"USD\",\"details\":{\"subtotal\":\"0.60\"}},\"payment_mode\":\"INSTANT_TRANSFER\",\"state\":\"authorized\",\"protection_eligibility\":\"ELIGIBLE\",\"protection_eligibility_type\":\"ITEM_NOT_RECEIVED_ELIGIBLE,UNAUTHORIZED_PAYMENT_ELIGIBLE\",\"parent_payment\":\"PAY-6FD94763FB485961SKQ4BREY\",\"valid_until\":\"2014-11-08T17:34:11Z\",\"links\":[{\"href\":\"https://api.sandbox.paypal.com/v1/payments/authorization/2LP967258V024852T\",\"rel\":\"self\",\"method\":\"GET\"},{\"href\":\"https://api.sandbox.paypal.com/v1/payments/authorization/2LP967258V024852T/capture\",\"rel\":\"capture\",\"method\":\"POST\"},{\"href\":\"https://api.sandbox.paypal.com/v1/payments/authorization/2LP967258V024852T/void\",\"rel\":\"void\",\"method\":\"POST\"},{\"href\":\"https://api.sandbox.paypal.com/v1/payments/authorization/2LP967258V024852T/reauthorize\",\"rel\":\"reauthorize\",\"method\":\"POST\"},{\"href\":\"https://api.sandbox.paypal.com/v1/payments/payment/PAY-6FD94763FB485961SKQ4BREY\",\"rel\":\"parent_payment\",\"method\":\"GET\"}]},\"links\":[{\"href\":\"https://api.sandbox.paypal.com/v1/notifications/webhooks-events/WH-8UH59159LY570081N-5FX3594634324213T\",\"rel\":\"self\",\"method\":\"GET\"},{\"href\":\"https://api.sandbox.paypal.com/v1/notifications/webhooks-events/WH-8UH59159LY570081N-5FX3594634324213T/resend\",\"rel\":\"resend\",\"method\":\"POST\"}]}"
# Paypal-Transmission-Id in webhook payload header
transmission_id = "efcfecb0-50a3-11e4-acdb-8d0d8bca8f12"
# Paypal-Transmission-Time in webhook payload header
timestamp = "2014-10-10T17:36:16Z"
# Webhook id created
webhook_id = "40Y916089Y8324740"
# Paypal-Transmission-Sig in webhook payload header
actual_signature = "mcLeCd3PZXLR2DYFbcgf/Fzjk0wAaQ0+awY7en8J3w+UxlE5nzwIQIgHAup+x7cCrEWKzSLNSdAw9OCXb+0Pg030OEhP6iSEBr3XcTrfNXhrjz9Mbl35fe7qY6eOM4lJy2vRYAGGj9X2zXNI4Ag4wUIZlc03QRCkvAedGOkopuHXCepeVVgCEIaB4NCHgLKgjpmRaj6bRXdz1Odlm0BrG6pb7Fjw3cbhbBrw6twZugD8d/fj3juUU63UFGp77RGTxtMdnnAfHwlAQYSWRxiKxQbrE0PFZyICRcXd7hgluIv+ts/hqho4vVMi9UkRXfJCtaJ6o/tjDZjnO9rjMnu++g=="
# Paypal-Cert-Url in webhook payload header
cert_url = 'https://api.sandbox.paypal.com/v1/notifications/certs/CERT-360caa42-35c2ed1e-21e9a5d6'    

response = WebhookEvent.verify(transmission_id, timestamp, webhook_id, event_body, cert_url, actual_signature)
print(response)
