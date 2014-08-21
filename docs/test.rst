Running tests
=============

KoNLPy has tests to evaulate its quality.
To perform a test, use the code below.

.. code-block:: bash

    $ pip install pytest
    $ cd konlpy
    $ py.test

.. note::

    KoNLPy was tested on the below environments:

    - Ubuntu 12.04 with openjdk-7-jdk
    - Ubuntu 13.10 with openjdk-7-jdk
    - Window 7 with Sun/Oracle JDK 1.7.0 (:py:mod:`.hannanum`, :py:mod:`.mecab` have issues)
