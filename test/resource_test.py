from test_helper import unittest
from paypalrestsdk.resource import Resource
'''
class TestResource(unittest.TestCase):
  def test_getter(self):
    data = {
      'name': 'testing',
      'amount': 10.0,
      'transaction': { 'description': 'testing' },
      'items': [ { 'name': 'testing' } ] }
    resource = Resource(data)
    self.assertEqual(resource.name, 'testing')
    self.assertEqual(resource['name'], 'testing')
    self.assertEqual(resource.amount, 10.0)
    self.assertEqual(resource.items[0].__class__, Resource)
    self.assertEqual(resource.items[0].name, 'testing')
    self.assertEqual(resource.items[0]['name'], 'testing')
    self.assertEqual(resource.unknown, None)
    self.assertRaises(KeyError, lambda: resource['unknown'])

  def test_setter(self):
    data = { 'name': 'testing' }
    resource = Resource(data)
    self.assertEqual(resource.name, 'testing' )
    resource.name = 'changed'
    self.assertEqual(resource.name, 'changed' )
    resource['name'] = 'again-changed'
    self.assertEqual(resource.name, 'again-changed' )
    resource.transaction = { 'description': 'testing' }
    self.assertEqual(resource.transaction.__class__, Resource)
    self.assertEqual(resource.transaction.description, 'testing')

  def test_to_dict(self):
    data = {
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
        "description": "This is the payment transaction description." }]}
    resource = Resource(data)
    self.assertEqual(resource.to_dict(), data)

  def test_request_id(self):
    data = {
      'name': 'testing',
      'request_id': 1234 }
    resource = Resource(data)
    self.assertEqual(resource.to_dict(), {'name': 'testing'})
    self.assertEqual(resource.request_id, 1234)
    self.assertEqual(resource.http_headers(), {'PayPal-Request-Id': 1234})

  def test_http_headers(self):
    data = {
     'name': 'testing',
     'header': { 'My-Header': 'testing' } }
    resource = Resource(data)
    self.assertEqual(resource.header, {'My-Header': 'testing'})
    self.assertEqual(resource.http_headers(), {'PayPal-Request-Id': resource.request_id, 'My-Header': 'testing'})

'''


