import re
import urllib

# Join given url
# == Example
#   api.join_url("example.com", "index.html") # Return "example.com/index.html"
def join_url(url, path):
  return re.sub(r'/?$', re.sub(r'^/?', '/', path), url)


def join_url_params(url, params):
  return url + "?" + urllib.urlencode(params)
