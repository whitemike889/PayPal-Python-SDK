PayPal Python SDK release notes
============================

v1.2.0
-----
* Subscription (Billing Plan and Billing Agreement) API supported

v1.1.0
-----
* Invoicing API support added 
* Added tests and samples for using the invoicing api via the sdk
* PayPal Mobile Backend sample added

v1.0.0
-----
* Future Payments support added along with tests and samples
* Move from httplib2 to requests
* Improve error reporting
* Exceptions below http layer removed

v0.7.0
-----
* Allow multiple API object in same thread
* Remove mutable default arguments
* Change comments to be docstrings
* Token creation supports unicode
* Add unit_tests using mock and patch, separate from functional_tests
* Optimize merge_dict

v0.6.4
-----
* Support OpenIDConnect for sandbox environment

v0.6.3
-----
* Added support for Reauthorization.

v0.6.2
-----
* Fixed content-type issue with generate_token API

v0.6.1
-----
* Added support for Python 2.6

v0.6.0
-----
* Added support for Auth and Capture APIs

v0.5.3
-----
* Added Tokeninfo and Userinfo classes to support openid_connect

v0.5.3
-----
* Validate token hash on every request
* Resolved issue with builtin function(items) in Resource class