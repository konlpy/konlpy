#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import find_packages, setup
from konlpy import __version__

def requirements():
    if sys.version_info[0] < 3:
        reqfile = 'requirements.txt'
    else:
        reqfile = 'requirements-py3.txt'
    with open(os.path.join(os.path.dirname(__file__), reqfile)) as f:
        return f.read().splitlines()

setup(name='konlpy',
    version=__version__,
    description='Python package for Korean natural language processing.',
    long_description="""\
Korean, the 13th most widely spoken language in the world, is a beautiful, yet complex language. Myriad Korean NLP engines were built by numerous researchers, to computationally extract meaningful features from the labyrinthine text.

KoNLPy is not just to create another, but to unify and build upon their shoulders, and see one step further. It is built particularly in the Python (programming) language, not only because of its its simplicity and elegance, but its powerful string processing modules and applicability to various tasks - including crawling, Web programming, and data analysis.""",
    url='http://konlpy.org',
    author='Lucy Park',
    author_email='me@lucypark.kr',
    keywords=['Korean', 'CJK',
              'NLP', 'natural language processing',
              'CL', 'computational linguistics',
              'tagging', 'tokenizing', 'linguistics', 'text analytics'],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        ],
    packages=find_packages(),
    package_data={'konlpy': [
        'data/*/*/*.txt',
        'java/conf/plugin/*/*/*.json',
        'java/data/*/*',
        'java/jhannanum-0.8.4.jar', 'java/bin/kr/lucypark/jhannanum/*/*.class',
        'java/kkma-2.0.jar', 'java/bin/kr/lucypark/kkma/*.class',
        'java/komoran-2.4-e.jar', 'java/shineware-common-2.0.jar', 'java/shineware-ds-1.0.jar', 'java/bin/kr/lucypark/komoran/*.class',
        ]},
    install_requires=requirements())
