# #Create Payment Using PayPal Sample
# This sample code demonstrates how you can process a
# PayPal Account based Payment.
# API used: /v1/payments/payment
import paypalrestsdk

#authorization code from mobile sdk
authorization_code = ''

#Save refresh token in database
refresh_token = api.get_refresh_token(authorization_code)

#correlation id from mobile sdk
correlation_id=''

payment = paypalrestsdk.Payment({
  "intent":  "authorize",

  "payer": {
    "payment_method":  "paypal" },

  "transactions": [{

    "amount":{
      "total":  "0.17",
      "currency":  "USD"},
    "description":  "This is the payment transaction description."}]})

# If payment intent is authorize prints out the authorization
# id, it can be used to capture payment later using 
# samples/authorization/capture.py
if payment.create(refresh_token, correlation_id):
  print("Payment %s created successfully"%(payment.id))
  if payment['intent'] == "authorize":
    print(
      "Payment %s authorized. Authorization id is %s"
      %(payment.id, payment['transactions'][0]['related_resources'][0]['authorization']['id'])
      )
else:
  print("Error while creating payment:")
  print(payment.error)
