import paypal, os, unittest

class Api(unittest.TestCase):

  def setUp(self):
    self.api = paypal.Api(
      client_id= os.environ['PAYPAL_CLIENT_ID'],
      client_secret= os.environ['PAYPAL_CLIENT_SECRET'] )

  def test_get(self):
    payment_history = self.api.get("/v1/payments/payment?count=1")
    self.assertEqual(payment_history['count'], 1)

  def test_post(self):
    credit_card = self.api.post("v1/vault/credit-card", {
      "type": "visa",
      "number": "4417119669820331",
      "expire_month": "11",
      "expire_year": "2018",
      "cvv2": "874",
      "first_name": "Joe",
      "last_name": "Shopper" })
    self.assertEqual(credit_card.get('error'), None)
    self.assertNotEqual(credit_card.get('id'), None)
