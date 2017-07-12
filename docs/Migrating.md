# Migrating from Version 1 to Version 2

## 1. Initialize SDK

#### BEFORE
```py
paypalrestsdk.configure(client_id, client_secret)
```

#### AFTER
```py
env = paypalrestsdk.PayPalEnvironment(client_id, client_secret, mode=paypalrestsdk.PayPalEnvironment.SANDBOX)
                                      
client = paypalrestsdk.PayPalHttpClient(environment=env)
```

# 2. Make a call

#### BEFORE
```py
from paypalrestsdk import Payment

payment = Payment({
    "payer": {
        "payment_method": "paypal"
    },
    "intent": "sale",
    ...
  })
  
if payment.create():
    print("Payment[%s] created successfully" % (payment.id))
else:
    print("Error while creating payment:")
    print(payment.error)
```

#### AFTER
```py
payment_create_request = paypalrestsdk.PaymentCreateRequest()
payment_create_request.body({
    "payer": {
        "payment_method": "paypal"
    },
    "intent": "sale",
    ...
})

try:
    payment_create_response = client.execute(payment_create_request)
    payment = payment_create_response.result
    print("Payment[%s] created successfully" % (payment.id))
except IOError as ioe:
    print("Error while creating payment:")
    print(ioe)
```

