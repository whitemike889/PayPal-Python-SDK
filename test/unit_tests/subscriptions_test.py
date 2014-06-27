from test_helper import paypal, unittest
from mock import patch, ANY
import urlparse


class TestBillingPlan(unittest.TestCase):

    def setUp(self):
        self.billing_plan_attributes = {
            "name": "Fast Speed Plan",
            "description": "Template creation.",
            "type": "fixed",
            "payment_definitions": [
                {
                    "name": "Payment Definition-1",
                    "type": "REGULAR",
                    "frequency": "MONTH",
                    "frequency_interval": "2",
                    "amount": {
                        "value": "100",
                        "currency": "USD"
                    },
                    "cycles": "12",
                    "charge_models": [
                        {
                            "type": "SHIPPING",
                            "amount": {
                                "value": "10",
                                "currency": "USD"
                            }
                        },
                        {
                            "type": "TAX",
                            "amount": {
                                "value": "12",
                                "currency": "USD"
                            }
                        }
                    ]
                }
            ],
            "merchant_preferences": {
                "setup_fee": {
                    "value": "1",
                    "currency": "USD"
                },
                "return_url": "http://www.paypal.com",
                "cancel_url": "http://www.yahoo.com",
                "autobill_amount": "YES",
                "initial_amount_fail_action": "CONTINUE",
                "max_fail_attempts": "0"
            }
        }
        self.billing_plan_update_attributes = [
            {
                "op": "replace",
                "path": "/",
                "value": {
                    "state": "ACTIVE"
                }
            }
        ]
        self.billing_plan = paypal.BillingPlan(self.billing_plan_attributes)
        self.billing_plan.id = 'P-0NJ10521L3680291SOAQIVTQ'

    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_create(self, mock):
        response = self.billing_plan.create()

        mock.assert_called_once_with(self.billing_plan.api, 'v1/payments/billing_plans',
            self.billing_plan_attributes, {'PayPal-Request-Id' : billing_plan.request_id}, None)
        self.assertEqual(response, True)

    @patch('test_helper.paypal.Api.get', autospec=True)
    def test_find(self, mock):
        billing_plan = paypal.BillingPlan.find(self.billing_plan.id)

        mock.assert_called_once_with(self.billing_plan.api, 'v1/payments/billing_plans/' + self.billing_plan.id)
        self.assertTrue(isinstance(billing_plan, paypal.BillingPlan))

    @patch('test_helper.paypal.Api.get', autospec=True)
    def test_all(self, mock):
        mock.return_value = {'plans': [self.billing_plan_attributes]}
        history = paypal.BillingPlan.all({'status': 'CREATED'})

        mock.assert_called_once_with(self.billing_plan.api, 'v1/payments/billing_plans?status=CREATED')
        self.assertEqual(len(self.history.plans), 1)
        self.assertTrue(isinstance(history.plans[0], paypal.BillingPlan))

    @patch('test_helper.paypal.Api.patch', autospec=True)
    def test_replace(self, mock):
        response = self.billing_plan.replace(self.billing_plan_update_attributes)

        mock.assert_called_once_with(self.billing_plan.api, 'v1/payments/billing_plans/' + self.billing_plan.id \
            , self.billing_plan_update_attributes, {'PayPal-Request-Id' : self.billing_plan.request_id}, None))
        self.assertEqual(response, True)

class TestBillingAgreement(unittest.TestCase):

    def setUp(self):
        self.billing_agreement_attributes = {
            "name": "Fast Speed Agreement",
            "description": "Agreement for Fast Speed Plan",
            "start_date": "2015-02-19T00:37:04Z",
            "plan": {
                "id": "P-0NJ10521L3680291SOAQIVTQ"
            },
            "payer": {
                "payment_method": "paypal"
            },
            "shipping_address": {
                "line1": "StayBr111idge Suites",
                "line2": "Cro12ok Street",
                "city": "San Jose",
                "state": "CA",
                "postal_code": "95112",
                "country_code": "US"
            }
        }

        self.billing_agreement_attributes_created = {
            "name": "Fast Speed Agreement",
            "description": "Agreement for Fast Speed Plan",
            "links": [
                {
                    "href": "https://localhost/cgi-bin/webscr?cmd=_express-checkout&token=EC-7MD89916KU283780J",
                    "rel": "approval_url",
                    "method": "REDIRECT"
                },
                {
                    "href": "https://api.sandbox.paypal.com/v1/payments/billing-agreements/EC-7MD89916KU283780J/agreement-execute",
                    "rel": "execute",
                    "method": "POST"
                }
            ],
            "start_date": "2015-02-19T00:37:04Z",
            "plan": {
                "id": "P-0NJ10521L3680291SOAQIVTQ",
                "state": "ACTIVE",
                "name": "Fast Speed Plan",
                "description": "Template creation.",
                "type": "FIXED",
                "payment_definitions": [
                {
                    "id": "PD-0NJ10521L3680291SOAQIVTQ",
                    "name": "Payment Definition-1",
                    "type": "REGULAR",
                    "frequency": "Month",
                    "frequency_interval": "2",
                    "amount": {
                        "value": "100"
                    }
                }],
                "currency_code": "USD"
            }
        }

        self.billing_agreement_update_attributes = [
            {
                "op": "replace",
                "path": "/",
                "value": {
                    "description": "New Description",
                    "name": "New Name",
                    "shipping_address": {
                        "line1": "StayBr111idge Suites",
                        "line2": "Cro12ok Street",
                        "city": "San Jose",
                        "state": "CA",
                        "postal_code": "95112",
                        "country_code": "US"
                    }
                }
            }
        ]

        self.billing_agreement_executed_attributes = {
            "id": "I-THNVHK6X9H0V",
            "links": [{
                "href": "https://api.sandbox.paypal.com/v1/payments/billing-agreements/I-THNVHK6X9H0V",
                "rel": "self",
                "method": "GET"
            }]
        }

        self.billing_agreement = paypal.BillingAgreement(self.billing_agreement_attributes)
        self.billing_agreement.id = "I-THNVHK6X9H0V"

    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_create(self, mock):
        response = self.billing_agreement.create()

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements',
            self.billing_agreement_attributes, {'PayPal-Request-Id' : billing_agreement.request_id}, None)
        self.assertEqual(response, True)

    @patch('test_helper.paypal.Api.get', autospec=True)
    def test_find(self, mock):

        billing_agreement = paypal.BillingAgreement.find(self.billing_agreement.id)

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements/' + self.billing_agreement.id)
        self.assertTrue(isinstance(billing_agreement, paypal.BillingAgreement))

    @patch('test_helper.paypal.Api.patch', autospec=True)
    def test_replace(self, mock):
        response = self.billing_agreement.replace(self.billing_agreement_update_attributes)

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements/' + self.billing_agreement.id \
            , self.billing_agreement_update_attributes, {'PayPal-Request-Id' : self.billing_agreement.request_id}, None))
        self.assertEqual(response, True)

    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_suspend(self, mock):
        suspend_attributes = {
            "note": "Suspending the agreement"
        }
        response = self.billing_agreement.suspend(suspend_attributes)

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements/' + self.billing_agreement.id + '/suspend', \
         suspend_attributes, {'PayPal-Request-Id' : ANY})
        self.assertEqual(response, True)

    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_reactivate(self, mock):
        reactivate_attributes = {
            "note": "Reactivating the agreement"
        }
        response = self.billing_agreement.reactivate(reactivate_attributes)

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements/' + self.billing_agreement.id + '/re-activate', \
         reactivate_attributes, {'PayPal-Request-Id' : ANY})
        self.assertEqual(response, True)

    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_cancel(self, mock):
        cancel_attributes = {
            "note": "Canceling the agreement"
        }
        response = self.billing_agreement.cancel(cancel_attributes)

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements/' + self.billing_agreement.id + '/cancel', \
         cancel_attributes, {'PayPal-Request-Id' : ANY})
        self.assertEqual(response, True)

    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_set_balance(self, mock):
        set_balance_attributes = {
            "value" : "10",
            "currency" : "USD"
        }
        response = self.billing_agreement.set_balance(set_balance_attributes)

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements/' + self.billing_agreement.id + '/set-balance', \
         set_balance_attributes, {'PayPal-Request-Id' : ANY})
        self.assertEqual(response, True)

    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_bill_balance(self, mock):
        bill_balance_attributes = {
            "note": "Billing Balance Amount",
            "amount": {
                "value": "10",
                "currency": "USD"
            }
        }
        response = self.billing_agreement.bill_balance(bill_balance_attributes)

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements/' + self.billing_agreement.id + '/bill-balance', \
         bill_balance_attributes, {'PayPal-Request-Id' : ANY})
        self.assertEqual(response, True)

    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_execute(self, mock):
        response = self.billing_agreement.create()

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements',
            self.billing_agreement_attributes, {'PayPal-Request-Id' : ANY}, None)
        self.assertEqual(response, True)

        self.billing_agreement = self.billing_agreement_attributes_created
        mock.return_value = self.billing_agreement_executed_attributes

        response = billing_agreement.execute()
        # Test that execute actually makes a http post to the href element of links array with id
        execute_url = [link['href'] for link in self.billing_agreement_attributes_created.links if link['rel'] == 'execute'][0]
        execute_url_path = urlparse.urlparse(execute_url).path

        mock.assert_called_with(self.billing_agreement.api, execute_url_path, {}, {'PayPal-Request-Id' : ANY})
        self.assertTrue(isinstance(response, paypal.Resource))

    @patch('test_helper.paypal.Api.get', autospec=True)
    def test_search_transactions(self, mock):
        date_range = {
            "start-date": "2014-07-20",
            "end-date": "2014-07-30"
        }
        mock.return_value = {
            "agreement_transaction_list": [
                {
                    "transaction_id": "I-HT38K76XPMGJ",
                    "status": "Created",
                    "transaction_type": "Recurring Payment",
                    "amount": "",
                    "fee_amount": "",
                    "net_amount": "",
                    "currency_code": "",
                    "payer_email": "",
                    "payer_name": "Jose Ramirez",
                    "time_stamp": "2014-07-29T13:05:48Z",
                    "time_zone": "GMT"
                },
                {
                    "transaction_id": "18972938Y4931603B",
                    "status": "Completed",
                    "transaction_type": "Recurring Payment",
                    "amount": "1.00",
                    "fee_amount": "-0.33",
                    "net_amount": "0.67",
                    "currency_code": "USD",
                    "payer_email": "sai@paypal.com",
                    "payer_name": "Jose Ramirez",
                    "time_stamp": "2014-07-29T13:06:04Z",
                    "time_zone": "GMT"
                }
            ]
        }
        transactions = self.billing_agreement.search_transactions(date_range)

        mock.assert_called_once_with(self.billing_agreement.api, 'v1/payments/billing_agreements/' \
        + self.billing_agreement.id + '/transaction?start-date=2014-07-20&end-date=2014-07-30', {'PayPal-Request-Id' : ANY})
        self.assertEqual(len(transactions.agreement_transaction_list), 2)