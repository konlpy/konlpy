#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import sys
import platform
from setuptools import find_packages, setup


def get_about():
    about = {}
    basedir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(basedir, 'konlpy', 'about.py')) as f:
        exec(f.read(), about)
    return about


def requirements():
    # both JPype1 and JPype1-py3 don't support Windows. see http://konlpy.org/en/v0.4.4/install/.
    if platform.system() == 'Windows':
        return []

    def _openreq(reqfile):
        with open(os.path.join(os.path.dirname(__file__), reqfile)) as f:
            return f.read().splitlines()

    if sys.version_info >= (3, ):
        return _openreq('requirements-py3.txt')
    else:
        return _openreq('requirements.txt')

<<<<<<< master

about = get_about()
setup(name='konlpy',
=======
setup(name='konlpy',
<<<<<<< HEAD
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
=======
>>>>>>> Revert "update experimental streaming interface from koshort"
      version=about['__version__'],
      description=about['__summary__'],
      long_description=about['__description__'],
      url=about['__url__'],
      author=about['__author__'],
      author_email=about['__email__'],
      keywords=['Korean', 'CJK',
                'NLP', 'natural language processing',
                'CL', 'computational linguistics',
                'tagging', 'tokenizing', 'linguistics', 'text analytics'],
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Information Analysis',
          'Topic :: Text Processing',
          'Topic :: Text Processing :: Filters',
          'Topic :: Text Processing :: General',
          'Topic :: Text Processing :: Linguistic',
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
      ],
      license=about['__license__'],
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
<<<<<<< master
      entry_points={'console_scripts': [
          'stream_twitter = konlpy.stream.twitter:main',
          'stream_naver = konlpy.stream.naver:main',
          'stream_daum = konlpy.stream.daum:main',
          'stream_google = konlpy.stream.google_trend:main',
          'stream_dcinside = konlpy.stream.dcinside:main',
      ]},
      install_requires=requirements())
=======
      install_requires=requirements())
>>>>>>> parent of 82368b6... update experimental streaming interface from koshort
>>>>>>> Revert "update experimental streaming interface from koshort"
