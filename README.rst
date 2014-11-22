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

To modify docs
--------------

Setup
'''''

1. Include the following lines in `~/.bashrc`

        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8

2. Install dependencies

        $ make init_i18n

Modify
''''''

1. Modify a document file

Move to the `docs` folder and modify the corresponding `*.rst` files

        $ cd docs
        $ vi some_file.rst

2. Build docs

        $ make html

3. Extract translation phrases

        $ make extract_i18n

4. Modify translations

        $ cd locale/ko/LC_MESSAGES
        $ vi some_file.po

5. Update translations

        $ make update_i18n

6. Commit and push to the repository
