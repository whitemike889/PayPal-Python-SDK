from test_helper import paypal, unittest

class TestPayment(unittest.TestCase):

  def test_create(self):
    payment = paypal.Payment({
      "intent": "sale",
      "payer": {
        "payment_method": "credit_card",
        "funding_instruments": [{
          "credit_card": {
            "type": "visa",
            "number": "4417119669820331",
            "expire_month": "11",
            "expire_year": "2018",
            "cvv2": "874",
            "first_name": "Joe",
            "last_name": "Shopper" }}]},
      "transactions": [{
        "amount": {
          "total": "1.00",
          "currency": "USD" },
        "description": "This is the payment transaction description." }]})
    self.assertEqual(payment.create(), True)

  def test_all(self):
    payment_histroy = paypal.Payment.all({"count": 1 })
    self.assertEqual(payment_histroy.count, 1)
    self.assertEqual(payment_histroy.payments[0].__class__, paypal.Payment)

    # payment_histroy = paypal.Payment.all({"count": 5 })
    # payment_histroy = paypal.Payment.all({"count": 10 })
    # payment_histroy = paypal.Payment.all({"count": 15 })

  def test_find(self):
    payment_history = paypal.Payment.all({"count": 1 })
    payment_id = payment_history.payments[0]['id']
    payment = paypal.Payment.find(payment_id)
    self.assertEqual(payment.id, payment_id)

  def test_execute(self):
    None

class TestSale(unittest.TestCase):

  def test_find(self):
    None

  def test_refund(self):
    None
