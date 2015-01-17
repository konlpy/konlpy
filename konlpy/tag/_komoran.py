#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys

try:
    import jpype
except ImportError:
    pass

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

        from konlpy.tag import Komoran

        komoran = Komoran()
        print komoran.pos(u'우왕 코모란도 오픈소스가 되었어요')

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    :param dicpath: The path of dictionary files. The KOMORAN system dictionary is loaded by default.
    """

    def pos(self, phrase, flatten=True):
        """POS tagger."""

        phrase = utils.preprocess(phrase)
        if sys.version_info[0] < 3:
            result = self.jki.analyzeMorphs(phrase, self.dicpath)
        else:
            result = self.jki.analyzeMorphs3(phrase, self.dicpath).toString()

        return parse(result, flatten)


    def nouns(self, phrase):
        """Noun extractor."""

        tagged = self.pos(phrase)
        return [s for s, t in tagged if t.startswith('N')]


    def __init__(self, jvmpath=None, dicpath=None):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath)
        komoranJavaPackage = jpype.JPackage('kr.lucypark.komoran')
        KomoranInterfaceJavaClass = komoranJavaPackage.KomoranInterface
        try:
            self.jki = KomoranInterfaceJavaClass()
        except TypeError: # Package kr.lucypark.komoran.KomoranInterface is not Callable
            raise IOError("Please download komoran-dic: `konlpy.download('komoran-dic')`")

        if dicpath:
            self.dicpath = dicpath
        else:
            # FIXME: Cannot execute without sudoing
            # java.lang.NoClassDefFoundErrorPyRaisable: java.lang.NoClassDefFoundError: kr/co/shineware/nlp/komoran/core/analyzer/Komoran
            self.dicpath = os.path.join(utils.installpath, 'java', 'data', 'models')
