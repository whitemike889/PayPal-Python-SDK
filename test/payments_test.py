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
        "item_list": {
          "items": [{
            "name": "item",
            "sku": "item",
            "price": "1.00",
            "currency": "USD",
            "quantity": 1 }]},
        "amount": {
          "total": "1.00",
          "currency": "USD" },
        "description": "This is the payment transaction description." }]})
    self.assertEqual(payment.create(), True)

  def test_validation(self):
    payment = paypal.Payment({})
    self.assertEqual(payment.create(), False)

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

  def test_not_found(self):
    self.assertRaises(paypal.ResourceNotFound, paypal.Payment.find, ("PAY-1234"))

  def test_execute(self):
    payment = paypal.Payment({
      "intent": "sale",
      "payer": {
        "payment_method": "paypal" },
      "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/" },
      "transactions": [{
        "item_list": {
          "items": [{
            "name": "item",
            "sku": "item",
            "price": "1.00",
            "currency": "USD",
            "quantity": 1 }]},
        "amount": {
          "total": "1.00",
          "currency": "USD" },
        "description": "This is the payment transaction description." }]})
    self.assertEqual(payment.create(), True)
    payment.execute({ 'payer_id': 'HZH2W8NPXUE5W' })

class TestSale(unittest.TestCase):

  def test_find(self):
    sale = paypal.Sale.find("7DY409201T7922549")
    self.assertEqual(sale.__class__, paypal.Sale)

  def test_refund(self):
    sale   = paypal.Sale.find("7DY409201T7922549")
    refund = sale.refund({ "amount": { "total": "0.01", "currency": "USD" } })
    self.assertEqual(refund.success(), True)

class TestRefund(unittest.TestCase):

  def test_find(self):
    refund = paypal.Refund.find("5C377143F71265517")
    self.assertEqual(refund.__class__, paypal.Refund)
