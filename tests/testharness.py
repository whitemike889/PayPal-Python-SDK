import unittest

from paypalrestsdk.core.environment import PayPalEnvironment
from paypalrestsdk.core.paypal_http_client import PayPalHttpClient
import os

class TestHarness(unittest.TestCase):

    def setUp(self):
        self.environment = PayPalEnvironment(os.getenv("PAYPAL_CLIENT_ID"), os.getenv("PAYPAL_CLIENT_SECRET"), PayPalEnvironment.SANDBOX)
        self.client = PayPalHttpClient(self.environment)
