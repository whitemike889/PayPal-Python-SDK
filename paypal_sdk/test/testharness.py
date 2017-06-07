import unittest

from paypal_sdk import PayPalEnvironment
from paypal_sdk import PayPalHttpClient

class TestHarness(unittest.TestCase):

    def setUp(self):
        environment = PayPalEnvironment("client_id", "client_secret", PayPalEnvironment.SANDBOX)
        self.client = PayPalHttpClient(environment)
