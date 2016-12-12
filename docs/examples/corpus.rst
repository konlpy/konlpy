Exploring a corpus
==================

A corpus is a set of documents.

Below is a way of exploring unique tokens of a corpus,
namely the `Heap's Law <http://en.wikipedia.org/wiki/Heaps%27_law>`_.

.. literalinclude:: corpus.py
    :language: python

- heap.png:
    .. image:: heap.png
        :width: 100%

But why is our image not log-function shaped, as generally known?
That is because the corpus we used is very small, and contains only 10 documents.
To observe the Heap's law's log-function formatted curve,
try experimenting with a larger corpus.
Below is an image drawn from 1,000 Korean news articles.
Of course, the curve will become smoother with a much larger corpus.

- heap-1000.png:
    .. image:: heap-1000.png
        :width: 100%
