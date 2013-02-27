import paypal.util as util
import unittest

class Util(unittest.TestCase):

  def test_join_url(self):
    url = util.join_url("payment", "1")
    self.assertEqual(url, "payment/1")
    url = util.join_url("payment/", "1")
    self.assertEqual(url, "payment/1")
    url = util.join_url("payment", "/1")
    self.assertEqual(url, "payment/1")
    url = util.join_url("payment/", "/1")
    self.assertEqual(url, "payment/1")

  def test_join_url_params(self):
    url = util.join_url_params("payment", { "count": 1 })
    self.assertEqual(url, "payment?count=1")
    url = util.join_url_params("payment", { "count": 1, "next_id": 4321 })
    self.assertEqual(url, "payment?count=1&next_id=4321")

