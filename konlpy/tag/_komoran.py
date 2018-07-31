# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

import jpype

from konlpy import jvm, utils


__all__ = ['Komoran']


class Komoran():
    """Wrapper for `KOMORAN <https://github.com/shin285/KOMORAN>`_.

    KOMORAN is a relatively new open source Korean morphological analyzer written in Java, developed by `Shineware <http://shineware.co.kr>`_, since 2013.

    .. code-block:: python

        >>> from konlpy.tag import Komoran
        >>> komoran = Komoran()
        >>> print(komoran.morphs(u'우왕 코모란도 오픈소스가 되었어요'))
        ['우왕', '코', '모란', '도', '오픈소스', '가', '되', '었', '어요']
        >>> print(komoran.nouns(u'오픈소스에 관심 많은 멋진 개발자님들!'))
        ['오픈소스', '관심', '개발자']
        >>> print(komoran.pos(u'원칙이나 기체 설계와 엔진·레이더·항법장비 등'))
        [('원칙', 'NNG'), ('이나', 'JC'), ('기체', 'NNG'), ('설계', 'NNG'), ('와', 'JC'), ('엔진', 'NNG'), ('·', 'SP'), ('레이더', 'NNG'), ('·', 'SP'), ('항법', 'NNP'), ('장비', 'NNG'), ('등', 'NNB')]

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    :param dicpath: The path of dictionary files. The KOMORAN system dictionary is loaded by default.
    """

    def pos(self, phrase, flatten=True, join=False):
        """POS tagger.

        :param flatten: If False, preserves eojeols.
        :param join: If True, returns joined sets of morph and tag.
        """

        sentences = phrase.split('\n')
        morphemes = []
        if not sentences:
            return morphemes

        for sentence in sentences:
            result = self.jki.analyze(sentence).getTokenList()
            result = [(token.getMorph(), token.getPos()) for token in result]

            if join:
                result = ['{}/{}'.format(morph, pos) for morph, pos in result]

            morphemes.append(result)

        if flatten:
            return sum(morphemes, [])
        return morphemes

    def nouns(self, phrase):
        """Noun extractor."""

        tagged = self.pos(phrase)
        return [s for s, t in tagged if t.startswith('NN')]

    def morphs(self, phrase):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase)]

    def add_userdic_file(self, dicpath):
        """
        Arguments
        ---------
        dicpath : str
            dictionary file path
        """
        self.jki.setUserDic(dicpath)

    def __init__(self, jvmpath=None, modelpath=None):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath)

        if modelpath:
            self.modelpath = modelpath
        else:
            # FIXME: Cannot execute without sudoing
            # java.lang.NoClassDefFoundErrorPyRaisable: java.lang.NoClassDefFoundError: kr/co/shineware/nlp/komoran/core/analyzer/Komoran
            self.modelpath = os.path.join(utils.installpath, 'java', 'data', 'models')
        self.tagset = utils.read_json('%s/data/tagset/komoran.json' % utils.installpath)

        komoranJavaPackage = jpype.JPackage('kr.co.shineware.nlp.komoran.core')

        try:
            self.jki = komoranJavaPackage.Komoran(self.modelpath)
        except TypeError:  # Package kr.lucypark.komoran.KomoranInterface is not Callable
            raise IOError("Cannot access komoran-dic. Please leave an issue at https://github.com/konlpy/konlpy/issues")
