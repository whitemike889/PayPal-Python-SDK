from paypalrestsdk import BillingPlan
import logging
logging.basicConfig(level=logging.INFO)

history = BillingPlan.all({"status": "CREATED"})

print("List BillingPlan:")
for plan in history.plans:
    print("  -> BillingPlan[%s]" % (plan.id))
