#!/usr/bin/env python

import os.path

from setuptools import setup, find_packages


# get the version to include in setup()
dir_ = os.path.abspath(os.path.dirname(__file__))
with open(f'{dir_}/asyncio_concurrent_functions/__init__.py') as fh:
    for line in fh:
        if '__VERSION__' in line:
            exec(line)


setup(
    name='asyncio-concurrent-functions',
    version=__VERSION__,
    author='Kyle Smith',
    author_email='smithk86@gmail.com',
    url='https://github.com/smithk86/asyncio-service',
    packages=[
        'asyncio_concurrent_functions'
    ],
    install_requires=[
        'asyncio-pool'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'pytest-asyncio'
    ]
)
