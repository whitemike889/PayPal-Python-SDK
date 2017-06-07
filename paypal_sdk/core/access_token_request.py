from braintreehttp import HttpRequest


class AccessTokenRequest(HttpRequest):

    def __init__(self, paypal_environment, refresh_token=None):
        path = "/v1/oauth2/token"
        body = "grant_type=client_credentials"
        if refresh_token:
            path = "/v1/identity/openidconnect/tokenservice"
            body += "&refresh_token={0}".format(refresh_token)

        HttpRequest.__init__(self, path, "POST", request_body=body)
        self.headers["Content-Type"] = "application/x-www-form-urlencoded"
        self.headers["Authorization"] = paypal_environment.authorization_string()
