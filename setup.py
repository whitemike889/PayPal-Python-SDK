from distutils.core import setup
from paypal import version

setup(
    name='paypal',
    version= version,
    author='PayPal',
    author_email='DL-PP-Platform-Ruby-SDK@ebay.com',
    packages=['paypal'],
    scripts=[],
    url='https://www.x.com/',
    license='LICENSE.txt',
    description='',
    long_description=open('README.md').read(),
    install_requires=[
      'httplib2'
    ],
)
