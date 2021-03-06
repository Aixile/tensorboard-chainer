#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = [
    'protobuf',
    'six',
]

test_requirements = [
    'pytest',
]

setup(
    name='tensorboard-chainer',
    version='0.2.8',
    description='Log TensorBoard events with chainer',
    author='nake nat',
    author_email='nakanat.stock@gmail.com',
    url='https://github.com/neka-nat/tensorboard-chainer',
    packages=find_packages(exclude=['docs', 'tests']),
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    test_suite='tests',
    tests_require=test_requirements
)

# python setup.py bdist_wheel --universal upload
