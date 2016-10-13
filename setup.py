# -*- coding: utf-8 -*-
"""setup.py."""

from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'requests>=2.11.1',
    'xmltodict>=0.10.2'
]

VERSION = '0.0.8'

LONG_DESCRIPTION = 'wechatkit is a common wechat api component.'

setup(
    name='wechatkit',
    version=VERSION,
    description='wechatkit is a common wechat api component.',
    long_description=LONG_DESCRIPTION,
    author='silence',
    author_email='istommao@gmail.com',
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/istommao/wechatkit',
    keywords='wechatkit is a common wechat api component!'
)
