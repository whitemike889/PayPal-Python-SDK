import paypal.util as util
import paypal.api  as api

class Resource(dict):

  convert_resources = {}

  def __init__(self, attributes = {}):
    self.merge(attributes)

  def __getattr__(self, name):
    return self.get(name)

  def __setattr__(self, name, value):
    self[name] = self.convert(name, value)

  def success(self):
    return self.get('error') == None

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
    new_attributes = api.default().post(self.path, self)
    self['error'] = None
    self.merge(new_attributes)
    return self.success()

class Post(Resource):
  def self_post(self, name, attributes = {}):
    url = util.join_url(self.path, str(self['id']))
    url = util.join_url(url, name)
    new_attributes = api.default().post(url, attributes)
    self['error'] = None
    self.merge(new_attributes)
    return self.success()

  def post(self, name, attributes = {}, klass = Resource):
    url = util.join_url(self.path, str(self['id']))
    url = util.join_url(url, name)
    new_attributes = api.default().post(url, attributes)
    return klass(new_attributes)
