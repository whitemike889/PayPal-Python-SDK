import logging, os, paypal

# Logging
logging.basicConfig(level=logging.DEBUG)

# Credential
client_id     = os.environ['PAYPAL_CLIENT_ID']
client_secret = os.environ['PAYPAL_CLIENT_SECRET']

# Set credential for default api
paypal.set_config( client_id= client_id, client_secret= client_secret )
