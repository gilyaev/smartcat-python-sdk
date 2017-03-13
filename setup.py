#!/usr/bin/env python

from setuptools import setup

import os
import re

this_dir = os.path.dirname(__file__)
readme_filename = os.path.join(this_dir, 'README.rst')
requirements_filename = os.path.join(this_dir, 'requirements.txt')
init_file = os.path.join(this_dir, 'smartcat/__init__.py')


with open(init_file, 'r') as fd:
    PACKAGE_VERSION = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE).group(1)

PACKAGE_NAME = 'smartcat'
PACKAGE_AUTHOR = 'Viktor Zhyliaiev'
PACKAGE_AUTHOR_EMAIL = 'gilyaev@gmail.com'
PACKAGE_DESCRIPTION = 'An SDK built to facilitate integration with SmartCAT API.'
PACKAGE_URL = 'https://github.com/gilyaev/smartcat-python-sdk'
PACKAGES = [
    'smartcat',
]
PACKAGE_DATA = {}
PACKAGE_LICENSE = 'Apache 2.0'

with open(readme_filename) as f:
    PACKAGE_LONG_DESCRIPTION = f.read()


with open(requirements_filename) as f:
    PACKAGE_INSTALL_REQUIRES = [line[:-1] for line in f]


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description=PACKAGE_DESCRIPTION,
    long_description=PACKAGE_LONG_DESCRIPTION,
    author=PACKAGE_AUTHOR,
    author_email=PACKAGE_AUTHOR_EMAIL,
    url=PACKAGE_URL,
    packages=PACKAGES,
    include_package_data=True,
    package_data=PACKAGE_DATA,
    package_dir={'smartcat': 'smartcat'},
    install_requires=PACKAGE_INSTALL_REQUIRES,
    license=PACKAGE_LICENSE,
    zip_safe=False,
)
