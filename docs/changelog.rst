Change logs
===========

`Version 0.6.0 <https://github.com/konlpy/konlpy/releases/tag/v0.6.0>`_
-----------------------------------------------------------------------

Released on Jan 2, 2022.

- Added English version of `CONTRIBUTING.rst` [:issue:`302` by :committer:`gabrielacorona`]
- Enhanced jpype compatibility for Windows [:issue:`370` by :committer:`hexists`]
- Fixed parsing issue for Mecab [:issue:`360` by :committer:`swyo`]
- Fixed `make check` for in `Makefile` [:issue:`340` by :committer:`kwonmha`]
- Fixed errors in documentation [:issue:`299` by :committer:`hdatteln`], [:issue:`308` by :committer:`hdatteln`]
- Refactored code [:issue:`323` by :committer:`nyanye`]
- Removed koshort [:issue:`318` by :committer:`nyanye`]

`Version 0.5.2 <https://github.com/konlpy/konlpy/releases/tag/v0.5.2>`_
-----------------------------------------------------------------------

Released on Dec 3, 2019.

- Added normalize method to Okt [:issue:`100` by :committer:`lifefeel`]
- Added data acquisition features from Koshort [:issue:`211` by :committer:`nyanye`]
- Added docker installation steps [:issue:`252` by :committer:`raccoonyy`]
- Updated Mecab to mecab-0.996-ko-0.9.2 and mecab-ko-dic-2.1.1-20180720 [:issue:`214` by :committer:`rickiepark`]
- Added Python 2 warning at the install.rst [:issue:`277` by :committer:`minhoryang`]
- Added methods to make Mecab picklable [:issue:`234` by :committer:`rickiepark`] [:issue:`258` by :committer:`rickiepark`]
- Added tests for coverage [:issue:`261` by :committer:`minhoryang`] [:issue:`262` by :committer:`minhoryang`]
- Fixed Komoran not to POS tag empty sentences [:issue:`201` by :committer:`lovit`]
- Fixed JPype usage by adding numpy as dependency [:issue:`246` by :committer:`e9t`]
- Fixed to use tweepy 3.7.0+ to avoid collision with Python 3.7+ [:issue:`243` by :committer:`shurain`]
- Fixed to use JPype 0.7.0+ to remove warning message [:issue:`245` by :committer:`e9t`]
- Fixed to use lxml 4.1.0+ to avoid installation errors [:issue:`242` by :committer:`shurain`]
- Fixed stream.google_trend test fail [:issue:`244` by :committer:`shurain`]
- Fixed by removing .decode in Mecab.pos for Python3 usage [:issue:`108` by :committer:`ty91`]
- Updated Mecab installation script [:issue:`158` by :committer:`HaebinShin`], [:issue:`247` by :committer:`e9t`], [:issue:`255` by :committer:`HaebinShin`], [:issue:`277` by :committer:`minhoryang`]
- Lower-bound Java Compile Version [:issue:`259` by :committer:`e9t`]

`Version 0.5.1 <https://github.com/konlpy/konlpy/releases/tag/v0.5.1>`_
-----------------------------------------------------------------------

Released on Aug 3, 2018.

- Added JVM memory option to backends [:issue:`199` by :committer:`lovit`]

`Version 0.5.0 <https://github.com/konlpy/konlpy/releases/tag/v0.5.0>`_
-----------------------------------------------------------------------

Released on Aug 1, 2018.

- Added userdic to Komoran [:issue:`87` by :committer:`lovit`]
- Added `stream` parameter to pprint [:issue:`179` by :committer:`jaejunh`]
- Added `join` parameter to POS taggers [:issue:`135` by :committer:`pinetree408`]
- Fixed JPype-related installation error [:issue:`94` by :committer:`shaynekang`]
- Moved description.py to konlpy/about.py [:issue:`194`]
- Refactored Java code [:issue:`86` by :committer:`mwkang`]
- Replaced wildcard expansion in `mecab.sh` [:issue:`161` by :committer:`j-min`]
- Updated Komoran from 2.4 to 3.0 and add userdic [:issue:`198` by :committer:`lovit`]
- Updated Twitter from 2.4.3 to okt-2.1.0 [:issue:`156` by :committer:`zsef123`]

.. warning::

    Previous `dicpath` in Komoran's API is now `modelpath`.
    The name was changed to prevent confusion with the newly added `userdic`.

`Version 0.4.4 <https://github.com/konlpy/konlpy/releases/tag/v0.4.4>`_
-----------------------------------------------------------------------

Released on Oct 25, 2015.

- Included tagsets for each morpheme analyzer [:commit:`26a39d7`]

`Version 0.4.3 <https://github.com/konlpy/konlpy/releases/tag/v0.4.3>`_
-----------------------------------------------------------------------

Released on Feb 27, 2015.

- Fixed conditional requirement bug for pip3 [:issue:`50`]

`Version 0.4.2 <https://github.com/konlpy/konlpy/releases/tag/v0.4.2>`_
-----------------------------------------------------------------------

Released on Feb 25, 2015.

- Updated Korean documents (i.e., include missing .mo files)

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
- Enabled installation via ``pip``
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
