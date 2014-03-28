from test_helper import paypal, unittest
from mock import patch, ANY

class TestInvoice(unittest.TestCase):

	def setUp(self):
		self.invoice_attributes = {
			'merchant_info': {
				'email': 'ppaas_default@paypal.com'
			},
			'billing_info': [
				{ 'email': 'example@example.com' }
			],
			'items': [
				{
					'name': 'Sutures',
					'quantity': 100,
					'unit_price': {
						'currency': 'USD',
						'value': 5
					}
				}
			]
		}
		self.invoice = paypal.Invoice(self.invoice_attributes)
		self.invoice.id = 'INV2-RUVR-ADWQ-H89Y-ABCD'

	@patch('test_helper.paypal.Api.post', autospec=True)
	def test_create(self, mock):
		invoice = paypal.Invoice(self.invoice_attributes)
		response = invoice.create()

		mock.assert_called_once_with(invoice.api,'v1/invoices/invoice', self.invoice_attributes, {'PayPal-Request-Id' : invoice.request_id}, None)
		self.assertEqual(response, True)

	@patch('test_helper.paypal.Api.get', autospec=True)
	def test_find(self, mock):
		invoice = paypal.Invoice.find(self.invoice.id)

		mock.assert_called_once_with(self.invoice.api, 'v1/invoices/invoice/'+self.invoice.id)
		self.assertTrue(isinstance(invoice, paypal.Invoice))

	@patch('test_helper.paypal.Api.get', autospec=True)
	def test_all(self, mock):
		mock.return_value = {'total_count': 1, 'invoices': [self.invoice_attributes]}
		history = paypal.Invoice.all({'count': 1})

		mock.assert_called_once_with(self.invoice.api, 'v1/invoices/invoice?count=1')
		self.assertEqual(history.total_count, 1)
		self.assertTrue(isinstance(history.invoices[0], paypal.Invoice))



	@patch('test_helper.paypal.Api.delete', autospec=True)
	def test_delete(self, mock):
		response = self.invoice.delete()

		mock.assert_called_once_with(self.invoice.api,'v1/invoices/invoice/'+self.invoice.id)
		self.assertEqual(response, True)

	@patch('test_helper.paypal.Api.put', autospec=True)
	def test_update(self, mock):
		response = self.invoice.update(self.invoice_attributes)

		mock.assert_called_once_with(self.invoice.api,'v1/invoices/invoice/'+self.invoice.id, self.invoice_attributes, {'PayPal-Request-Id' : self.invoice.request_id}, None)
		self.assertEqual(response, True)

	@patch('test_helper.paypal.Api.post', autospec=True)
	def test_send(self, mock):
		response = self.invoice.send()

		mock.assert_called_once_with(self.invoice.api,'v1/invoices/invoice/'+self.invoice.id+'/send', {}, {'PayPal-Request-Id' : ANY})
		self.assertEqual(response, True)


	@patch('test_helper.paypal.Api.post', autospec=True)
	def test_search(self, mock):
		search_attributes = {
			"start_invoice_date" : "2010-05-10 PST",
			"end_invoice_date" : "2013-05-11 PST",
			"page" : 1,
			"page_size" : 20,
			"total_count_required" : True
		}
		mock.return_value = {'total_count': 1, 'invoices': [self.invoice_attributes]}

		history = paypal.Invoice.search(search_attributes);

		mock.assert_called_once_with(self.invoice.api,'v1/invoices/invoice/search', search_attributes)
		self.assertEqual(history.total_count, 1)
		self.assertTrue(isinstance(history.invoices[0], paypal.Invoice))

	@patch('test_helper.paypal.Api.post', autospec=True)
	def test_remind(self, mock):
		remind_attributes = {
			'subject': 'Past due',
			'note': 'Please pay soon',
			'send_to_merchant': True
		}

		response = self.invoice.remind(remind_attributes);

		mock.assert_called_once_with(self.invoice.api,'v1/invoices/invoice/'+self.invoice.id+'/remind', remind_attributes, {'PayPal-Request-Id' : ANY})
		self.assertEqual(response, True)

	@patch('test_helper.paypal.Api.post', autospec=True)
	def test_cancel(self, mock):
		cancel_attributes = {
			'subject': 'Past due',
			'note': 'Canceling invoice',
			'send_to_merchant': True,
			'send_to_payer': True
		}

		response = self.invoice.cancel(cancel_attributes);

		mock.assert_called_once_with(self.invoice.api,'v1/invoices/invoice/'+self.invoice.id+'/cancel', cancel_attributes, {'PayPal-Request-Id' : ANY})
		self.assertEqual(response, True)
