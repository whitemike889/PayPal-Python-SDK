import unittest
import json

from paypalrestsdk.webhooks import WebhookDeleteRequest
from tests.webhooks.webhook_create_test import create_webhook
from tests.testharness import TestHarness

def delete_webhook(client, webhook_id):
    request = WebhookDeleteRequest(webhook_id)

    return client.execute(request)

class WebhookDeleteTest(TestHarness):

    def testWebhookDeleteTest(self):
        created_response = create_webhook(self.client)

        delete_response = delete_webhook(self.client, created_response.result.id)
        self.assertEqual(204, delete_response.status_code)

if __name__ == "__main__":
    unittest.main()
