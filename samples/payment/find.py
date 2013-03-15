# #GetPayment Sample
# This sample code demonstrates how you can retrieve
# the details of a payment resource.
# API used: /v1/payments/payment/{payment-id}
import paypal
import logging
logging.basicConfig(level=logging.INFO)

try:
  # Retrieve the payment object by calling the
  # `find` method
  # on the Payment class by passing Payment ID
  payment = paypal.Payment.find("PAY-0XL713371A312273YKE2GCNI")
  print("Got Payment Details for Payment[%s]"%(payment.id))

except paypal.ResourceNotFound as error:
  # It will through ResourceNotFound exception if the payment not found
  print("Payment Not Found")

