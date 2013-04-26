from test_helper import unittest, paypal, client_id
from paypalrestsdk.openid_connect import Tokeninfo, Userinfo, authorize_url, logout_url


class TestTokeninfo(unittest.TestCase):

  def test_create(self):
    self.assertRaises(paypal.BadRequest, Tokeninfo.create, {})

  def test_userinfo(self):
    self.assertRaises(paypal.UnauthorizedAccess, Tokeninfo().userinfo, {})

  def test_refresh(self):
    self.assertRaises(paypal.BadRequest, Tokeninfo().refresh, {})

  def test_create_with_refresh_token(self):
    self.assertRaises(paypal.BadRequest, Tokeninfo.create_with_refresh_token, {})

class TestUserinfo(unittest.TestCase):

  def test_get(self):
    self.assertRaises(paypal.UnauthorizedAccess, Userinfo.get, "invalid")

class TestUrls(unittest.TestCase):

  def test_authorize_url(self):
    url = authorize_url()
    self.assertRegexpMatches(url, 'response_type=code')
    self.assertRegexpMatches(url, 'scope=openid')
    self.assertRegexpMatches(url, 'client_id=%s'%(client_id))

  def test_authorize_url_options(self):
    url = authorize_url({ 'scope': 'openid profile' })
    self.assertRegexpMatches(url, 'scope=openid\+profile')

  def test_authorize_url_using_tokeninfo(self):
    url = Tokeninfo.authorize_url({ 'scope': 'openid profile' })
    self.assertRegexpMatches(url, 'scope=openid\+profile')

  def test_logout_url(self):
    url = logout_url()
    self.assertRegexpMatches(url, 'logout=true')

  def test_logout_url_options(self):
    url = logout_url({'id_token': '1234'})
    self.assertRegexpMatches(url, 'id_token=1234')

  def test_logout_url_using_tokeninfo(self):
    url = Tokeninfo({'id_token': '1234'}).logout_url()
    self.assertRegexpMatches(url, 'id_token=1234')

