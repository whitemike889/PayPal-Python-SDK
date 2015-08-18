PayPal Python SDK release notes
============================

v1.11.0
----
* Full request/response logged at DEBUG level for non production environments
* Travis tests gets deployed on new platform

v1.10.1
----
* Webhook cert patch
* Support PAYPAL_AUTH_ALGO header for webhook validation

v1.10.0
----
* Webhook certificate chain, common name and expiry validation added
* Resource conversion syntax more pythonic
* Endpoint configuration made more flexible for easier custom endpoints
* __contains__ implemented on Resource object
* Allow changing of logger level within projects

v1.9.1
----
* Webhook default algorithm update

v1.9.0
----
* Add Tox for unit test automation for different Python versions
* Support PyPy
* Sample added to demo update shipping cost during payment execution

v1.8.0
----
* Payouts cancel feature added
* Patch version imports
* Merge pull #84 for crypto dependency docs
* Google appengine workaround documented

v1.7.1
----
* OpenSSL only imported when necessary
* Dependency versions updated
* Config.py added as source of all configuration information
* Setup.py refactored to get information from config

v1.7.0
----
* Payouts API support added
* Complete pep8ify of tests and samples

v1.6.2
-----
* Search transactions for billing agreements patched
* Empty billing plan fetch issue fixed for subscription sample app
* Travis build update

v1.6.1
-----
* Python 3 compatibility patch for openssl crypto verify

v1.6.0
-----
* Webhook and Webhook events creation and management supported
* Parse webhook events and return the appropriate resource
* Verification that webhook events are unaltered and originate from PayPal
* Update Travis and Coveralls badges and User Agent for repo renaming

v1.5.0
-----
* Payment Experience customizaton feature added via API for Web Profiles

v1.4.1
-----
* Update Paypal-Client-Metadata-Id header for future payments
* Subscription API changes for searching transactions and listing billing plans

v1.4.0
-----
* Add Orders API support
* Demonstrate samples for EC parameters support (improves feature gap between REST and CLASSIC payment APIs)
* Invocing record payment, record refund and qr-code support added
* Activate method added for billing plans
* Merged toanant's pull request for #62 fix

v1.3.0
-----
* update saved credit card in vault

v1.2.2
-----
* get_access_token added to api spec
* Patches for python 3 compatibility

v1.2.1
-----
* Patch for exceptions import issue #50
* Patch for urlparse import issue

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