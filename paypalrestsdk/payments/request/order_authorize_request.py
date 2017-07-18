# This class was generated on Tue, 18 Jul 2017 12:57:03 PDT by version 0.01 of Braintree SDK Generator
# order_authorize_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"order.authorize","Description":"Authorizes an order, by ID. In the JSON request body, include an `amount` object.","Parameters":[{"Type":"string","VariableName":"order_id","Description":"The ID of the order to authorize.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":{"Type":"Order","VariableName":"body","Description":"An order transaction.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ResponseType":{"Type":"Authorization","VariableName":"","Description":"An authorization.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/orders/{order_id}/authorize","ExpectedStatusCode":200}



class OrderAuthorizeRequest:
    """
    Authorizes an order, by ID. In the JSON request body, include an `amount` object.
    """

    def __init__(self, order_id):
        self.verb = "POST"
        self.path = "/v1/payments/orders/{order_id}/authorize?".replace("{order_id}", str(order_id))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"

    
    
    def requestBody(self, body):
        self.body = body
        return self
