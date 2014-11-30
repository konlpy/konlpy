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
++++++++++++

누구나 KoNLPy의 컨트리뷰터가 될 수 있습니다.

컨트리뷰션을 하는 방법은 1) 질문하기 2) 이슈 제안/해결하기 3) 문서 수정하기 등 세 가지입니다.

1) 질문하기
-----------

1. KoNLPy를 사용하다가 막히는 부분이 있다면 먼저 `이슈가 제기되었는지 확인 <https://github.com/e9t/konlpy/issues>`_ 해봅니다.
2. 같은 이슈가 이미 제기되었고,
    - 이슈가 해결되었다면(closed): 최신 릴리즈에서 문제가 해결되었을 가능성이 높습니다. 쓰레드에서 다른 분들이 어떻게 해결했는지 파악해보는 것도 좋은 방법입니다.
    - 이슈가 아직 해결되지 않았다면(open): 댓글로 문제 상황을 설명해주세요.
3. 같은 이슈가 아직 제기되지 않았다면, "New Issue" 버튼을 눌러 이슈를 새로 생성해주시면 됩니다. 이슈를 새로 생성하시는 경우에는 사용하는 OS나 패키지 버젼 등을 같이 적어주시면 문제를 빠르게 해결하는데 도움이 됩니다. 

2) 이슈 제안/해결하기
---------------------

- `깃헙 이슈 <https://github.com/e9t/konlpy/issues>`_ 에 코드를 개선할 수 있는 방법을 제안하거나, 제안된 이슈에 대해 토론/해결하실 수 있습니다.
- 기여하신 부분에 대해 정확한 attribution을 할 수 있도록, 가능하다면 pull request를 보내주시기 바랍니다.

3) 문서 수정하기
----------------

- 사소한 오타 등을 발견하여 수정을 요청하고 싶은 경우에는 konlpy@googlegroups.com로 메일을 보내주셔도 됩니다.
- 하지만 기왕이면 기여하신 부분에 대해 정확한 attribution을 할 수 있도록, pull request를 보내주시기 바랍니다.

Setup docs
''''''''''

1. Fork and clone KoNLPy::

    git clone git@github.com:[your_github_id]/konlpy.git
    
2. Include the following lines in your `~/.bashrc`::

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

3. Install dependencies::

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
