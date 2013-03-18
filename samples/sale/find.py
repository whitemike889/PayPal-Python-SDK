# # Get Details of a Sale Transaction Sample
# This sample code demonstrates how you can retrieve
# details of completed Sale Transaction.
# API used: /v1/payments/sale/{sale-id}
import paypal
import logging
logging.basicConfig(level=logging.INFO)

try:
  # Get Sale object by passing sale id
  sale = paypal.Sale.find("7DY409201T7922549")
  print("Got Sale details for Sale[%s]"%(sale.id))

except paypal.ResourceNotFound as error:
  print("Sale Not Found")
