# REST SDK

The PayPal REST SDK provides Python APIs to create, process and manage payment.

## Installation

    pip install git+https://github.com/paypal/rest-api-sdk-python.git

## Run Testcase

    python -m unittest discover -s test/ -p '*_test.py'

## Set Log level

    import logging
    logging.basicConfig(level=logging.INFO)

## Example

```python
import paypal
import logging

logging.basicConfig(level=logging.INFO)

paypal.set_config(
  endpoint="https://api.sandbox.paypal.com",
  client_id="EBWKjlELKMYqRNQ6sYvFo64FtaRLRR5BdHEESmha49TM",
  client_secret="EO422dn3gQLgDbuwqTjzrFgFtaRLRR5BdHEESmha49TM")

payment = paypal.Payment({
  "intent": "sale",
  "payer": {
    "payment_method": "credit_card",
    "funding_instruments": [{
      "credit_card": {
        "type": "visa",
        "number": "4417119669820331",
        "expire_month": "11",
        "expire_year": "2018",
        "cvv2": "874",
        "first_name": "Joe",
        "last_name": "Shopper" }}]},
  "transactions": [{
    "amount": {
      "total": "1.00",
      "currency": "USD" },
    "description": "This is the payment transaction description." }]})

if payment.create() :
  print "Payment created successfully"
else:
  print payment.error
