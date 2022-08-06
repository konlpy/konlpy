References
==========

.. role:: license

.. role:: language

.. note::
    Please `modify this document <https://github.com/konlpy/konlpy/blob/master/docs/references.rst>`_ if anything is erroneous or not included.
    Last updated at |today|.

.. _engines:

Korean morpheme analyzer tools
------------------------------

When you're analyzing Korean text, the most basic task you need to perform is morphological analysis.
There are several libraries in various programming languages to achieve this:

C/C++
'''''

- `MeCab-ko <https://bitbucket.org/eunjeon/mecab-ko/>`_ (2013) - By Yong-woon Lee and Youngho Yoo :license:`GPL` :license:`LGPL` :license:`BSD`
- `UTagger <http://nlplab.ulsan.ac.kr/Demo/ProjectDemo.html>`_ (2012) - By Joon-Choul Shin, Cheol-Young Ock* (Ulsan University) :license:`GPL` :license:`custom`
    - 신준철, 옥철영, `기분석 부분 어절 사전을 활용한 한국어 형태소 분석기 (A Korean Morphological Analyzer using a Pre-analyzed Partial Word-phrase Dictionary) <http://www.dbpia.co.kr/Journal/ArticleDetail/NODE01873335>`_, 정보과학회논문지: 소프트웨어 및 응용, 제39권 제5호, 2012.
    - 신준철, 옥철영, `한국어 품사 및 동형이의어 태깅을 위한 단계별 전이모델 (A Stage Transition Model for Korean Part-of-Speech and Homograph Tagging) <http://www.dbpia.co.kr/Journal/ArticleDetail/NODE02033338>`_, 정보과학회논문지: 소프트웨어 및 응용, 제39권 제11호, 2012.
    - `slides <http://www.slideserve.com/mills/u-tagger-2013>`_
- `MACH <http://cs.sungshin.ac.kr/~shim/demo/mach.html>`_ (2002) - By Kwangseob Shim (성신여대) :license:`custom`
    - Kwangseob Shim, Jaehyung Yang, `MACH: A Supersonic Korean Morphological Analyzer <http://www.aclweb.org/anthology/C02-1092>`_, ACL, 2002.
- `KTS <http://wiki.kldp.org/wiki.php/KTS>`_ (1995) - By 이상호, 서정연, 오영환 (KAIST) :license:`GPL v2`
    - 이상호, `KTS: Korean Tagging System Manual (Version 0.9) <https://wiki.kldp.org/wiki.php/KTS?action=download&value=ktsmanual.pdf>`_
    - 김재훈, 서정연, `자연언어 처리를 위한 한국어 품사 태그 (A Korean part-of-speech tag set for natural language processing) <https://wiki.kldp.org/wiki.php/KTS?action=download&value=tag-set.pdf>`_, 1993.
    - Created at 1995, released at 2002. [1]_

Java/Scala
''''''''''

- `twitter-korean-text <https://github.com/twitter/twitter-korean-text/>`_ (2014) - By Will Hohyon Ryu (Twitter) :license:`Apache v2`
- `KOMORAN <http://shineware.tistory.com/tag/KOMORAN>`_ (2013) - By 신준수 (shineware) :license:`Apache v2`
- `KKMA <http://kkma.snu.ac.kr>`_ (2010) - By Sang-goo Lee*, `Dongjoo Lee <http://therocks.tistory.com>`_, et al. (Seoul National University) :license:`GPL v2`
    - 이동주, 연종흠, 황인범, 이상구, `꼬꼬마: 관계형 데이터베이스를 활용한 세종 말뭉치 활용 도구 <http://ids.snu.ac.kr/w/images/f/f8/CPL2010-therocks.pdf>`_, 정보과학회논문지: 컴퓨팅의 실제 및 레터, Volume 16, No.11, 2010.
- `Arirang <http://cafe.naver.com/korlucene>`_ (2009) - By SooMyung Lee :license:`Apache v2`
    - `code <http://sourceforge.net/projects/lucenekorean>`_
- `HanNanum <http://semanticweb.kaist.ac.kr/home/index.php/HanNanum>`_ (1999) - By Key-Sun Choi* et al. (KAIST) :license:`GPL v3`
    - `code <http://kldp.net/projects/hannanum/src>`_, `docs <http://semanticweb.kaist.ac.kr/research/hannanum/j/javadoc/>`_

Python
''''''

- `KoNLPy <http://konlpy.org>`_ (2014) :license:`GPL v3+`
    - By Lucy Park (Seoul National University)
    - Wrapper for Hannanum, KKMA, KOMORAN, twitter-korean-text, MeCab-ko
    - Tools for Hangul/Korean manipulation
- `UMorpheme <https://pypi.python.org/pypi/UMorpheme>`_ (2014) :license:`MIT`
    - By Kyunghoon Kim (UNIST)
    - Wrapper for MeCab-ko for online usage

R
''

- `KoNLP <https://github.com/haven-jeon/KoNLP>`_ (2011) :license:`GPL v3`
    - By Heewon Jeon
    - Wrapper for Hannaum

Others
''''''

- `K-LIWC <http://k-liwc.ajou.ac.kr/>`_ (아주대)
- `KRISTAL-IRMS <http://www.kristalinfo.com/>`_ (KISTI)
    - `Development history <http://spasis.egloos.com/9507>`_
- `Korean XTAG <http://www.cis.upenn.edu/~xtag/koreantag/>`_ (UPenn)
- `HAM <http://nlp.kookmin.ac.kr/HAM/kor/ham-intr.html>`_ (국민대)
- `POSTAG/K <http://nlp.postech.ac.kr/~project/DownLoad/k_api.html>`_ (POSTECH)

.. _corpora:

Corpora
-------

- `Korean Universal Dependency (UD) Treebank <https://github.com/UniversalDependencies/UD_Korean>`_, 2013.
- Korea University Korean Corpus, 1995.
    - 10M tokens of Korean of 1970-90s
- `HANTEC 2.0 <http://www.kristalinfo.com/download/#hantec>`_, KISTI & 충남대, 1998-2003.
    - 120,000 test documents (237MB)
    - 50 TREC-type questions for QA (48KB)
- `HKIB-40075 <http://www.kristalinfo.com/TestCollections/readme_hkib.html>`_, KISTI & 한국일보, 2002.
    - 40,075 test documents for text categorization (88MB)
- `KAIST Corpus <http://semanticweb.kaist.ac.kr/home/index.php/KAIST_Corpus>`_, KAIST, 1997-2005.
- `Sejong Corpus <http://www.sejong.or.kr/>`_, National Institute of the Korean Language, 1998-2007.
- Yonsei Corpus, 연세대, 1987.
    - 42M tokens of Korean since the 1960s
- `BoRA 언어자원은행 <http://semanticweb.kaist.ac.kr/org/bora/>`_, KAIST

Other NLP tools
---------------

- `Hangulize <http://www.hangulize.org/>`_ - By Heungsub Lee :language:`Python`
    - Hangul transcription tool to 38+ languages
- `Hanja <https://github.com/suminb/hanja>`_ - By Sumin Byeon :language:`Python`
    - Hanja to hangul transcriptor
- `Jamo <http://github.com/JDong820/python-jamo>`_ - By Joshua Dong :language:`Python`
    - Hangul syllable decomposition and synthesis
- `KoreanParser <http://semanticweb.kaist.ac.kr/home/index.php/KoreanParser>`_ - By DongHyun Choi, Jungyeul Park, Key-Sun Choi (KAIST) :language:`Java`
    - Language parser
- `Korean <http://pythonhosted.org/korean>`_ - By Heungsub Lee :language:`Python`
    - Package for attaching particles (josa) in sentences
- `go_hangul <https://github.com/suapapa/go_hangul>`_ (2012) - By Homin Lee :language:`Go` :license:`BSD`
    - Tools for Hangul manipulation `[docs] <https://godoc.org/github.com/suapapa/go_hangul>`_
- `Speller <http://speller.cs.pusan.ac.kr/>`_ (부산대)


.. [1] https://wiki.kldp.org/wiki.php/KTS
