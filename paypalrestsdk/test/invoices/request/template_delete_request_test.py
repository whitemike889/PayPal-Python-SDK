# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# template_delete_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"template.delete","Description":"Deletes a template, by ID.","Parameters":[{"Type":"string","VariableName":"template_id","Description":"The ID of the template to delete.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":null,"ContentType":"application/json","HttpMethod":"DELETE","Path":"/v1/invoicing/templates/{template_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from paypalrestsdk.invoices.request import TemplateDeleteRequest
from paypalrestsdk.test.testharness import TestHarness
from test_util import deleteTemplate, createTemplate


class TemplateDeleteRequestTest(TestHarness):

    def testTemplateDeleteRequestTest(self):
        create_response, _ = createTemplate(self.client)

        response = deleteTemplate(self.client, create_response.result.template_id)

        self.assertEqual(204, response.status_code)
        self.assertIsNone(response.result)

if __name__ == "__main__":
    unittest.main()
