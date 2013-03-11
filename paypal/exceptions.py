
class ConnectionError(Exception):
  def __init__(self, response, content = None, message = None):
    self.response = response
    self.content  = content
    self.message  = message

  def __str__(self):
    message = "Failed."
    if hasattr(self.response, 'status'):
      message = message + "  Response status = %s."%(self.response.status)
    if hasattr(self.response, 'reason'):
      message = message + "  Response message = %s."%(self.response.reason)
    return message

# Raised when a Timeout::Error occurs.
class TimeoutError(ConnectionError):
  def __init__(message):
    self.message = message

  def __str__(self):
    return self.message

# Raised when a OpenSSL::SSL::SSLError occurs.
class SSLError(ConnectionError):
  def __init__(message):
    self.message = message

  def __str__(self):
    return self.message

# 3xx Redirection
class Redirection(ConnectionError):
  def __str__(self):
    message = super(Redirection, self).__str__()
    if self.response.get('Location'):
      message = "%s => %s"%(message, self.response.get('Location'))
    return message

class MissingParam(TypeError):
  None

class MissingConfig(Exception):
  None

# 4xx Client Error
class ClientError(ConnectionError):
  None

# 400 Bad Request
class BadRequest(ClientError):
  None

# 401 Unauthorized
class UnauthorizedAccess(ClientError):
  None

# 403 Forbidden
class ForbiddenAccess(ClientError):
  None

# 404 Not Found
class ResourceNotFound(ClientError):
  None

# 409 Conflict
class ResourceConflict(ClientError):
  None

# 410 Gone
class ResourceGone(ClientError):
  None

# 5xx Server Error
class ServerError(ConnectionError):
  None

# 405 Method Not Allowed
class MethodNotAllowed(ClientError):
  def allowed_methods(self):
    return self.response['Allow']
