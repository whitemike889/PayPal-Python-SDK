import httplib2, base64, json
import paypal.util as util
import logging

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
      token_hash = self.request(util.join_url(self.token_endpoint, "/v1/oauth2/token"), "POST",
        body = "response_type=token&grant_type=client_credentials",
        headers = { "Authorization": ("Basic %s" % self.basic_auth()), "Accept": "application/json" } )
      self.token = token_hash['access_token']
    return self.token

  # Make HTTP call and Format Response
  # == Example
  #   api.request("https://api.sandbox.paypal.com/v1/payments/payment?count=10", "GET")
  #   api.request("https://api.sandbox.paypal.com/v1/payments/payment", "POST", "{}" )
  def request(self, url, method, body = None, headers = None):
    http = httplib2.Http(**self.ssl_options)
    headers = headers or self.headers()

    logging.info('Request[%s]: %s'%(method, url))
    response, data = http.request(url, method, body= body, headers= headers)
    logging.info('Response[%d]: %s'%(response.status, response.reason))

    if(response.status >= 200 and response.status <= 299):
      return json.loads(data)

    elif(response.status == 400 and response['content-type'] == "application/json"): # Format Response error message
      return { "error": json.loads(data) }

    elif(response.status == 401 and self.token and self.client_id): # Handle Expire token
      self.token = None
      return self.request(url, method, body)

    else: # Raise Exception
      raise Exception(response.reason)

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
  def get(self, action):
    return self.request(util.join_url(self.endpoint, action), 'GET' )

  # Make POST request
  # == Example
  #   api.post("v1/payments/payment", { 'indent': 'sale' })
  #   api.post("v1/payments/payment/PAY-1234/execute", { 'payer_id': '1234' })
  def post(self, action, params = {}):
    return self.request(util.join_url(self.endpoint, action), 'POST', body= json.dumps(params) )

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
