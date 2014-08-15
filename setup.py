#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(name='konlpy',
    version='0.3',
    description='Korean morpheme analyzer on Python',
    url='http://github.com/e9t/konlpy',
    author='Lucy Park',
    author_email='me@lucypark.kr',
    license='Apache v2.0',
    packages=find_packages(),
    package_data={'konlpy': [
        'java/conf/plugin/*/*/*.json',
        'java/data/*/*',
        'java/jhannanum-0.8.4.jar',
        'java/bin/kr/lucypark/jhannanum/*/*.class',
        'java/src/kr/lucypark/jhannanum/*/*.java']},
    install_requires=requirements,
    zip_safe=False)
