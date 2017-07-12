# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# template_update_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"template.update","Description":"Updates a template, by ID. In the JSON request body, specify a complete `template` object. The update method does not support partial updates.","Parameters":[{"Type":"string","VariableName":"template_id","Description":"The ID of the template to update.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Template","VariableName":"body","Description":"Invoicing template.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Template","VariableName":"","Description":"Invoicing template.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"PUT","Path":"/v1/invoicing/templates/{template_id}","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.invoices.request.test_util import createTemplate, invoice_template_attributes

from paypalrestsdk.invoices.request import TemplateUpdateRequest
from tests.testharness import TestHarness


class TemplateUpdateRequestTest(TestHarness):

    def testTemplateUpdateRequestTest(self):
        create_response, cleanup = createTemplate(self.client)

        request = TemplateUpdateRequest(create_response.result.template_id)
        request.body(invoice_template_attributes())

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        cleanup()

if __name__ == "__main__":
    unittest.main()
