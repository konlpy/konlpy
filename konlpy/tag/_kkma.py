#! /usr/bin/python
# -*- coding: utf-8 -*-

import re
try:
    import jpype
except ImportError:
    pass

from .. import jvm
from .. import utils


__all__ = ['Kkma']


class Kkma():
    """Wrapper for `Kkma <http://kkma.snu.ac.kr>`_.

    Kkma is a morphological analyzer and natural language processing system written in Java, developed by the Intelligent Data Systems (IDS) Laboratory at `SNU <http://snu.ac.kr>`_.

    .. code-block:: python

        from konlpy.tag import Kkma

        kkma = Kkma()
        print kkma.sentences(u'저는 대학생이구요. 소프트웨어 관련학과 입니다.')
        print kkma.nouns(u'대학에서 DB, 통계학, 이산수학 등을 배웠지만...')
        print kkma.morphs(u'자주 사용을 안하다보니 모두 까먹은 상태입니다.')
        print kkma.pos(u'어쩌면 좋죠?')

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    """

    def nouns(self, phrase):
        """Noun extractor."""

        phrase = utils.preprocess(phrase)
        nouns = self.jki.extractNoun(phrase)
        if not nouns: return []
        return [nouns.get(i).getString() for i in range(nouns.size())]

    def pos(self, phrase, flatten=True):
        """POS tagger."""

        phrase = utils.preprocess(phrase)
        sentences = self.jki.morphAnalyzer(phrase)
        morphemes = []
        if not sentences: return morphemes

        for i in range(sentences.size()):
            sentence = sentences.get(i)
            for j in range(sentence.size()):
                eojeol = sentence.get(j)
                if flatten:
                    for k in range(eojeol.size()):
                        morpheme = eojeol.get(k)
                        morphemes.append((morpheme.getString(), morpheme.getTag()))
                else:
                    morphemes.append([(eojeol.get(k).getString(), eojeol.get(k).getTag())\
                                     for k in range(eojeol.size())])

        return morphemes

    def morphs(self, phrase):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase)]

    def sentences(self, phrase):
        """Sentence detection."""

        phrase = utils.preprocess(phrase)
        sentences = self.jki.morphAnalyzer(phrase)
        if not sentences: return []
        return [sentences.get(i).getSentence() for i in range(sentences.size())]


    def __init__(self, jvmpath=None):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath)

        kkmaJavaPackage = jpype.JPackage('kr.lucypark.kkma')
        KkmaInterfaceJavaClass = kkmaJavaPackage.KkmaInterface
        self.jki = KkmaInterfaceJavaClass() # Java instance
