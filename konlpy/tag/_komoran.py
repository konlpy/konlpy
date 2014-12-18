#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

try:
    import jpype
except ImportError:
    pass

from .. import jvm
from .. import utils


__all__ = ['Komoran']


def parse(result, flatten=False):
    if flatten:
        return [r.rsplit('/', 1) for sublist in result for r in sublist]
    else:
        return [[r.rsplit('/', 1) for r in sublist] for sublist in result]


class Komoran():
    """Wrapper for `KOMORAN <http://shineware.tistory.com/entry/KOMORAN-ver-24>`_.

    KOMORAN is a relatively new open source Korean morphological analyzer written in Java, developed by `Shineware <http://shineware.co.kr>`_, since 2013.

    .. code-block:: python

        from konlpy.tag import Komoran

        komoran = Komoran()
        print komoran.pos(u'우왕 코모란도 오픈소스가 되었어요')

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    :param dicpath: The path of dictionary files.
    """

    def pos(self, phrase, flatten=True):
        """POS tagger."""

        # TODO: consider Python version

        phrase = utils.preprocess(phrase)
        result = self.jki.analyzeMorphs(phrase, self.dicpath)

        return parse(result, flatten)

    def nouns(self, phrase):
        """Noun extractor."""

        tagged = self.pos(phrase)
        return [s for s, t in tagged if t.startswith('N')]

    def __init__(self, jvmpath=None, dicpath='%s/java/data/models' % utils.installpath):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath)

        komoranJavaPackage = jpype.JPackage('kr.lucypark.komoran')
        KomoranInterfaceJavaClass = komoranJavaPackage.KomoranInterface
        self.jki = KomoranInterfaceJavaClass()
        self.dicpath = dicpath
