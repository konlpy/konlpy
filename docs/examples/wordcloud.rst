Drawing a word cloud
====================

Below shows a code example that crawls a National Assembly bill from the web, extract nouns and draws a word cloud - from head to tail in Python.

You can change the bill number (i.e., ``bill_num``), and see how the word clouds differ per bill.
(ex: '1904882', '1904883', 'ZZ19098', etc)

.. literalinclude:: wordcloud.py
    :language: python

.. note::
    The `PyTagCloud <https://pypi.python.org/pypi/pytagcloud>`_ installed in PyPI may not be sufficient for drawing wordclouds in Korean.
    You may add eligible fonts - that support the Korean language - manually, or install the Korean supported version `here <https://github.com/e9t/PyTagCloud>`_.

.. image:: wordcloud.png
    :width: 100%
