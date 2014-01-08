from test_helper import unittest, client_id, client_secret, paypal
from mock import patch, Mock, ANY
import logging
logging.basicConfig(filename='eg.log',level=logging.DEBUG)

#TODO: REPLACE GETT

class Api(unittest.TestCase):

  def setUp(self):
    self.api = paypal.Api(
      client_id= client_id, 
      client_secret= client_secret
    )
    
  def test_endpoint(self):
    
    new_api = paypal.Api(mode="live")
    self.assertEqual(new_api.endpoint, "https://api.paypal.com")
    self.assertEqual(new_api.token_endpoint, "https://api.paypal.com")
    
    new_api = paypal.Api(mode="sandbox")
    self.assertEqual(new_api.endpoint, "https://api.sandbox.paypal.com")
    self.assertEqual(new_api.token_endpoint, "https://api.sandbox.paypal.com")

    new_api = paypal.Api(endpoint="https://custom-endpoint.paypal.com")
    self.assertEqual(new_api.endpoint, "https://custom-endpoint.paypal.com")
    self.assertEqual(new_api.token_endpoint, "https://custom-endpoint.paypal.com")
  
  #@patch('paypalrestsdk.api.httplib2')
  #def test_get(self, patch_api):
  def test_get(self):
    self.api.request = Mock()
    payment_history = self.api.get("/v1/payments/payment?count=1")
    self.api.request.assert_called_once_with('https://api.sandbox.paypal.com/v1/payments/payment?count=1','GET',headers={})
  
  
  def test_post(self):
    self.api.request = Mock()
    credit_card = self.api.post("v1/vault/credit-card", {
      "type": "visa",
      "number": "4417119669820331",
      "expire_month": "11",
      "expire_year": "2018",
      "cvv2": "874",
      "first_name": "Joe",
      "last_name": "Shopper" })
    print credit_card
    self.assertEqual(credit_card.get('error'), None)
    self.assertNotEqual(credit_card.get('id'), None)
  '''
  def test_post_mock(self):
    self.api.request = Mock()
    self.api.post("v1/vault/credit-card", {
      "type": "visa",
      "number": "4417119669820331",
      "expire_month": "11",
      "expire_year": "2018",
      "cvv2": "874",
      "first_name": "Joe",
      "last_name": "Shopper" })
    self.api.assert_called_once_with('https://api.sandbox.paypal.com/v1/vault/credit-card','POST',params)
  '''



