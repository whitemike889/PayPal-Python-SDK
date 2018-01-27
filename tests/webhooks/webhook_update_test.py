import unittest
import json

from paypalrestsdk.webhooks import WebhookUpdateRequest
from tests.webhooks.webhook_create_test import create_webhook
from tests.testharness import TestHarness

class WebhookUpdateTest(TestHarness):
    def testWebhookUpdateTest(self):
        created_response = create_webhook(self.client)

        update_request = WebhookUpdateRequest(created_response.result.id)
        update_request.request_body([{
            "op": "replace",
            "path": "/url",
            "value": "https://example.com/updated_url"
        }])


        updated_response = self.client.execute(update_request)
        self.assertEqual(200, updated_response.status_code)
        self.assertIsNotNone(updated_response.result)
        self.assertEqual("https://example.com/updated_url", updated_response.result.url)

if __name__ == "__main__":
    unittest.main()
