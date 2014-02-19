from test_helper import unittest, client_id, client_secret, paypal
from mock import patch, Mock, ANY

class Api(unittest.TestCase):

  def setUp(self):
    self.api = paypal.Api(
      client_id= client_id, 
      client_secret= client_secret
    )
    self.api.request = Mock()
    self.card_attributes = {
      "type": "visa",
      "number": "4417119669820331",
      "expire_month": "11",
      "expire_year": "2018",
      "cvv2": "874",
      "first_name": "Joe",
      "last_name": "Shopper" }

    
  def test_endpoint(self):
    new_api = paypal.Api(mode="live", client_id="dummy", client_secret="dummy")
    self.assertEqual(new_api.endpoint, "https://api.paypal.com")
    self.assertEqual(new_api.token_endpoint, "https://api.paypal.com")

    new_api = paypal.Api(mode="sandbox", client_id="dummy", client_secret="dummy")
    self.assertEqual(new_api.endpoint, "https://api.sandbox.paypal.com")
    self.assertEqual(new_api.token_endpoint, "https://api.sandbox.paypal.com")

    new_api = paypal.Api(endpoint="https://custom-endpoint.paypal.com", client_id="dummy", client_secret="dummy")
    self.assertEqual(new_api.endpoint, "https://custom-endpoint.paypal.com")
    self.assertEqual(new_api.token_endpoint, "https://custom-endpoint.paypal.com")
  
  def test_get(self):
    payment_history = self.api.get("/v1/payments/payment?count=1")
    self.api.request.assert_called_once_with('https://api.sandbox.paypal.com/v1/payments/payment?count=1','GET',headers={})
  
  def test_post(self):
    self.api.request.return_value = {'id': 'test'}
    credit_card = self.api.post("v1/vault/credit-card", self.card_attributes)

    #self.api.request.assert_called_once_with('https://api.sandbox.paypal.com/v1/vault/credit-card', 'POST', body=self.card_attributes, headers={})
  
    self.assertEqual(credit_card.get('error'), None)
    self.assertNotEqual(credit_card.get('id'), None)

  def test_bad_request(self):
    self.api.request.return_value = {'error': 'test'}
    credit_card = self.api.post("v1/vault/credit-card", {})
    
    self.api.request.assert_called_once_with('https://api.sandbox.paypal.com/v1/vault/credit-card',
                                        'POST', 
                                         data='{}',
                                         headers={})
    self.assertNotEqual(credit_card.get('error'), None)

  def test_expired_time(self):
    old_token = self.api.get_token()
    self.api.token_hash["expires_in"] = 0
    self.assertNotEqual(self.api.get_token(), old_token)

  def test_not_found(self):
    self.api.request.side_effect = paypal.ResourceNotFound("error")
    self.assertRaises(paypal.ResourceNotFound, self.api.get, ("/v1/payments/payment/PAY-1234"))
