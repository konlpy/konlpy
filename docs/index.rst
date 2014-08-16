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

KoNLPy is a Python package for natural language processing of the Korean language. For installation directions, see :doc:`install`.


Basic usage
-----------

.. sourcecode:: python

    from konlpy import init_jvm
    from konlpy.tag import Hannanum

    init_jvm()
    hannanum = Hannanum()
    print hannanum.pos(u'웃으면 더 행복합니다!')
    print hannanum.nouns(u'다람쥐 헌 쳇바퀴에 타고파')

For more on how to use KoNLPy, go see the :ref:`api`.


License
-------

KoNLPy is `Apache 2.0`_ licensed.
This means you are allowed to copy, modify and redistribute in both noncommercial and commercial means.
However if possible, please denote the name of this package and the original author in your work.

.. _Apache 2.0: http://opensource.org/licenses/Apache-2.0


Contribute
----------

Found a bug? Have a good idea for improving KoNLPy?
Visit the `KoNLPy GitHub page`_ and `suggest a new issue`_ or `make a pull request`_.

.. _KoNLPy GitHub page: https://github.com/e9t/konlpy
.. _suggest a new issue: https://github.com/e9t/konlpy/issues
.. _make a pull request: https://github.com/e9t/konlpy/pulls


User guide
==========

.. toctree::
  :glob:

  install

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
