# This class was generated on Thu, 06 Jul 2017 16:03:37 PDT by version 0.01 of Braintree SDK Generator
# invoice_search_request_test.py
# DO NOT EDIT
# @type request
# @json {"Name":"invoice.search","Description":"Lists invoices that match search criteria. In the JSON request body, include a `search` object that specifies the search criteria.","Parameters":[],"RequestType":{"Type":"Search","VariableName":"body","Description":"Invoice search parameters.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Invoices","VariableName":"","Description":"List of merchant invoices. Can include the total invoices count and HATEOAS links for navigation.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/invoicing/search","ExpectedStatusCode":200,"FileSuffix":"Test"}



import unittest

from tests.invoices.request.test_util import createInvoice

from paypalrestsdk.invoices.request import InvoiceSearchRequest
from tests.testharness import TestHarness


class InvoiceSearchRequestTest(TestHarness):

    def testInvoiceSearchRequestTest(self):
        invoice_send_response = createInvoice(self.client)

        request = InvoiceSearchRequest()
        request.requestBody({
            "number": invoice_send_response.result.number
        })

        response = self.client.execute(request)
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.result.invoices))
        self.assertEqual(invoice_send_response.result.id, response.result.invoices[0].id)

if __name__ == "__main__":
    unittest.main()
