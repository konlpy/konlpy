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

KoNLPy is a Python package for natural language processing of the Korean language. For installation directions, see :doc:`here <install>`.

Basic usage
-----------

.. sourcecode:: python

    from konlpy.tag import Hannanum

    hannanum = Hannanum()
    print hannanum.pos(u'웃으면 더 행복합니다!')
    print hannanum.nouns(u'다람쥐 헌 쳇바퀴에 타고파')

For more on how to use KoNLPy, go see the :ref:`api`.

License
-------

The majority of KoNLPy is `Apache v2.0 <http://opensource.org/licenses/Apache-2.0>`_ licensed.
This means you are allowed to copy, modify and redistribute most parts of the package in both noncommercial and commercial means.

However, please note that the :py:mod:`.hannanum`, :py:mod:`.kkma` modules are copylefted, and each are licensed GPL3, GPL2, according to the original license. [#]_ All other parts of the package are free to use.

Contribute
----------

Found a bug? Have a good idea for improving KoNLPy?
Visit the `KoNLPy GitHub page <https://github.com/e9t/konlpy>`_ and `suggest a new issue <https://github.com/e9t/konlpy/issues>`_ or `make a pull request <https://github.com/e9t/konlpy/pulls>`_.



User guide
==========

.. toctree::
  :glob:
  :maxdepth: 2

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

.. [#] The original JHannanum and Kkma projects are licensed `GPL v3 or above <http://gnu.org/licenses/gpl.html>`_, `GPL v2 <http://www.gnu.org/licenses/gpl-2.0.html>`_, respectively.
