import unittest
import json

from paypalrestsdk.webhooks import WebhookGetRequest
from tests.webhooks.webhook_create_test import create_webhook
from tests.testharness import TestHarness

class WebhookGetTest(TestHarness):

    def testWebhookGetTest(self):
        created_response = create_webhook(self.client)

        request = WebhookGetRequest(created_response.result.id)
        get_response = self.client.execute(request)
        self.assertEqual(200, get_response.status_code)
        self.assertIsNotNone(get_response.result)
        self.assertEqual(created_response.result.id, get_response.result.id)

if __name__ == "__main__":
    unittest.main()
