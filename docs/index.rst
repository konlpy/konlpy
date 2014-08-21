KoNLPy: Korean NLP in Python
============================

.. image:: https://travis-ci.org/e9t/konlpy.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/e9t/konlpy
    :height: 18px

.. image:: https://readthedocs.org/projects/konlpy/badge/?version=latest
    :alt: Documentation Status
    :target: https://readthedocs.org/projects/konlpy/?badge=latest
    :height: 18px

KoNLPy is a Python package for natural language processing (NLP) of the Korean language.
For installation directions, see :doc:`here <install>`.

.. sourcecode:: python

    >>> from konlpy.tag import Kkma
    >>> from konlpy.utils import pprint
    >>> kkma = Kkma()
    >>> pprint(kkma.sentences(u'저는 대학생이구요. 소프트웨어 관련학과 입니다.'))
    [저는 대학생이구요.,
     소프트웨어 관련학과 입니다.]
    >>> pprint(kkma.nouns(u'대학에서 DB, 통계학, 이산수학 등을 배웠지만...'))
    [대학,
     통계학,
     이산,
     이산수학,
     수학,
     등]
    >>> pprint(kkma.pos(u'자주 사용을 안하다보니 모두 까먹은 상태입니다.'))
    [(자주, MAG),
     (사용, NNG),
     (을, JKO),
     (안하, VV),
     (다, ECS),
     (보, VXV),
     (니, ECD),
     (모두, MAG),
     (까먹, VV),
     (은, ETD),
     (상태, NNG),
     (이, VCP),
     (ㅂ니다, EFN),
     (., SF)]

For more on how to use KoNLPy, go see the :ref:`api`.

Standing on the shoulders of giants
-----------------------------------

Korean, the `13th most widely spoken language in the world <http://www.koreatimes.co.kr/www/news/nation/2014/05/116_157214.html>`_, is a beautiful, yet complex language.
Myriad :ref:`engines` were built by numerous researchers, to computationally extract meaningful features from the labyrinthine text.

KoNLPy is not just to create another, but to unify and build upon their shoulders, and see one step further.
It is built particularly in the `Python (programming) language <http://python.org>`_, not only because of its its simplicity and elegance, but its powerful string processing modules and applicability to various tasks - including crawling, Web programming, and data analysis.

The three philosophies this project aims to maintain are:

- Keep it simple.
- Make it easy. For humans. [#]_
- `"Democracy on the web works." <https://github.com/e9t/konlpy>`_

Please `report <me@lucypark.kr>`_ when you think any have gone stale.

License
-------

- `GPL v3 or above <http://gnu.org/licenses/gpl.html>`_ [#]_

Contribute
----------

KoNLPy isn't perfect, but it will continuously evolve and you are invited to participate!

Found a bug? Have a good idea for improving KoNLPy?
Visit the `KoNLPy GitHub page <https://github.com/e9t/konlpy>`_ and `suggest an idea <https://github.com/e9t/konlpy/issues>`_ or `make a pull request <https://github.com/e9t/konlpy/pulls>`_.


User guide
==========

.. toctree::
  :glob:
  :maxdepth: 2

  install
  morph
  data
  examples
  test
  references

.. _api:

API
===

.. toctree::
  :glob:

  api/konlpy


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* :doc:`changelog`


.. [#] With `clear and brief <http://echojuliett.tumblr.com/post/32108001510/clarity-brevity>`_ documents.
.. [#] No, I'm not extremely fond of this either. However, some important depedencies - such as Hannanum, Kkma, MeCab-ko - are GPL licensed, so we wanted to honor their licenses. (Though it was also an inevitable choice. We hope this may change in the future.)
