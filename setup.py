#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='konlpy',
    version='0.1',
    description='Korean morpheme analyzer on Python',
    url='http://github.com/e9t/konlpy',
    author='Lucy Park',
    author_email='ejpark04@snu.ac.kr',
    license='Apache v2.0',
    packages=['konlpy'],
    install_requires=[
        'JPype1==0.5.5.1',
        'regex==2014.02.19',
    ],
    zip_safe=False)
