# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_get_all_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.get_all","Description":"Lists merchant invoices. To filter the invoices that appear in the response, you can specify one or more optional query parameters.","Parameters":[{"Type":"integer","VariableName":"page","Description":"A *zero-relative* index of the list of merchant invoices.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"integer","VariableName":"page_size","Description":"The number of invoices to list beginning with the specified `page`.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null,"Location":"query"},{"Type":"boolean","VariableName":"total_count_required","Description":"Indicates whether the total count appears in the response. Default is `false`.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null,"Location":"query"}],"RequestType":null,"ResponseType":{"Type":"Invoices","VariableName":"","Description":"List of merchant invoices. Can include the total invoices count and HATEOAS links for navigation.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"GET","Path":"/v1/invoicing/invoices/","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.invoices.request.test_util import createInvoice

from paypalrestsdk.invoices.request import InvoiceGetAllRequest
from tests.testharness import TestHarness


class InvoiceGetAllRequestTest(TestHarness):

    def testInvoiceGetAllRequestTest(self):
        createInvoice(self.client)

        request = InvoiceGetAllRequest()
        request.page(0)
        request.pageSize(1)
        request.totalCountRequired(True)

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.result)

        self.assertTrue(response.result.total_count > 0)
        self.assertTrue(len(response.result.invoices) == 1)

if __name__ == "__main__":
    unittest.main()
