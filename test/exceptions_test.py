import unittest
from httplib2 import Response
from paypalrestsdk.exceptions import *
'''
class TestExceptions(unittest.TestCase):

  def test_connection(self):
    error = ConnectionError({})
    self.assertEqual(str(error), "Failed.")

  def test_timeout(self):
    error = TimeoutError("HTTP Timeout")
    self.assertEqual(str(error), "HTTP Timeout")

  def test_ssl_error(self):
    error = SSLError("SSL Error")
    self.assertEqual(str(error), "SSL Error")

  def test_redirect(self):
    error = Redirection({ "Location": "http://example.com" })
    self.assertEqual(str(error), "Failed. => http://example.com")

  def test_not_found(self):
    response = Response({ "status": 404, "reason": "Not Found" })
    error = ResourceNotFound(response)
    self.assertEqual(str(error), "Failed.  Response status = 404.  Response message = %s."%(response.reason))

  def test_unauthorized_access(self):
    response = Response({ "status": 401, "reason": "Unauthorized" })
    error = UnauthorizedAccess(response)
    self.assertEqual(str(error), "Failed.  Response status = 401.  Response message = %s."%(response.reason))

  def test_missing_param(self):
    error = MissingParam("Missing Payment Id")
    self.assertEqual(str(error), "Missing Payment Id")

  def test_missing_config(self):
    error = MissingParam("Missing client_id")
    self.assertEqual(str(error), "Missing client_id")

'''