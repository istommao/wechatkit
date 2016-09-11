# -*- coding: utf-8 -*-
"""setup.py."""
import os
from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'requests>=2.11.1',
    'xmltodict>=0.10.2'
]

VERSION = '0.0.5'


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    README = f.read()


setup(
    name='wechatkit',
    version=VERSION,
    description='wechatkit is a common wechat api component.',
    long_description=README,
    author='silence',
    author_email='istommao@gmail.com',
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/istommao/wechatkit',
    keywords='wechatkit is a common wechat api component!'
)
