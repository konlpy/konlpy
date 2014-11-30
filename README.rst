KoNLPy
======

.. image:: https://travis-ci.org/e9t/konlpy.svg?branch=master
    :alt: Build Status
    :target: https://travis-ci.org/e9t/konlpy

.. image:: https://readthedocs.org/projects/konlpy/badge/?version=latest
    :alt: Documentation Status
    :target: https://readthedocs.org/projects/konlpy/?badge=latest

.. image:: https://coveralls.io/repos/e9t/konlpy/badge.png
    :alt: Coverage Status
    :target: https://coveralls.io/r/e9t/konlpy

한국어 자연어처리를 할 수 있는 파이썬 패키지입니다.

KoNLPy is a Python package for natural language processing of the Korean language. 

- English documentation: http://konlpy.org/en
- 한국어 문서: http://konlpy.org/ko

Contributing
""""""""""""

Documentation
-------------

Setup docs
''''''''''

1. Fork and clone KoNLPy::

    git clone git@github.com:[your_github_id]/konlpy.git
    
1. Include the following lines in your `~/.bashrc`::

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

2. Install dependencies::

    $ make init_i18n

Modify and push docs
''''''''''''''''''''

1. Modify a document file::

    $ cd docs             # Move to the `docs` folder
    $ vi some_file.rst    # Modify corresponding `*.rst` files

2. Build docs::

    $ make html

3. Extract translation phrases::

    $ make extract_i18n

4. Modify translations::

    $ cd locale/ko/LC_MESSAGES
    $ vi some_file.po

5. Update translations::

    $ make update_i18n

6. Commit and push your repository

7. Send a pull request
