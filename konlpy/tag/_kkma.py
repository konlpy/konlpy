# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re
import jpype

from konlpy import jvm, utils


__all__ = ['Kkma']


class Kkma():
    """Wrapper for `Kkma <http://kkma.snu.ac.kr>`_.

    Kkma is a morphological analyzer and natural language processing
    system written in Java, developed by the Intelligent Data Systems (IDS)
    Laboratory at `SNU <http://snu.ac.kr>`_.

    .. code-block:: python

        >>> from konlpy.tag import Kkma
        >>> kkma = Kkma()
        >>> print(kkma.morphs(u'공부를 하면할수록 모르는게 많다는 것을 알게 됩니다.'))
        ['공부', '를', '하', '면', '하', 'ㄹ수록', '모르', '는', '것', '이', '많', '다는', '것', '을', '알', '게', '되', 'ㅂ니다', '.']
        >>> print(kkma.nouns(u'대학에서 DB, 통계학, 이산수학 등을 배웠지만...'))
        ['대학', '통계학', '이산', '이산수학', '수학', '등']
        >>> print(kkma.pos(u'다 까먹어버렸네요?ㅋㅋ'))
        [('다', 'MAG'), ('까먹', 'VV'), ('어', 'ECD'), ('버리', 'VXV'), ('었', 'EPT'), ('네요', 'EFN'), ('?', 'SF'), ('ㅋㅋ', 'EMO')]
        >>> print(kkma.sentences(u'그래도 계속 공부합니다. 재밌으니까!'))
        ['그래도 계속 공부합니다.', '재밌으니까!']

    .. warning::

        There are reports that ``Kkma()`` is weak for long strings with no spaces between words. See issue :issue:`73` for details.

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    :param max_heap_size: Maximum memory usage limitation (Megabyte) :py:func:`.init_jvm`.
    """

    def nouns(self, phrase):
        """Noun extractor."""

        nouns = self.jki.extractNoun(phrase)
        if not nouns: return []
        return [nouns.get(i).getString() for i in range(nouns.size())]

    def pos(self, phrase, flatten=True, join=False):
        """POS tagger.

        :param flatten: If False, preserves eojeols.
        :param join: If True, returns joined sets of morph and tag.
        """

        sentences = self.jki.morphAnalyzer(phrase)
        morphemes = []
        if not sentences:
            return morphemes

        for i in range(sentences.size()):
            sentence = sentences.get(i)
            for j in range(sentence.size()):
                eojeol = sentence.get(j)
                if flatten:
                    for k in range(eojeol.size()):
                        morpheme = eojeol.get(k)
                        if join:
                            morphemes.append(morpheme.getString() + '/' + morpheme.getTag())
                        else:
                            morphemes.append((morpheme.getString(), morpheme.getTag()))
                else:
                    if join:
                        morphemes.append([eojeol.get(k).getString() + '/' + eojeol.get(k).getTag()
                                         for k in range(eojeol.size())])
                    else:
                        morphemes.append([(eojeol.get(k).getString(), eojeol.get(k).getTag())
                                         for k in range(eojeol.size())])

        return morphemes

    def morphs(self, phrase):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase)]

    def sentences(self, phrase):
        """Sentence detection."""

        sentences = self.jki.morphAnalyzer(phrase)
        if not sentences: return []
        return [sentences.get(i).getSentence() for i in range(sentences.size())]

    def __init__(self, jvmpath=None, max_heap_size=1024):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath, max_heap_size)

        kkmaJavaPackage = jpype.JPackage('kr.lucypark.kkma')
        KkmaInterfaceJavaClass = kkmaJavaPackage.KkmaInterface
        self.jki = KkmaInterfaceJavaClass()  # Java instance
        self.tagset = utils.read_json('%s/data/tagset/kkma.json' % utils.installpath)
