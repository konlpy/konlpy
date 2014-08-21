Change logs
===========

`Version 0.3 <https://github.com/e9t/konlpy/releases/tag/v0.3>`_
----------------------------------------------------------------

Not released yet.

- Changed API by automatically initializing JVM for Hannanum, Kkma
- Added Kkma module with Kkma 2.0
- Added documents using Sphinx and Read the Docs
- Added license: GPL v3 or above
- Added pretty print function for Unicode
- Added noun extractor to Mecab
- Fixed Hannanum, Kkma module bug where it couldn't handle empty input strings

.. warning::

    The versions below do not have documents available, and are not backwards-compatible.

`Version 0.2 <https://github.com/e9t/konlpy/releases/tag/v0.2>`_
----------------------------------------------------------------

Released on Aug 1, 2014.

- Changed API by explicitly initializing JVM for Hannanum
- Added Mecab module with MeCab-0.996-ko-0.9.1
- Added unit tests
- Added test automation with Travis CI 
- Fixed Hannanum module parsing error when '/', '+' are in text
- Fixed Hannanum module text indexing error (results get truncated)

`Version 0.1 <https://github.com/e9t/konlpy/releases/tag/v0.1>`_
----------------------------------------------------------------

Released on Jun 15, 2014.
Initial release of KoNLPy.

- Inspired by Heewon Jeon's `KoNLP <https://github.com/haven-jeon/KoNLP>`_ project, a wrapper of the Hannanum analyzer for R. The name KoNLPy, comes from this project.
- Added Hannanum module with JHannanum 0.8.3
