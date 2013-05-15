#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as fp:
    readme = fp.read()

packages = [
    'roviclient'
]

requires = [
    'requests>=1.2.0'
]

setup(
    name='roviclient',
    version='0.1.0',
    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',
    url='https://github.com/dasevilla/rovi-python',
    license='MIT',
    description='A simple Python client library for the Rovi API',
    long_description=readme,
    install_requires=requires,
    packages=packages,
)
