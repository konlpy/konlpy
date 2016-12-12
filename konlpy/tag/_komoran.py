#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys

import jpype

from .. import jvm
from .. import utils
from .. import internals


__all__ = ['Komoran']


def parse(result, flatten):
    def _parse(token):
        return [tuple(s[1:].rsplit('/', 1)) for s in re.findall('\+.+?/[A-Z]+', token)]

    if sys.version_info[0] < 3:
        parsed = [[tuple(r.rsplit('/', 1)) for r in sublist] for sublist in result]
    else:
        parsed = [_parse(i) for i in result[1:-1].split(', ')]

    if flatten:
        return sum(parsed, [])
    return parsed


class Komoran():
    """Wrapper for `KOMORAN <http://shineware.tistory.com/entry/KOMORAN-ver-24>`_.

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

    def pos(self, phrase, flatten=True):
        """POS tagger.

        :param flatten: If False, preserves eojeols."""

        if sys.version_info[0] < 3:
            result = self.jki.analyzeMorphs(phrase, self.dicpath)
        else:
            result = self.jki.analyzeMorphs3(phrase, self.dicpath).toString()

        return parse(result, flatten)

    def nouns(self, phrase):
        """Noun extractor."""

        tagged = self.pos(phrase)
        return [s for s, t in tagged if t.startswith('NN')]

    def morphs(self, phrase):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase)]

    def __init__(self, jvmpath=None, dicpath=None):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath)
        komoranJavaPackage = jpype.JPackage('kr.lucypark.komoran')
        KomoranInterfaceJavaClass = komoranJavaPackage.KomoranInterface
        try:
            self.jki = KomoranInterfaceJavaClass()
        except TypeError:  # Package kr.lucypark.komoran.KomoranInterface is not Callable
            raise IOError("Cannot access komoran-dic. Please leave an issue at https://github.com/konlpy/konlpy/issues")

        if dicpath:
            self.dicpath = dicpath
        else:
            # FIXME: Cannot execute without sudoing
            # java.lang.NoClassDefFoundErrorPyRaisable: java.lang.NoClassDefFoundError: kr/co/shineware/nlp/komoran/core/analyzer/Komoran
            self.dicpath = os.path.join(utils.installpath, 'java', 'data', 'models')
            self.tagset = utils.read_json('%s/data/tagset/komoran.json' % utils.installpath)
