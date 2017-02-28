from braintreehttp import DefaultHttpClient
from braintreehttp import Injector
from injector import OAuthInjector


class PayPalHttpClient(DefaultHttpClient):
    def __init__(self, environment, auth_injector=None):
        DefaultHttpClient.__init__(self)
        self.environment = environment
        if auth_injector:
            self.add_injector(auth_injector)
        else:
            auth_injector = OAuthInjector(environment)
            self.add_injector(auth_injector)

        self.add_injector(injector=PayPalHttpClient.PayPalDefaultInjector(environment.base_url))

    class PayPalDefaultInjector(Injector):

        def __init__(self, base_url):
            self.base_url = base_url

        def __call__(self, request):
            if "http" not in request.url:
                request.url = self.base_url() + request.url

            if request.json:
                request.headers["Content-Type"] = "application/json"

            if "Accept-Encoding" not in request.headers:
                request.headers["Accept-Encoding"] = "gzip"

