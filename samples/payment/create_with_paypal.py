# #Create Payment Using PayPal Sample
# This sample code demonstrates how you can process a
# PayPal Account based Payment.
# API used: /v1/payments/payment
import paypal
import logging

logging.basicConfig(level=logging.INFO)

# ###Payment
# A Payment Resource; create one using
# the above types and intent as 'sale'
payment = paypal.Payment({
  "intent":  "sale",

  # ###Payer
  # A resource representing a Payer that funds a payment
  # Payment Method as 'paypal'
  "payer":  {
    "payment_method":  "paypal" },

  # ###Redirect URLs
  "redirect_urls": {
    "return_url": "http://localhost:3000/payment/execute",
    "cancel_url": "http://localhost:3000/" },

  # ###Transaction
  # A transaction defines the contract of a
  # payment - what is the payment for and who
  # is fulfilling it.
  "transactions":  [ {

    # ###Amount
    # Let's you specify a payment amount.
    "amount":  {
      "total":  "5",
      "currency":  "USD" },
    "description":  "This is the payment transaction description." } ] } )

# Create Payment and return status
if payment.create():
  print "Payment[%s] created successfully"%(payment.id)
  # Redirect the user to given approval url
  for link in payment.links:
    if link.method == "REDIRECT":
      redirect_url = link.href
      print "Redirect for approval: %s"%(redirect_url)
else:
  print "Error while creating payment:"
  print payment.error
