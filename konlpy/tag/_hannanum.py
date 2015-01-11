#! /usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re
try:
    import jpype
except ImportError:
    pass

from .. import jvm
from .. import utils


__all__ = ['Hannanum']


tag_re = '(.+?\\/\\w+)\\+?'

def parse(result, flatten=False):
    def parse_opt(opt):
        return [tuple(u.rsplit('/', 1))\
                    for u in re.findall(tag_re, opt.strip())]

    if not result: return []

    elems = result.strip().splitlines()
    index = [i for i, e in enumerate(elems) if not e]
    parts = utils.partition(elems, index)

    if flatten:
        return sum([parse_opt(opt) for part in parts\
                for opt in list(filter(None, part))[1:]], [])
    else:
        return [[parse_opt(opt) for opt in list(filter(None, part))[1:]]\
                for part in parts]


class Hannanum():
    """Wrapper for `JHannanum <http://semanticweb.kaist.ac.kr/home/index.php/HanNanum>`_.

    JHannanum is a morphological analyzer and POS tagger written in Java, and developed by the `Semantic Web Research Center (SWRC) <http://semanticweb.kaist.ac.kr/>`_ at KAIST since 1999.

    .. code-block:: python

        from konlpy.tag import Hannanum

        hannanum = Hannanum()
        print hannanum.analyze(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.')
        print hannanum.nouns(u'다람쥐 헌 쳇바퀴에 타고파')
        print hannanum.pos(u'웃으면 더 행복합니다!')
        print hannanum.morphs(u'웃으면 더 행복합니다!')

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    """

    def analyze(self, phrase):
        """Phrase analyzer.

        This analyzer returns various morphological candidates for each token.
        It consists of two parts: 1) Dictionary search (chart), 2) Unclassified term segmentation.
        """

        phrase = utils.preprocess(phrase)
        result = self.jhi.morphAnalyzer(phrase)
        return parse(result)

    def nouns(self, phrase):
        """Noun extractor."""

        phrase = utils.preprocess(phrase)
        return list(self.jhi.extractNoun(phrase))

    def pos(self, phrase, ntags=9, flatten=True):
        """POS tagger.

        This tagger is HMM based, and calculates the probability of tags.

        :param ntags: The number of tags. It can be either 9 or 22."""

        phrase = utils.preprocess(phrase)
        if ntags==9:
            result = self.jhi.simplePos09(phrase)
        elif ntags==22:
            result = self.jhi.simplePos22(phrase)
        else:
            raise Exception('ntags in [9, 22]')
        return parse(result, flatten=flatten)

    def morphs(self, phrase):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase)]

    def __init__(self, jvmpath=None):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath)

        jhannanumJavaPackage = jpype.JPackage('kr.lucypark.jhannanum.comm')
        HannanumInterfaceJavaClass = jhannanumJavaPackage.HannanumInterface
        self.jhi = HannanumInterfaceJavaClass() # Java instance
