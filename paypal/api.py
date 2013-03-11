import httplib2, base64, json
import paypal.util as util
import logging, datetime
from paypal.exceptions import *

class Api:

  # Create API object
  # == Example
  #   import paypal
  #   api = paypal.Api( mode="sandbox", client_id='CLIENT_ID', client_secret='CLIENT_SECRET', ssl_options={} )
  def __init__(self, **args):
    self.mode           = args.get("mode", "sandbox")
    self.endpoint       = args.get("endpoint", self.default_endpoint())
    self.token_endpoint = args.get("token_endpoint", self.endpoint)
    self.client_id      = args.get("client_id")
    self.client_secret  = args.get("client_secret")
    self.token          = args.get("token")
    self.ssl_options    = args.get("ssl_options", {})

  # Default endpoint
  def default_endpoint(self):
    if self.mode == "live" :
      return "https://api.paypal.com"
    else:
      return "https://api.sandbox.paypal.com"

  # Find basic auth
  def basic_auth(self):
    return base64.encodestring('%s:%s' % (self.client_id, self.client_secret)).replace('\n', '')

  # Generate token
  def get_token(self):
    if self.token == None :
      token_hash = self.http_call(util.join_url(self.token_endpoint, "/v1/oauth2/token"), "POST",
        body = "response_type=token&grant_type=client_credentials",
        headers = { "Authorization": ("Basic %s" % self.basic_auth()), "Accept": "application/json" } )
      self.token = token_hash['access_token']
    return self.token

  # Make HTTP call and Format Response
  # == Example
  #   api.request("https://api.sandbox.paypal.com/v1/payments/payment?count=10", "GET", {})
  #   api.request("https://api.sandbox.paypal.com/v1/payments/payment", "POST", "{}", {} )
  def request(self, url, method, body = None, headers = {}):

    http_headers = dict(self.headers().items() + headers.items())

    if http_headers.get('PayPal-Request-Id'):
      logging.info('PayPal-Request-Id: %s'%(http_headers['PayPal-Request-Id']))

    try:
      return self.http_call(url, method, body= body, headers= http_headers)

    # Format Error message for bad request
    except BadRequest as error:
      return { "error": json.loads(error.content) }

    # Handle Exipre token
    except UnauthorizedAccess as error:
      if(self.token and self.client_id):
        self.token = None
        return self.request(url, method, body, headers)
      else:
        raise error

  # Make http Call
  def http_call(self, url, method, **args):
    logging.info('Request[%s]: %s'%(method, url))
    http = httplib2.Http(**self.ssl_options)
    start_time = datetime.datetime.now()
    response, content = http.request(url, method, **args)
    duration   = datetime.datetime.now() - start_time
    logging.info('Response[%d]: %s, Duration: %s.%ss'%(response.status, response.reason, duration.seconds, duration.microseconds))
    return self.handle_response(response, content)

  # Validate HTTP response
  def handle_response(self, response, content):
    status = response.status
    if status in [ 301, 302, 303, 307 ] :
      raise Redirection(response, content)
    elif status >= 200 and status <= 299 :
      return json.loads(content)
    elif status == 400 :
      raise BadRequest(response, content)
    elif status == 401 :
      raise UnauthorizedAccess(response, content)
    elif status == 403 :
      raise ForbiddenAccess(response, content)
    elif status == 404 :
      raise ResourceNotFound(response, content)
    elif status == 405 :
      raise MethodNotAllowed(response, content)
    elif status == 409 :
      raise ResourceConflict(response, content)
    elif status == 410 :
      raise ResourceGone(response, content)
    elif status == 422 :
      raise ResourceInvalid(response, content)
    elif status >= 401 and status <= 499 :
      raise ClientError(response, content)
    elif status >= 500 and status <= 599 :
      raise ServerError(response, content)
    else:
      raise ConnectionError(response, content, "Unknown response code: #{response.code}")

  # Default HTTP headers
  def headers(self):
    return { "Authorization": ("Bearer %s" % self.get_token()),
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "PayPalSDK/rest-sdk-python" }

  # Make GET request
  # == Example
  #   api.get("v1/payments/payment?count=1")
  #   api.get("v1/payments/payment/PAY-1234")
  def get(self, action, headers = {}):
    return self.request(util.join_url(self.endpoint, action), 'GET', headers = headers)

  # Make POST request
  # == Example
  #   api.post("v1/payments/payment", { 'indent': 'sale' })
  #   api.post("v1/payments/payment/PAY-1234/execute", { 'payer_id': '1234' })
  def post(self, action, params = {}, headers = {}):
    return self.request(util.join_url(self.endpoint, action), 'POST', body= json.dumps(params), headers = headers )

global __api__
__api__ = None

# Get default api
def default():
  global __api__
  if __api__ is None :
    __api__ = Api()
  return __api__

# Create new default api object with given configuration
def set_config(**config):
  global __api__
  __api__ = Api(**config)
  return __api__
