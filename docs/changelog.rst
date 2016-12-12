Change logs
===========

`Version 0.4.4 <https://github.com/konlpy/konlpy/releases/tag/v0.4.4>`_
-----------------------------------------------------------------------

Released on Oct 25, 2015.

- Include tagsets for each morpheme analyzer [:commit:`26a39d7`]

`Version 0.4.3 <https://github.com/konlpy/konlpy/releases/tag/v0.4.3>`_
-----------------------------------------------------------------------

Released on Feb 27, 2015.

- Fix conditional requirement bug for pip3 [:issue:`50`]

`Version 0.4.2 <https://github.com/konlpy/konlpy/releases/tag/v0.4.2>`_
-----------------------------------------------------------------------

Released on Feb 25, 2015.

- Update Korean documents (i.e., include missing .mo files)

`Version 0.4.1 <https://github.com/konlpy/konlpy/releases/tag/v0.4.1>`_
-----------------------------------------------------------------------

Released on Feb 25, 2015.

- Added :py:class:`.tag.Twitter`
- Added wheel files to pypi [:issue:`48`]
- Fixed bash script syntax error [:issue:`42` by :committer:`re4lfl0w`]
- Fixed pip3 installation error [:issue:`43`]
- Include Komoran dictionaries in package [:commit:`796c156`]

`Version 0.4.0 <https://github.com/konlpy/konlpy/releases/tag/v0.4.0>`_
-----------------------------------------------------------------------

Released on Jan 18, 2015.

- Added :py:mod:`.data`, :py:mod:`.downloader` [:issue:`4`]
- Added :py:func:`.utils.csvread`, :py:func:`.utils.csvwrite`
- Added :py:func:`.utils.read_txt()`
- Added nonflattened results for POS taggers
- Added Komoran module with KOMORAN 2.4
- Change dependency version of JPype1 to 0.5.7+
- Change dependency version of mecab-python from 0.993 to 0.996 [:issue:`19` with comments by Yong-woon Lee]
- Fixed concordance bug for Python2 [:commit:`6caa929`]
- Fixed pprint bug on Windows [:issue:`37`]

`Version 0.3.3 <https://github.com/konlpy/konlpy/releases/tag/v0.3.3>`_
-----------------------------------------------------------------------

Released on Sep 7, 2014.

- Added Python 3 support [:issue:`17` by :committer:`hyeshik`]
- Created `KoNLPy mailing list at Google Groups <https://groups.google.com/forum/#!forum/konlpy>`_

`Version 0.3.2 <https://github.com/konlpy/konlpy/releases/tag/v0.3.2>`_
-----------------------------------------------------------------------

Released on Sep 4, 2014.

- Fixed JPype class loading error for Mac OS X [:issue:`6` by :committer:`combacsa`]
    - JPype 0.5.5.4 is not compatible with JDK 1.7 in Mac OS X 10.9
- Fixed Kkma memory error for Mac OS X [:issue:`13` by :committer:`combacsa`]
    - `java.lang.OutOfMemoryError` in Mac OS X if heap memory is too small

`Version 0.3.1 <https://github.com/konlpy/konlpy/releases/tag/v0.3.1>`_
-----------------------------------------------------------------------

Released on Sep 4, 2014.

- Added MeCab installer script
- Fixed Morph modules to handle strings with whitespaces only
- Fixed data inclusion error for Hannanum
- Modified tagger filenames with underscore prefixes
- Modified concordance function not to print results by default
- Modified Hannanum `morph` method to `analyze`
- Uploaded `KoNLPy to PyPI <https://pypi.python.org/pypi/konlpy>`_

`Version 0.3.0 <https://github.com/konlpy/konlpy/releases/tag/v0.3.0>`_
-----------------------------------------------------------------------

Released on Aug 25, 2014.

- Changed API by automatically initializing JVM for Hannanum, Kkma
- Added Kkma module with Kkma 2.0
- Added documents using Sphinx and Read the Docs
- Added license: GPL v3 or above
- Added pretty print function for Unicode
- Added noun extractor to Mecab
- Fixed Hannanum, Kkma module bug where it couldn't handle empty input strings

.. warning::

    The versions below do not have documents available, and are not backwards-compatible.

`Version 0.2 <https://github.com/konlpy/konlpy/releases/tag/v0.2>`_
-------------------------------------------------------------------

Released on Aug 1, 2014.

- Changed API by explicitly initializing JVM for Hannanum
- Added Mecab module with MeCab-0.996-ko-0.9.1
- Added unit tests
- Added test automation with Travis CI 
- Fixed Hannanum module parsing error when '/', '+' are in text
- Fixed Hannanum module text indexing error (where results get truncated)

`Version 0.1 <https://github.com/konlpy/konlpy/releases/tag/v0.1>`_
-------------------------------------------------------------------

Released on Jun 15, 2014.
Initial release of KoNLPy.

- Inspired by Heewon Jeon's `KoNLP <https://github.com/haven-jeon/KoNLP>`_ project, a wrapper of the Hannanum analyzer for R. The name KoNLPy, comes from this project.
- Added Hannanum module with JHannanum 0.8.3
