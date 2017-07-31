# This class was generated on Tue, 18 Jul 2017 12:57:03 PDT by version 0.01 of Braintree SDK Generator
# authorization_void_request.py
# DO NOT EDIT
# @type request
# @json {"Name":"authorization.void","Description":"Voids, or cancels, an authorization, by ID. You cannot void a fully captured authorization.","Parameters":[{"Type":"string","VariableName":"authorization_id","Description":"The ID of the authorization to void.","IsArray":false,"ReadOnly":false,"Required":true,"Properties":null,"Location":"path"}],"RequestType":null,"ResponseType":{"Type":"Authorization","VariableName":"","Description":"An authorization.","IsArray":false,"ReadOnly":false,"Required":false,"Properties":null},"ContentType":"application/json","HttpMethod":"POST","Path":"/v1/payments/authorization/{authorization_id}/void","ExpectedStatusCode":200}



class AuthorizationVoidRequest:
    """
    Voids, or cancels, an authorization, by ID. You cannot void a fully captured authorization.
    """

    def __init__(self, authorization_id):
        self.verb = "POST"
        self.path = "/v1/payments/authorization/{authorization_id}/void?".replace("{authorization_id}", str(authorization_id))
        self.headers = {}
        self.headers["Content-Type"] = "application/json"

    
