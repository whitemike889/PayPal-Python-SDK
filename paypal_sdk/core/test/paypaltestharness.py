import json

from braintreehttp import TestHarness
from braintreehttp import HttpResponse
from paypal_sdk.core.access_token import AccessToken
from paypal_sdk.core.environment import PayPalEnvironment
from paypal_sdk.core.access_token_request import AccessTokenRequest

OAUTH_PATH = "/v1/oauth2/token"
OPENID_CONNECT_PATH = "/v1/identity/openidconnect/tokenservice"


class PayPalTestHarness(TestHarness):

    def environment(self):
        return PayPalEnvironment("client-id", "client-secret", "http://localhost")

    def stubaccesstokenrequest(self, refresh_token=None, access_token_json=None):
        if not access_token_json:
            access_token_json = self.access_token_response()

        request = AccessTokenRequest(self.environment(), refresh_token)
        response = HttpResponse(json.dumps(access_token_json), 200, {"Content-Type": "application/json"})

        self.stubrequest(request, response)

    def simpleaccesstoken(self):
        return AccessToken("sample-access-token", 3600, "Bearer")

    def access_token_response(self, refresh_token=None):
        at = self.simpleaccesstoken()
        resp = {
            "access_token": at.access_token,
            "expires_in": at.expires_in,
            "token_type": at.token_type
        }
        if refresh_token:
            resp["refresh_token"] = refresh_token

        return resp
