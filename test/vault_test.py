from test_helper import paypal, unittest

class TestCreditCard(unittest.TestCase):

  def test_create(self):
    credit_card = paypal.CreditCard({
      "type": "visa",
      "number": "4417119669820331",
      "expire_month": "11",
      "expire_year": "2018",
      "cvv2": "874",
      "first_name": "Joe",
      "last_name": "Shopper" })
    self.assertEqual(credit_card.create(), True)

  def test_find(self):
    None
