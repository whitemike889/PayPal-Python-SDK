from paypalrestsdk import BillingPlan
import logging

logging.basicConfig(level=logging.INFO)

billing_plan = BillingPlan({
    "name": "Fast Speed Plan",
    "description": "Template creation.",
    "type": "fixed",
    "payment_definitions": [
        {
            "name": "Payment Definition-1",
            "type": "REGULAR",
            "frequency": "MONTH",
            "frequency_interval": "2",
            "amount": {
                "value": "100",
                "currency": "USD"
            },
            "cycles": "12",
            "charge_models": [
                {
                    "type": "SHIPPING",
                    "amount": {
                        "value": "10",
                        "currency": "USD"
                    }
                },
                {
                    "type": "TAX",
                    "amount": {
                        "value": "12",
                        "currency": "USD"
                    }
                }
            ]
        }
    ],
    "merchant_preferences": {
        "setup_fee": {
            "value": "1",
            "currency": "USD"
        },
        "return_url": "http://www.paypal.com",
        "cancel_url": "http://www.yahoo.com",
        "autobill_amount": "YES",
        "initial_amount_fail_action": "CONTINUE",
        "max_fail_attempts": "0"
    }
})

if billing_plan.create():
  print("Billing Plan [%s] created successfully"%(billing_plan.id))
else:
  print(billing_plan.error)
