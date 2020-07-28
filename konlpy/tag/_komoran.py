# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import os

import jpype

from konlpy import jvm, utils
from konlpy.tag._common import validate_phrase_inputs


__all__ = ['Komoran']


class Komoran():
    """Wrapper for `KOMORAN <https://github.com/shin285/KOMORAN>`_.

    KOMORAN is a relatively new open source Korean morphological analyzer written in Java, developed by `Shineware <http://shineware.co.kr>`_, since 2013.

    .. code-block:: python

        >>> cat /tmp/dic.txt  # Place a file in a location of your choice
        코모란	NNP
        오픈소스	NNG
        바람과 함께 사라지다	NNP
        >>> from konlpy.tag import Komoran
        >>> komoran = Komoran(userdic='/tmp/dic.txt')
        >>> print(komoran.morphs(u'우왕 코모란도 오픈소스가 되었어요'))
        ['우왕', '코모란', '도', '오픈소스', '가', '되', '었', '어요']
        >>> print(komoran.nouns(u'오픈소스에 관심 많은 멋진 개발자님들!'))
        ['오픈소스', '관심', '개발자']
        >>> print(komoran.pos(u'혹시 바람과 함께 사라지다 봤어?'))
        [('혹시', 'MAG'), ('바람과 함께 사라지다', 'NNP'), ('보', 'VV'), ('았', 'EP'), ('어', 'EF'), ('?', 'SF')]

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    :param userdic: The path to the user dictionary.

        This enables the user to enter custom tokens or phrases, that are mandatorily assigned to tagged as a particular POS.
        Each line of the dictionary file should consist of a token or phrase, followed by a POS tag, which are delimited with a `<tab>` character.

        An example of the file format is as follows:

        .. code-block:: python

            바람과 함께 사라지다	NNG
            바람과 함께	NNP
            자연어	NNG

        If a particular POS is not assigned for a token or phrase, it will be tagged as NNP.
    :param modelpath: The path to the Komoran HMM model.
    :param max_heap_size: Maximum memory usage limitation (Megabyte) :py:func:`.init_jvm`.
    """

    def __init__(self, jvmpath=None, userdic=None, modelpath=None, max_heap_size=1024):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath, max_heap_size)

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

        if userdic:
            self.jki.setUserDic(userdic)

    def pos(self, phrase, flatten=True, join=False):
        """POS tagger.

        :param flatten: If False, preserves eojeols.
        :param join: If True, returns joined sets of morph and tag.
        """
        validate_phrase_inputs(phrase)

        sentences = phrase.split('\n')
        morphemes = []
        if not sentences:
            return morphemes

        for sentence in sentences:
            if not sentence:
                continue
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
