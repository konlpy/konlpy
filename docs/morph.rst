Morphological analysis and POS tagging
======================================

*Morphological analysis* is the identification of the structure of morphemes and other linguistic units, such as root words, affixes, or parts of speech.

*POS (part-of-speech) tagging* is the process of marking up morphemes in a phrase, based on their definitions and contexts.
For example.::

    가방에 들어가신다 -> 가방/NNG + 에/JKM + 들어가/VV + 시/EPH + ㄴ다/EFN

POS tagging with KoNLPy
-----------------------

In KoNLPy, there are several different options you can choose for POS tagging.
All have the same input-output structure; the input is a phrase, and the output is a list of tagged morphemes.

For detailed usage instructions see the :doc:`api/konlpy.tag`.

.. seealso::
    `Korean POS tags comparison chart <https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0>`_

        Compare POS tags between several Korean analytic projects. (In Korean)

Comparison between POS tagging classes
--------------------------------------

Now, we do time and performation analysis for executing the ``pos`` method for each of the classes in the :doc:`api/konlpy.tag`. The experiments were carried out on a Intel i7 CPU with 4 cores, Python 2.7, and KoNLPy 0.4.1.

Time analysis [#]_
''''''''''''''''''

1. *Loading time*: Class loading time, including dictionary loads.

    - :py:class:`.Kkma`: 5.6988 *secs*
    - :py:class:`.Komoran`: 5.4866  *secs*
    - :py:class:`.Hannanum`: 0.6591  *secs*
    - :py:class:`.Twitter`: 1.4870 *secs*
    - :py:class:`.Mecab`: 0.0007 *secs*

2. *Execution time*: Time for executing the ``pos`` method for each class, with 100K characters.

    - :py:class:`.Kkma`: 35.7163 *secs*
    - :py:class:`.Komoran`: 25.6008 *secs*
    - :py:class:`.Hannanum`: 8.8251 *secs*
    - :py:class:`.Twitter`: 2.4714 *secs*
    - :py:class:`.Mecab`: 0.2838 *secs*

    If we test among a various number of characters, all classes' execution times increase in an exponential manner.

    .. image:: images/time.png


Performance analysis
''''''''''''''''''''

The performance evaluation is replaced with result comparisons for several sample sentences.

1. *"아버지가방에들어가신다"*

   We can check the spacing algorithm through this example. Desirably, an analyzer would parse this sentence to ``아버지가 + 방에 + 들어가신다`` (My father enters the room), rather than ``아버지 + 가방에 + 들어가신다`` (My father goes in the bag). :py:class:`.Hannanum` and :py:class:`.Komoran` are careful in spacing uncertain terms, and defaults the whole phrase to nouns. :py:class:`.Kkma` is more confident, but gets undesirable results. For this result, :py:class:`.Mecab` shows the best results.

.. csv-table::
    :header-rows: 1
    :file: morph-0.csv

2. *"나는 밥을 먹는다" vs "하늘을 나는 자동차"*

   If we focus on "나는" in both sentences, we can see whether an analyzer considers the context of words. "나는" in the first sentence should be ``나/N + 는/J``, and in the second sentence ``나(-ㄹ다)/V + 는/E``. :py:class:`.Kkma` properly understands the latter "나는" as a verb, wheras the rest observe it as nouns.

.. csv-table::
    :header-rows: 1
    :file: morph-1.csv

.. csv-table::
    :header-rows: 1
    :file: morph-2.csv

3. *"아이폰 기다리다 지쳐 애플공홈에서 언락폰질러버렸다 6+ 128기가실버ㅋ"*

   How do each of the analyzers deal with slang, or terms that are not included in the dictionary?

.. csv-table::
    :header-rows: 1
    :file: morph-3.csv

.. note::

    If you would like to run the experiments yourself, run `this code <https://github.com/konlpy/konlpy/blob/master/docs/morph.py>`_ from your local machine.

.. [#] Please note that these are comparisons among KoNLPy classes, and not the original distributions.
