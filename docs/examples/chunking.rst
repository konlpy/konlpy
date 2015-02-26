Chunking
========

After :doc:`tagging a sentence with part of speech </morph>`, we can segment it into several higher level multitoken sequences, or "chunks".

Here we demonstrate a way to easily chunk a sentence, and find noun, verb and adjective phrases in Korean text, using :py:class:`nltk:nltk.chunk.regexp.RegexpParser`.

.. literalinclude:: chunking.py
    :language: python

According to the chunk grammer defined above, we have three rules to extracted phrases from our sentence.
First, we have a rule to extract noun phrases (NP), where our chunker finds a serial of nouns, followed with an optional Suffix. (Note that these rules can be modified for your purpose, and that they should differ for each morphological analyzer.)
Then we have two more rules, each defining verb phrases (VP) and adjective phrases (AP).

The result is a tree, which we can print on the console, or display graphically as follows.

- Console::
  

    # Print whole tree
    (S
      (NP 만/Noun 6/Number 세/Noun 이하/Noun)
      의/Josa
      (NP 초등학교/Noun 취학/Noun 전/Noun 자녀/Noun)
      를/Josa
      (NP 양육/Noun)
      (VP 하기/Verb 위해서/Verb)
      는/Eomi)

    # Print noun phrases only
    만 6 세 이하
    (NP 만/Noun 6/Number 세/Noun 이하/Noun)
    초등학교 취학 전 자녀
    (NP 초등학교/Noun 취학/Noun 전/Noun 자녀/Noun)
    양육
    (NP 양육/Noun)

- chunking.png
    .. image:: chunking.png
        :width: 100%
