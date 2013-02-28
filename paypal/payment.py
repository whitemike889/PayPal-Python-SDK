import paypal.api  as api
import paypal.util as util

class Payment:

  path = "v1/payments/payment"

  def __init__(self, attributes = {}):
    self.attributes = dict(attributes.items())

  def success(self):
    return self.attributes.get('error') == None

  def merge(self, new_attributes):
    self.attributes = dict(self.attributes.items() + new_attributes.items())

  # == Example
  #   payment = Payment({'intent': 'sale', ... })
  #   payment.create()    # return True or False
  def create(self):
    new_attributes = api.default().post(self.path, self.attributes)
    self.attributes['error'] = None
    self.merge(new_attributes)
    return self.success()

  # == Example
  #   payment = Payment.find("PAY-1234")
  #   payment.execute({ 'payer_id': 1234 }) # return True or False
  def execute(params):
    url = util.join_url(Payment.path, str(self.attributes['id']))
    url = util.join_url(url, 'execute')
    new_attributes = api.default().post(url, params)
    self.attributes['error'] = None
    self.merge(new_attributes)
    return self.success()

  def __str__(self):
    return "Payment("+str(self.attributes)+")"

  # == Example
  #   Payment.find("PAY-1234")  # return Payment object
  @staticmethod
  def find(payment_id):
    url = util.join_url(Payment.path, str(payment_id))
    return Payment(api.default().get(url))

  # == Example
  #   Payment.all({'count': 10})  # return payment histroy hash
  @staticmethod
  def all(params = {}):
    url = util.join_url_params(Payment.path, params)
    return api.default().get(url)

