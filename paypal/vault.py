from paypal.resource import Find, Create

class CreditCard(Find, Create):

  path = "v1/vault/credit-card"
