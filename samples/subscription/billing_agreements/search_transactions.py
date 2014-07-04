from paypalrestsdk import BillingAgreement
import logging

BILLING_AGREEMENT_ID = "I-HT38K76XPMGJ"

try:
    billing_agreement = BillingAgreement.find(BILLING_AGREEMENT_ID)

    date_range = {
        "start-date": "2014-07-01",
        "end-date": "2014-07-20"
    }

    transactions = billing_agreement.search_transactions(date_range)
    for transaction in transactions.agreement_transaction_list:
        print("  -> Transaction[%s]" % (transaction.transaction_id))

    else:
        print(billing_agreement.error)

except ResourceNotFound as error:
    print("Billing Agreement Not Found")
