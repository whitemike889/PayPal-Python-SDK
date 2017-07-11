# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# template_get_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"template.get","Description":"Shows details for a template, by ID.","Parameters":[{"Type":"string","VariableName":"template_id","Description":"The ID of the template for which to show details.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Template","VariableName":"","Description":"Invoicing template.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/invoicing/templates/{template_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.invoices.request import TemplateGetRequest
from paypalrestsdk.test.testharness import TestHarness
from test_util import createTemplate


class TemplateGetRequestTest(TestHarness):

    def testTemplateGetRequestTest(self):
        create_response, cleanup = createTemplate(self.client)

        response = self.client.execute(TemplateGetRequest(create_response.result.template_id))
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        cleanup()

if __name__ == "__main__":
    unittest.main()
