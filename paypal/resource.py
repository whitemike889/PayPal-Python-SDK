import paypal.util as util
import paypal.api  as api
import uuid

class Resource(dict):

  convert_resources = {}

  def __init__(self, attributes = {}):
    super(Resource, self).__setattr__('error', None)
    super(Resource, self).__setattr__('headers', {})
    super(Resource, self).__setattr__('header', {})
    super(Resource, self).__setattr__('request_id', None)
    self.merge(attributes)

  def generate_request_id(self):
    if self.request_id == None :
      self.request_id = str(uuid.uuid4())
    return self.request_id

  def http_headers(self):
    return dict(self.header.items() + self.headers.items() +
        { 'PayPal-Request-Id': self.generate_request_id() }.items() )

  def __getattr__(self, name):
    return self.get(name)

  def __setattr__(self, name, value):
    value = self.convert(name, value)
    try:
      # Handle attributes(error, header, request_id)
      super(Resource, self).__getattribute__(name)
      super(Resource, self).__setattr__(name, value)
    except AttributeError:
      self[name] = value

  def success(self):
    return self.error == None

  def merge(self, new_attributes):
    for k in new_attributes:
      self.__setattr__(k, new_attributes[k])

  def convert(self, name, value):
    if isinstance(value, dict):
      klass = self.convert_resources.get(name, Resource)
      return klass(value)
    elif isinstance(value, list):
      new_list = []
      for obj in value:
        new_list.append(self.convert(name, obj))
      return new_list
    else:
      return value


class Find(Resource):
  @classmethod
  def find(klass, resource_id):
    url = util.join_url(klass.path, str(resource_id))
    return klass(api.default().get(url))

class List(Resource):
  list_class = Resource

  @classmethod
  def all(klass, params = None):
    if params == None:
      url = klass.path
    else:
      url = util.join_url_params(klass.path, params)
    return klass.list_class(api.default().get(url))

class Create(Resource):
  def create(self):
    new_attributes = api.default().post(self.path, self, self.http_headers())
    self.error = None
    self.merge(new_attributes)
    return self.success()

class Post(Resource):
  def post(self, name, attributes = {}, klass = Resource):
    url = util.join_url(self.path, str(self['id']))
    url = util.join_url(url, name)
    if not isinstance(attributes, Resource):
      attributes = Resource(attributes)
    new_attributes = api.default().post(url, attributes, attributes.http_headers())
    if isinstance(klass, Resource):
      klass.error = None
      klass.merge(new_attributes)
      return self.success()
    else:
      return klass(new_attributes)
