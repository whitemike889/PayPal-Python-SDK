## Example

```python
import paypal

paypal.set_config(
  client_id="CLIENT_ID",
  client_secret="CLIENT_SECRET")

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
```
