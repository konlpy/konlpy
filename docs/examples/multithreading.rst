Multithreading with KoNLPy
==========================

Sometimes it gets boring to wait for tagging jobs to end.
How about using some concurrency tricks?
Python supports multithreading and multiprocessing out-of-the-box, and you can use them with KoNLPy as well.
Here's an example using multithreading.

.. literalinclude:: multithreading.py
    :language: python

- Console::

    Number of lines in document:
    356
    Batch tagging:
    37.758173
    Concurrent tagging:
    8.037602


Check out how much faster it gets!

.. note::
    - Some useful references on concurrency with Python:
        - 장혜식, `"파이썬은 멀티코어 줘도 쓰잘데기가 없나요?"에 대한 파이썬 2.6의 대답 <http://highthroughput.org/wp/python-multiprocessing/>`_, 2008.
        - 하용호, `파이썬으로 클라우드 하고 싶어요 <http://www.slideshare.net/devparan/h3-2011-c6-python-and-cloud>`_, 2011.
