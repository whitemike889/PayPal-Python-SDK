from distutils.core import setup
from paypal import version

setup(
    name='paypalrestsdk',
    version= version,
    author='PayPal',
    author_email='DL-PP-Platform-Python-SDK@ebay.com',
    packages=['paypalrestsdk'],
    scripts=[],
    url='https://github.com/paypal/rest-api-sdk-python',
    license='LICENSE.txt',
    description='',
    long_description=open('README.md').read(),
    install_requires=[
      'httplib2'
    ],
)
