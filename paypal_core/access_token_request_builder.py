import requests
import base64


class AccessTokenRequestBuilder:

    @staticmethod
    def fetch_access_token(environment, refresh_token=None):
        if refresh_token:
            return AccessTokenRequestBuilder._fetch_access_token_refresh_token(environment, refresh_token)
        else:
            request = AccessTokenRequestBuilder._get_access_token_request(environment, "/v1/oauth2/token")
            request.data = "grant_type=client_credentials"

            return request

    @staticmethod
    def fetch_refresh_token(environment, auth_code):
        request = AccessTokenRequestBuilder._get_access_token_request(environment, "/v1/identity/openidconnect/tokenservice")
        request.data = "grant_type=authorization_code&code=" + auth_code

        return request

    @staticmethod
    def _fetch_access_token_refresh_token(environment, refresh_token):
        request = AccessTokenRequestBuilder._get_access_token_request(environment, "/v1/identity/openidconnect/tokenservice")
        request.data = "grant_type=client_credentials&refresh_token=" + refresh_token

        return request

    @staticmethod
    def _get_access_token_request(environment, path):
        request = requests.Request(method="POST", url=environment.base_url() + path)
        auth_header = base64.b64encode(environment.client_id + ":" + environment.client_secret)
        request.headers["Authorization"] = "Basic " + auth_header
        request.headers["Content-Type"] = "application/x-www-form-urlencoded"

        return request
