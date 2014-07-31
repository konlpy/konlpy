#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='konlpy',
    version='0.3-dev',
    description='Korean morpheme analyzer on Python',
    url='http://github.com/e9t/konlpy',
    author='Lucy Park',
    author_email='me@lucypark.kr',
    license='Apache v2.0',
    packages=['konlpy'],
    package_data={'konlpy': [
        'java/conf/plugin/*/*/*.json',
        'java/data/*/*',
        'java/jhannanum-0.8.4.jar',
        'java/bin/kr/lucypark/jhannanum/*/*.class',
        'java/src/kr/lucypark/jhannanum/*/*.java']},
    install_requires=[
        'JPype1>=0.5.5.1',
        'regex>=2014.02.19',
    ],
    zip_safe=False)
