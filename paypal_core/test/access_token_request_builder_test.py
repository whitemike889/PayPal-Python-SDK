import unittest
import responses
from unit_test_utils import OPENID_CONNECT_PATH, OAUTH_PATH
from paypal_core import *

env = PayPalEnvironment("clientId", "clientSecret", "http://localhost")


class TokenServiceTest(unittest.TestCase):

    @responses.activate
    def testTokenService_fetchAccessToken(self):
        request = AccessTokenRequestBuilder.fetch_access_token(env)

        self.assertTrue(request.url.endswith(OAUTH_PATH))
        self.assertTrue(request.headers["Authorization"].startswith("Basic "))
        self.assertEqual(request.headers["Content-Type"], "application/x-www-form-urlencoded")
        self.assertEqual(request.data, "grant_type=client_credentials")

    @responses.activate
    def testTokenService_fetchAccessToken_refreshToken_fetchesAccessToken(self):
        request = AccessTokenRequestBuilder.fetch_access_token(env, refresh_token="refresh-token")

        self.assertTrue(request.url.endswith(OPENID_CONNECT_PATH))
        self.assertTrue(request.headers["Authorization"].startswith("Basic "))
        self.assertEqual(request.headers["Content-Type"], "application/x-www-form-urlencoded")
        self.assertEqual(request.data, "grant_type=client_credentials&refresh_token=refresh-token")

    @responses.activate
    def testTokenService_fetchesRefreshToken_and_deserializes(self):
        request = AccessTokenRequestBuilder.fetch_refresh_token(env, "sample_authorization_code")

        self.assertTrue(request.url.endswith(OPENID_CONNECT_PATH))
        self.assertTrue(request.headers["Authorization"].startswith("Basic "))
        self.assertEqual(request.headers["Content-Type"], "application/x-www-form-urlencoded")
        self.assertEqual(request.data, "grant_type=authorization_code&code=sample_authorization_code")


if __name__ == '__main__':
    unittest.main()
