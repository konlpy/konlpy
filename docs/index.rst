.. KoNLPy documentation master file, created by
   sphinx-quickstart on Fri Aug 15 19:24:58 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

KoNLPy: Korean NLP in Python
============================

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

For more on how to use KoNLPy, go see the APIs.


License
-------

KoNLPy is `Apache 2.0`_ licensed.
This means you are allowed to copy, modify and redistribute in both noncommercial and commercial means, as long as you denote the original author -- Lucy Park.

.. _Apache 2.0: http://opensource.org/licenses/Apache-2.0


Contribute
----------

Found a bug? Have a good idea for improving KoNLPy?
Visit the `KoNLPy GitHub page`_ and `suggest a new issue`_ or `make a pull request`_.

.. _KoNLPy GitHub page: https://github.com/e9t/konlpy
.. _suggest a new issue: https://github.com/e9t/konlpy/issues
.. _make a pull request: https://github.com/e9t/konlpy/pulls


API
===

.. toctree::
  :glob:

  api
  install


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
