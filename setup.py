from setuptools import setup, find_packages


with open('README.rst') as fp:
    long_description = fp.read()


setup(
    name='roviclient',
    version='0.1.0',

    description='A simple Python client library for the Rovi API',
    long_description=long_description,

    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',

    url='https://github.com/dasevilla/rovi-python',
    download_url='https://github.com/dasevilla/rovi-python/tarball/master',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    install_requires=[
        'requests>=1.2.0',
    ],

    packages=find_packages(),
)
