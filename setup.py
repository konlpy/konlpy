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

    if sys.version_info[0] < 3:
        return _openreq('requirements2.txt')

    return _openreq('requirements.txt')


about = get_about()
setup(name='konlpy',
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
     install_requires=requirements())
