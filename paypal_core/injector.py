from braintreehttp import Injector
from braintreehttp import DefaultHttpClient
from access_token_request_builder import AccessTokenRequestBuilder


class OAuthInjector(Injector):
    def __init__(self, environment, refresh_token=None):
        self.environment = environment
        self.refresh_token = refresh_token
        self.http_client = DefaultHttpClient()
        self.access_token = None

    def __call__(self, r):
        if not self.access_token or self.access_token.is_expired():
            self.access_token = self._fetch_token()

        r.headers["Authorization"] = "Bearer " + self.access_token.access_token

        return r

    def _fetch_token(self):
        request = AccessTokenRequestBuilder.fetch_access_token(self.environment, self.refresh_token)
        response = self.http_client.execute(request)

        return response.result
