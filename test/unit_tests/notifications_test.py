from test_helper import paypal, unittest
from mock import patch, ANY
import zlib
import json


class TestWebhook(unittest.TestCase):

    def setUp(self):
        self.webhook_event_types = [
            {
                "name": "PAYMENT.AUTHORIZATION.CREATED"
            },
            {
                "name": "PAYMENT.AUTHORIZATION.VOIDED"
            }
        ]
        self.webhook_attributes = {
            "url": "https://www.yeowza.com/ppwebhook",
            "event_types": self.webhook_event_types
        }

        self.webhook = paypal.Webhook(self.webhook_attributes)
        self.webhook_id = '6HY79521VR978045E'

    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_create(self, mock):
        response = self.webhook.create()

        mock.assert_called_once_with(self.webhook.api, '/v1/notifications/webhooks/',
                                     self.webhook_attributes, {'PayPal-Request-Id': ANY}, None)
        self.assertEqual(response, True)

    @patch('test_helper.paypal.Api.get', autospec=True)
    def test_get_event_types(self, mock):
        self.webhook.id = self.webhook_id
        event_types = self.webhook.get_event_types()
        mock.assert_called_once_with(
            self.webhook.api, '/v1/notifications/webhooks/' + self.webhook_id + '/event-types')


class TestWebhookEvents(unittest.TestCase):

    def setUp(self):
        self.webhook_event_id = 'WH-1S115631EN580315E-9KH94552VF7913711'
        self.event_body = "{\"id\":\"WH-8UH59159LY570081N-5FX3594634324213T\",\"create_time\":\"2014-10-10T17:36:15Z\",\"resource_type\":\"authorization\",\"event_type\":\"PAYMENT.AUTHORIZATION.CREATED\",\"summary\":\"A successful payment authorization was created for 0.60 USD\",\"resource\":{\"id\":\"2LP967258V024852T\",\"create_time\":\"2014-10-10T17:34:11Z\",\"update_time\":\"2014-10-10T17:35:16Z\",\"amount\":{\"total\":\"0.60\",\"currency\":\"USD\",\"details\":{\"subtotal\":\"0.60\"}},\"payment_mode\":\"INSTANT_TRANSFER\",\"state\":\"authorized\",\"protection_eligibility\":\"ELIGIBLE\",\"protection_eligibility_type\":\"ITEM_NOT_RECEIVED_ELIGIBLE,UNAUTHORIZED_PAYMENT_ELIGIBLE\",\"parent_payment\":\"PAY-6FD94763FB485961SKQ4BREY\",\"valid_until\":\"2014-11-08T17:34:11Z\",\"links\":[{\"href\":\"https://api.sandbox.paypal.com/v1/payments/authorization/2LP967258V024852T\",\"rel\":\"self\",\"method\":\"GET\"},{\"href\":\"https://api.sandbox.paypal.com/v1/payments/authorization/2LP967258V024852T/capture\",\"rel\":\"capture\",\"method\":\"POST\"},{\"href\":\"https://api.sandbox.paypal.com/v1/payments/authorization/2LP967258V024852T/void\",\"rel\":\"void\",\"method\":\"POST\"},{\"href\":\"https://api.sandbox.paypal.com/v1/payments/authorization/2LP967258V024852T/reauthorize\",\"rel\":\"reauthorize\",\"method\":\"POST\"},{\"href\":\"https://api.sandbox.paypal.com/v1/payments/payment/PAY-6FD94763FB485961SKQ4BREY\",\"rel\":\"parent_payment\",\"method\":\"GET\"}]},\"links\":[{\"href\":\"https://api.sandbox.paypal.com/v1/notifications/webhooks-events/WH-8UH59159LY570081N-5FX3594634324213T\",\"rel\":\"self\",\"method\":\"GET\"},{\"href\":\"https://api.sandbox.paypal.com/v1/notifications/webhooks-events/WH-8UH59159LY570081N-5FX3594634324213T/resend\",\"rel\":\"resend\",\"method\":\"POST\"}]}"
        self.transmission_id = "efcfecb0-50a3-11e4-acdb-8d0d8bca8f12"
        self.timestamp = "2014-10-10T17:36:16Z"
        self.webhook_id = "40Y916089Y8324740"
        self.actual_signature = "mcLeCd3PZXLR2DYFbcgf/Fzjk0wAaQ0+awY7en8J3w+UxlE5nzwIQIgHAup+x7cCrEWKzSLNSdAw9OCXb+0Pg030OEhP6iSEBr3XcTrfNXhrjz9Mbl35fe7qY6eOM4lJy2vRYAGGj9X2zXNI4Ag4wUIZlc03QRCkvAedGOkopuHXCepeVVgCEIaB4NCHgLKgjpmRaj6bRXdz1Odlm0BrG6pb7Fjw3cbhbBrw6twZugD8d/fj3juUU63UFGp77RGTxtMdnnAfHwlAQYSWRxiKxQbrE0PFZyICRcXd7hgluIv+ts/hqho4vVMi9UkRXfJCtaJ6o/tjDZjnO9rjMnu++g=="
        self.cert_url = 'https://api.sandbox.paypal.com/v1/notifications/certs/CERT-360caa42-35c2ed1e-21e9a5d6'
        self.expected_signature = self.transmission_id + "|" + self.timestamp + "|" + \
            self.webhook_id + "|" + \
            str(zlib.crc32(self.event_body.encode('utf-8')) & 0xffffffff)

    @patch('test_helper.paypal.Api.get', autospec=True)
    @patch('test_helper.paypal.Api.post', autospec=True)
    def test_find_and_resend(self, mock_post, mock_get):
        webhook_event = paypal.WebhookEvent.find(self.webhook_event_id)
        mock_get.assert_called_once_with(
            webhook_event.api, '/v1/notifications/webhooks-events/' + self.webhook_event_id)
        self.assertTrue(isinstance(webhook_event, paypal.WebhookEvent))
        webhook_event.id = self.webhook_event_id

        response = webhook_event.resend()
        mock_post.assert_called_once_with(
            webhook_event.api, '/v1/notifications/webhooks-events/' + self.webhook_event_id + '/resend', {}, {'PayPal-Request-Id': ANY})
        self.assertEqual(response, True)

    def test_verify(self):
        response = paypal.WebhookEvent.verify(
            self.transmission_id, self.timestamp, self.webhook_id, self.event_body, self.cert_url, self.actual_signature)
        self.assertEqual(response, True)

    def test_get_expected_sig(self):
        expected_sig = paypal.WebhookEvent._get_expected_sig(
            self.transmission_id, self.timestamp, self.webhook_id, self.event_body)
        self.assertEqual(expected_sig, self.expected_signature)

    def test_get_resource(self):
        webhook_event = paypal.WebhookEvent(json.loads(self.event_body))
        event_resource = webhook_event.get_resource()
        self.assertTrue(isinstance(event_resource, paypal.Authorization))

    def test_get_cert(self):
        cert = paypal.WebhookEvent._get_cert(self.cert_url)
        self.assertNotEqual(cert, None)
