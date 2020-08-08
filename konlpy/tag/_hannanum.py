# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import re

import jpype

from konlpy import jvm, utils
from konlpy.tag._common import validate_phrase_inputs


__all__ = ['Hannanum']


tag_re = '(.+?\\/\\w+)\\+?'


def parse(result, flatten=False, join=False):
    def parse_opt(opt, join=False):
        if join:
            return [u for u in re.findall(tag_re, opt.strip())]
        else:
            return [tuple(u.rsplit('/', 1)) for u in re.findall(tag_re, opt.strip())]

    if not result:
        return []

    elems = result.strip().splitlines()
    index = [i for i, e in enumerate(elems) if not e]
    parts = utils.partition(elems, index)

    if flatten:
        return sum([parse_opt(opt, join=join) for part in parts
                    for opt in list(filter(None, part))[1:]], [])
    else:
        return [[parse_opt(opt, join=join) for opt in list(filter(None, part))[1:]]
                for part in parts]


class Hannanum():
    """
    Wrapper for `JHannanum <http://semanticweb.kaist.ac.kr/home/index.php/HanNanum>`_.

    JHannanum is a morphological analyzer and POS tagger written in Java,
    and developed by the
    `Semantic Web Research Center (SWRC) <http://semanticweb.kaist.ac.kr/>`_
    at KAIST since 1999.

    .. code-block:: python

        >>> from konlpy.tag import Hannanum
        >>> hannanum = Hannanum()
        >>> print(hannanum.analyze(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
        [[[('롯데마트', 'ncn'), ('의', 'jcm')], [('롯데마트의', 'ncn')], [('롯데마트', 'nqq'), ('의', 'jcm')], [('롯데마트의', 'nqq')]], [[('흑마늘', 'ncn')], [('흑마늘', 'nqq')]], [[('양념', 'ncn')]], [[('치킨', 'ncn'), ('이', 'jcc')], [('치킨', 'ncn'), ('이', 'jcs')], [('치킨', 'ncn'), ('이', 'ncn')]], [[('논란', 'ncpa'), ('이', 'jcc')], [('논란', 'ncpa'), ('이', 'jcs')], [('논란', 'ncpa'), ('이', 'ncn')]], [[('되', 'nbu'), ('고', 'jcj')], [('되', 'nbu'), ('이', 'jp'), ('고', 'ecc')], [('되', 'nbu'), ('이', 'jp'), ('고', 'ecs')], [('되', 'nbu'), ('이', 'jp'), ('고', 'ecx')], [('되', 'paa'), ('고', 'ecc')], [('되', 'paa'), ('고', 'ecs')], [('되', 'paa'), ('고', 'ecx')], [('되', 'pvg'), ('고', 'ecc')], [('되', 'pvg'), ('고', 'ecs')], [('되', 'pvg'), ('고', 'ecx')], [('되', 'px'), ('고', 'ecc')], [('되', 'px'), ('고', 'ecs')], [('되', 'px'), ('고', 'ecx')]], [[('있', 'paa'), ('다', 'ef')], [('있', 'px'), ('다', 'ef')]], [[('.', 'sf')], [('.', 'sy')]]]
        >>> print(hannanum.morphs(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
        ['롯데마트', '의', '흑마늘', '양념', '치킨', '이', '논란', '이', '되', '고', '있', '다', '.']
        >>> print(hannanum.nouns(u'다람쥐 헌 쳇바퀴에 타고파'))
        ['다람쥐', '쳇바퀴', '타고파']
        >>> print(hannanum.pos(u'웃으면 더 행복합니다!'))
        [('웃', 'P'), ('으면', 'E'), ('더', 'M'), ('행복', 'N'), ('하', 'X'), ('ㅂ니다', 'E'), ('!', 'S')]

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    :param max_heap_size: Maximum memory usage limitation (Megabyte) :py:func:`.init_jvm`.
    """

    def __init__(self, jvmpath=None, max_heap_size=1024):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath, max_heap_size)

        jhannanumJavaPackage = jpype.JPackage('kr.lucypark.jhannanum.comm')
        HannanumInterfaceJavaClass = jhannanumJavaPackage.HannanumInterface
        self.jhi = HannanumInterfaceJavaClass()  # Java instance
        self.tagset = utils.read_json('%s/data/tagset/hannanum.json' % utils.installpath)

    def analyze(self, phrase):
        """Phrase analyzer.

        This analyzer returns various morphological candidates for each token.
        It consists of two parts: 1) Dictionary search (chart),
        2) Unclassified term segmentation.
        """

        result = self.jhi.morphAnalyzer(phrase)
        return parse(result)

    def pos(self, phrase, ntags=9, flatten=True, join=False):
        """POS tagger.

        This tagger is HMM based, and calculates the probability of tags.

        :param ntags: The number of tags. It can be either 9 or 22.
        :param flatten: If False, preserves eojeols.
        :param join: If True, returns joined sets of morph and tag.
        """
        validate_phrase_inputs(phrase)

        if ntags == 9:
            result = self.jhi.simplePos09(phrase)
        elif ntags == 22:
            result = self.jhi.simplePos22(phrase)
        else:
            raise Exception('ntags in [9, 22]')
        return parse(result, flatten=flatten, join=join)

    def nouns(self, phrase):
        """Noun extractor."""

        tagged = self.pos(phrase)
        return [s for s, t in tagged if t.startswith('N')]

    def morphs(self, phrase):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase)]
