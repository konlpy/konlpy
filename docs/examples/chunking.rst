Chunking
========

After tagging a sentence with part of speech, we can segment it into several higher level multitoken sequences, or "chunks".

Here we demonstrate a way to easily chunk a sentence, and find noun, verb and adjective phrases in Korean text, using :py:class:`nltk:nltk.chunk.regexp.RegexpParser`.

.. literalinclude:: chunking.py
    :language: python

According to the chunk grammer defined above, we have three rules to extracted phrases from our sentence.
First, we have a rule to extract noun phrases (NP), where our chunker finds a serial of nouns, followed with an optional Suffix. (Note that these rules can be modified for your purpose, and that they should differ for each morphological analyzer.)
Then we have two more rules, each defining verb phrases (VP) and adjective phrases (AP).

The result is a tree, which we can print on the console, or display graphically as follows.

- Console::
  
    (S
      (NP man/Noun 6/Number se/Noun iha/Noun)
      yi/Josa
      (NP codeunghaggyo/Noun cwihag/Noun jeon/Noun janyeo/Noun)
      reul/Josa
      (NP yangyug/Noun)
      (VP hagi/Verb wihaeseo/Verb)
      neun/Eomi)

- chunking.png
    .. image:: chunking.png
        :width: 100%
