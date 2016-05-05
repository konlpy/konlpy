#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys
import platform
from setuptools import find_packages, setup
from description import __version__

def requirements():
    # both JPype1 and JPype1-py3 doesn't support Windows. see http://konlpy.org/en/v0.4.4/install/.
    if platform.system() == 'Windows':
        return []

    def _openreq(reqfile):
        with open(os.path.join(os.path.dirname(__file__), reqfile)) as f:
            return f.read().splitlines()

    if sys.version_info.major >= 3:
        return _openreq('requirements-py3.txt')
    else:
        return _openreq('requirements.txt')

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
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        ],
    license='GPL v3+',
    packages=find_packages(),
    package_data={'konlpy': [
        'data/corpus/*/*.txt',
        'data/tagset/*.json',
        'java/conf/plugin/*/*/*.json',
        'java/data/*/*',
        'java/*.jar',
        'java/bin/kr/lucypark/*/*.class',
        'java/bin/kr/lucypark/*/*/*.class',
        ]},
    install_requires=requirements())
