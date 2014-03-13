from test_helper import paypal, unittest
from mock import patch, Mock, ANY

class TestPayment(unittest.TestCase):

	def setUp(self):
		self.payment_attributes = {
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
		self.payment = paypal.Payment(self.payment_attributes)

	@patch('test_helper.paypal.Api.post', autospec=True)
	def test_create(self, mock):	
		response = self.payment.create()
		self.assertNotEqual(self.payment.request_id, None)
		mock.assert_called_once_with(self.payment.api,'v1/payments/payment',self.payment_attributes, {'PayPal-Request-Id' : self.payment.request_id}, None)		
		self.assertEqual(response, True)

	@patch('test_helper.paypal.Api.post', autospec=True)
	def test_validation(self, mock):
		'''
		Check that validation fails on trying to create a payment
		with required fields missing
		'''

		payment = paypal.Payment({})
		mock.return_value = {'error' : 'validation', 'message' : 'Invalid request - see details',
		 	'debug_id': 'b8ef6b0aa6329',
		 	'information_link' : 'https://developer.paypal.com/webapps/developer/docs/api/#VALIDATION_ERROR'
		 	}
		response = payment.create()
		mock.assert_called_once_with(self.payment.api,'v1/payments/payment',{}, {'PayPal-Request-Id' : payment.request_id}, None)

		self.assertEqual(response, False)

	
	@patch('test_helper.paypal.Api.get', autospec=True)
	def test_all(self, mock):
		mock.return_value = {'count': 1,'next_id': 'PAY-5TU016908T094823BKLKU7MY', 'payments': [{'update_time': '2014-01-14T15:00:41Z', 'links' : [],
	     	'payer': {'payment_method': 'paypal', 'payer_info': {}}, 'transactions': [], 'state': 'created', 'intent': 'sale', 'id': 'PAY-0A963503EW637094HKLKVCGI'}]}

		payment_histroy = paypal.Payment.all({"count": 1 })

		mock.assert_called_once_with(self.payment.api,'v1/payments/payment?count=1')
		self.assertEqual(payment_histroy.count, 1)

		self.assertEqual(payment_histroy.payments[0].__class__, paypal.Payment)

	@patch('test_helper.paypal.Api.get', autospec=True)
	def test_find(self, mock):
		mock.return_value = {'count': 1,'next_id': 'PAY-5TU016908T094823BKLKU7MY', 'payments': [{'update_time': '2014-01-14T15:00:41Z', 'links' : [],
		'payer': {'payment_method': 'paypal', 'payer_info': {}}, 'transactions': [], 'state': 'created', 'intent': 'sale', 'id': 'PAY-0A963503EW637094HKLKVCGI'}]}

		payment_history = paypal.Payment.all({"count": 1 })
		mock.assert_called_once_with(self.payment.api,'v1/payments/payment?count=1')

		payment_id = payment_history.payments[0]['id']
		mock.return_value = {'id': 'PAY-3KM36407UD294123NKLKV34I', 'intent' : 'sale', 'state' : 'completed', 'description' : 'This is the payment transaction' }
		payment = paypal.Payment.find(payment_id)

		mock.assert_called_with(self.payment.api,'v1/payments/payment/PAY-0A963503EW637094HKLKVCGI')

		self.assertNotEqual(payment.id, payment_id)
    
	@patch('test_helper.paypal.Api.get', autospec=True)
	def test_not_found(self, mock):
		mock.side_effect = paypal.ResourceNotFound('','')
		self.assertRaises(paypal.ResourceNotFound, paypal.Payment.find, ("PAY-1234"))

	@patch('test_helper.paypal.Api.post', autospec=True)
	def test_execute(self, mock):
		paypal_payment_attrib = {
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
	        "description": "This is the payment transaction description." }]}
		payment = paypal.Payment(paypal_payment_attrib)
		mock.return_value = {'id' : 'AY-7JD471929T152531RKLKWR6Q', 'intent' : 'sale', 'state' : 'completed', 'description' : 'This is the payment transaction' }

		response = payment.create()
		mock.assert_called_once_with(self.payment.api,'v1/payments/payment',paypal_payment_attrib, {'PayPal-Request-Id' : payment.request_id}, None)
		self.assertEqual(response, True)
		
		payment.execute({ 'payer_id': 'HZH2W8NPXUE5W' })
		mock.assert_called_with(self.payment.api,'v1/payments/payment/AY-7JD471929T152531RKLKWR6Q/execute',{'payer_id': 'HZH2W8NPXUE5W'}, {'PayPal-Request-Id' : ANY})

class TestSale(unittest.TestCase):

	def setUp(self):
		self.payment_attributes = {
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
		self.payment = paypal.Payment(self.payment_attributes)

	@patch('test_helper.paypal.Api.post', autospec=True)
	def create_sale(self, mock):
		mock.return_value = {'id': 'PAY-888868365Y436124EKLKW6JA', 'update_time': '2014-01-14T17:09:00Z', 'links': [], 'payer' : {}, 'transactions': [{'related_resources': [{'sale': {'update_time': '2014-01-14T17:09:00Z', 
							  	'links' : [], 'state': 'completed', 'id': '5VX40080GX603650', 
							  	'amount': {'currency': 'USD', 'total': '1.00'} }}],
							  	}]}
		response = self.payment.create()
		self.assertEqual(response, True)
		return self.payment.transactions[0].related_resources[0].sale
	    
	@patch('test_helper.paypal.Api.get', autospec=True)    
	def test_find(self, mock):
		sale = paypal.Sale.find(self.create_sale().id)
		mock.assert_called_once_with(sale.api,'v1/payments/sale/5VX40080GX603650')
		self.assertEqual(sale.__class__, paypal.Sale)

class TestRefund(unittest.TestCase):

	@patch('test_helper.paypal.Api.get', autospec=True)  
	def test_find(self,mock):
		refund_id = '5C377143F71265517'
		mock.return_value = {'update_time': '2013-04-01T08:44:09Z',
			 'sale_id': '7DY409201T7922549', 'state': 'completed', 'id': refund_id,
			 'amount': {'currency': 'USD', 'total': '0.01'}}
		refund = paypal.Refund.find(refund_id)
		mock.assert_called_once_with(refund.api, 'v1/payments/refund/'+refund_id)
		self.assertEqual(refund.__class__, paypal.Refund)

class TestAuthorization(unittest.TestCase):

	def setUp(self):
		self.payment_attributes = {
		"intent": "authorize",
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
		self.payment = paypal.Payment(self.payment_attributes)
		self.auth_id = '3J872959AY1512221'
		self.authorization_attributes = {'valid_until': '2014-02-12T21:11:25Z',
			  'update_time': '2014-01-14T21:11:33Z', 'links': [{'href': 'https://api.sandbox.paypal.com/v1/payments/authorization/3J872959AY1512221', 'method': 'GET', 'rel': 'self'},
			   {'href': 'https://api.sandbox.paypal.com/v1/payments/authorization/3J872959AY1512221/capture', 'method': 'POST', 'rel': 'capture'},
			    {'href': 'https://api.sandbox.paypal.com/v1/payments/authorization/3J872959AY1512221/void', 'method': 'POST', 'rel': 'void'},
			     {'href': 'https://api.sandbox.paypal.com/v1/payments/payment/PAY-1EE254486E964802VKLK2P7I', 'method': 'GET', 'rel': 'parent_payment'}],
			      'state': 'authorized', 'parent_payment': 'PAY-1EE254486E964802VKLK2P7I', 'amount': {'currency': 'USD', 'total': '1.00', 'details': {'subtotal': '1.00'}},
			       'create_time': '2014-01-14T21:11:25Z', 'id': '3J872959AY1512221'}
		self.capture_attributes = { "amount": { "currency": "USD", "total": "1.00" } }

	@patch('test_helper.paypal.Api.post', autospec=True)
	def test_create(self, mock):
		mock.return_value = {'id': 'PAY-888868365Y436124EKLKW6JA', 'update_time': '2014-01-14T17:09:00Z', 'links': [], 'payer' : {},
		'transactions': [{'related_resources': [{'authorization': self.authorization_attributes}],
		    					  	}]}
		response = self.payment.create()
		mock.assert_called_once_with(self.payment.api,'v1/payments/payment',self.payment_attributes, {'PayPal-Request-Id' : self.payment.request_id}, None)		
		self.assertEqual(response, True)
		self.assertNotEqual(self.payment.transactions[0].related_resources[0].authorization.id, None)

	@patch('test_helper.paypal.Api.get', autospec=True) 
	def test_find(self, mock):
		authorization = paypal.Authorization.find(self.auth_id)
		self.assertEqual(authorization.__class__, paypal.Authorization)
		mock.assert_called_once_with(authorization.api, 'v1/payments/authorization/'+self.auth_id)

	@patch('test_helper.paypal.Api.post', autospec=True) 
	def test_capture(self, mock):
		authorization = paypal.Authorization.find(self.auth_id)
		capture = authorization.capture(self.capture_attributes)
		self.assertEqual(capture.success(), True)
		mock.assert_called_once_with(authorization.api, 'v1/payments/authorization/' + self.auth_id + '/capture', self.capture_attributes, 
			{'PayPal-Request-Id': ANY})

	@patch('test_helper.paypal.Api.post', autospec=True) 
	def test_void(self, mock):
		authorization = paypal.Authorization.find(self.auth_id)
		self.assertEqual(authorization.void(), True)
		mock.assert_called_once_with(authorization.api, 'v1/payments/authorization/' + self.auth_id + '/void', {}, 
			{'PayPal-Request-Id': ANY})
  
	@patch('test_helper.paypal.Api.get', autospec=True) 
	def test_capture_find(self, mock):
		capture_id = '7S373777UY2709045'
		capture = paypal.Capture.find(capture_id)
		self.assertEqual(capture.__class__, paypal.Capture)
		mock.assert_called_once_with(capture.api, 'v1/payments/capture/' + capture_id)

