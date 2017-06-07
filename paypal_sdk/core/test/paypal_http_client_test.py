import unittest
import responses
import base64
import json

from braintreehttp import HttpRequest
from braintreehttp import HttpResponse
from paypal_sdk.core import PayPalHttpClient
from paypal_sdk.core.test import PayPalTestHarness


class PayPalHttpClientTest(PayPalTestHarness):

    def setUp(self):
        self.client = PayPalHttpClient(self.environment())

    @responses.activate
    def testPayPalHttpClient_execute_fetchesAccessTokenIfNone(self):
        request = HttpRequest("/", "POST")
        self.stubrequest(request)
        self.stubaccesstokenrequest()

        self.client.execute(request)

        self.assertEqual(2, len(responses.calls))

        accesstokenrequest = responses.calls[0].request
        self.assertEqual(self.environment().base_url() + "/v1/oauth2/token", accesstokenrequest.url)
        self.assertEqual("application/x-www-form-urlencoded", accesstokenrequest.headers["Content-Type"])

        expectedauthheader ="Basic {0}".format(base64.b64encode("{0}:{1}".format(self.environment().client_id, self.environment().client_secret)))
        self.assertEqual(expectedauthheader, accesstokenrequest.headers["Authorization"])
        self.assertEqual("grant_type=client_credentials", accesstokenrequest.body)

    @responses.activate
    def testPayPalHttpClient_execute_fetchesAccessTokenIfExpired(self):
        request = HttpRequest("/", "POST")
        self.stubrequest(request)

        self.client._access_token = self.simpleaccesstoken()
        self.client._access_token.expires_in = 0

        self.stubaccesstokenrequest()

        self.client.execute(request)

        self.assertEqual(2, len(responses.calls))

        accesstokenrequest = responses.calls[0].request
        self.assertEqual(self.environment().base_url() + "/v1/oauth2/token", accesstokenrequest.url)

    @responses.activate
    def testPayPalHttpClient_withRefreshToken_fetchesAccessTokenWithRefreshToken(self):
        request = HttpRequest("/", "POST")
        self.stubrequest(request)

        self.client = PayPalHttpClient(self.environment(), refresh_token="refresh-token")

        self.stubaccesstokenrequest(refresh_token="refresh-token")

        self.client.execute(request)

        self.assertEqual(2, len(responses.calls))

        accesstokenrequest = responses.calls[0].request
        self.assertEqual(self.environment().base_url() + "/v1/identity/openidconnect/tokenservice", accesstokenrequest.url)
        self.assertEqual("application/x-www-form-urlencoded", accesstokenrequest.headers["Content-Type"])

        expectedauthheader ="Basic {0}".format(base64.b64encode("{0}:{1}".format(self.environment().client_id, self.environment().client_secret)))
        self.assertEqual(expectedauthheader, accesstokenrequest.headers["Authorization"])
        self.assertEqual("grant_type=client_credentials&refresh_token=refresh-token", accesstokenrequest.body)

    @responses.activate
    def testPayPalHttpClient_execute_setsCommonHeaders_and_signsRequest(self):
        self.client._access_token = self.simpleaccesstoken()

        request = HttpRequest("/", "POST")
        self.stubrequest(request)

        self.client.execute(request)

        self.assertEqual(len(responses.calls), 1)

        actualrequest = responses.calls[0].request
        self.assertEquals(actualrequest.headers["Accept-Encoding"], "gzip")
        self.assertEquals(actualrequest.headers["Authorization"], "Bearer sample-access-token")

    @responses.activate
    def testPayPalHttpClient_execute_serializesDataWhenPresentAndContentTypeSet(self):
        self.client._access_token = self.simpleaccesstoken()

        body = {"some-key": "some-value"}
        request = HttpRequest("/", "POST", body)
        request.headers["Content-Type"] = "application/json"
        self.stubrequest(request)

        self.client.execute(request)

        self.assertEqual(1, len(responses.calls))

        actualrequest = responses.calls[0].request

        self.assertEqual(json.dumps(body), actualrequest.body)

    @responses.activate
    def testPayPalHttpClient_execute_withRequestBody_contentTypeNotPresent_throws(self):
        self.client._access_token = self.simpleaccesstoken()

        request = HttpRequest("/", "POST", {"some-key", "some-value"})
        self.stubrequest(request)

        try:
            self.client.execute(request)
            self.fail("expected IOError")
        except IOError as ioe:
            self.assertTrue("Unable to serialize content" in ioe.message)

    @responses.activate
    def testPayPalHttpClient_execute_withRequestBody_contentTypeNotJson(self):
        self.client._access_token = self.simpleaccesstoken()

        request = HttpRequest("/", "POST", {"some-key", "some-value"})
        request.headers["Content-Type"] = "application/xml"
        self.stubrequest(request)

        try:
            self.client.execute(request)
            self.fail("expected IOError")
        except IOError as ioe:
            self.assertTrue("Unable to serialize content" in ioe.message)

    @responses.activate
    def testPayPalHttpClient_execute_whenResponseBodyAndContentTypePresent_deserializesResponse(self):
        self.client._access_token = self.simpleaccesstoken()

        request = HttpRequest("/", "POST")
        response_body = json.dumps({"some-key": "some-value"})
        response = HttpResponse(response_body, 200, {"Content-Type": "application/json"})

        self.stubrequest(request, response)

        actualresponse = self.client.execute(request)
        self.assertEqual("some-value", actualresponse.result.some_key)

    @responses.activate
    def testPayPalHttpClient_execute_whenResponseBodyAndContentTypeNotPresent_throws(self):
        self.client._access_token = self.simpleaccesstoken()

        request = HttpRequest("/", "POST")
        response_body = json.dumps({"some-key": "some-value"})
        response = HttpResponse(response_body, 200)

        self.stubrequest(request, response)

        try:
            self.client.execute(request)
            self.fail("expected IOError")
        except IOError as ioe:
            self.assertTrue("Unsupported Content-Type" in ioe.message)

    @responses.activate
    def testPayPalHttpClient_execute_whenResponseBodyAndContentTypeNotJson_throws(self):
        self.client._access_token = self.simpleaccesstoken()

        request = HttpRequest("/", "POST")
        response_body = json.dumps({"some-key": "some-value"})
        response = HttpResponse(response_body, 200, {"Content-Type": "application/xml"})

        self.stubrequest(request, response)

        try:
            self.client.execute(request)
            self.fail("expected IOError")
        except IOError as ioe:
            self.assertTrue("Unsupported Content-Type: application/xml" in ioe.message)

if __name__ == '__main__':
    unittest.main()
