from distutils.core import setup
from paypalrestsdk.version import __version__

setup(
    name='paypalrestsdk',
    version= __version__,
    author='PayPal',
    author_email='DL-PP-Platform-Python-SDK@ebay.com',
    packages=['paypalrestsdk'],
    scripts=[],
    url='https://github.com/paypal/rest-api-sdk-python',
    license='LICENSE.txt',
    description='The PayPal REST SDK provides Python APIs to create, process and manage payment',
    long_description=open('README.md').read(),
    install_requires=[
      'httplib2'
    ],
)
