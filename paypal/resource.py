import paypal.util as util
import paypal.api  as api

class Resource(object):
  def __init__(self, attributes = {}):
    self.super_set('attributes', dict(attributes.items()))

  def super_set(self, name, value):
    super(Resource, self).__setattr__(name, value)

  def __getattr__(self, name):
    return self.attributes.get(name)

  def __setattr__(self, name, value):
    self.attributes[name] = value

  def __str__(self):
    return "%s(%s)"%(self.__class__.__name__, str(self.attributes))

  def success(self):
    return self.attributes.get('error') == None

  def merge(self, new_attributes):
    self.super_set('attributes', dict(self.attributes.items() + new_attributes.items()))


class Find(Resource):
  @classmethod
  def find(klass, resource_id):
    url = util.join_url(klass.path, str(resource_id))
    return klass(api.default().get(url))

class List(Resource):
  @classmethod
  def all(klass, params = None):
    if params == None:
      url = klass.path
    else:
      url = util.join_url_params(klass.path, params)
    return Resource(api.default().get(url))

class Create(Resource):
  def create(self):
    new_attributes = api.default().post(self.path, self.attributes)
    self.attributes['error'] = None
    self.merge(new_attributes)
    return self.success()

class Post(Resource):
  def self_post(self, name, attributes = {}):
    url = util.join_url(Payment.path, str(self.attributes['id']))
    url = util.join_url(url, name)
    new_attributes = api.default().post(url, params)
    self.attributes['error'] = None
    self.merge(new_attributes)
    return self.success()

  def post(self, name, attributes = {}, klass = Resource):
    url = util.join_url(Payment.path, str(self.attributes['id']))
    url = util.join_url(url, name)
    new_attributes = api.default().post(url, params)
    return klass(new_attributes)
