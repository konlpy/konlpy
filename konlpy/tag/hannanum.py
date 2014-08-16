#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
try:
    import jpype
except ImportError:
    pass

from .. import utils


__all__ = ['Hannanum']


tag_re = ur'(.+?\/\w+)\+?'

def parse(result, flatten=False):
    def parse_opt(opt):
        return [tuple(u.rsplit('/', 1))\
                    for u in re.findall(tag_re, opt.strip())]

    elems = result.strip().splitlines()
    index = [i for i, e in enumerate(elems) if not e]
    parts = utils.partition(elems, index)

    if flatten:
        return sum([parse_opt(opt) for part in parts\
                for opt in filter(None, part)[1:]], [])
    else:
        return [[parse_opt(opt) for opt in filter(None, part)[1:]]\
                for part in parts]


class Hannanum():
    """Wrapper for Hannanum morphological analyzer.

    `Hannanum`_ is a morphological analyzer and a POS tagger written in Java, developed by the `Semantic Web Research Center (SWRC)`_ in KAIST since 1999.
    It requires a JRE, and therefore requires the user to :py:func:`.init_jvm` e.g.

    .. code-block:: python
        :emphasize-lines: 4

        from konlpy import init_jvm
        from konlpy.tag import Hannanum

        init_jvm()
        hannanum = Hannanum()

        print hannanum.morph(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.')
        print hannanum.pos(u'웃으면 더 행복합니다!')
        print hannanum.nouns(u'다람쥐 헌 쳇바퀴에 타고파')

    :param jvmpath: The path of the JVM. If left empty, inferred by jpype.getDefaultJVMPath().


    .. _Hannanum: http://semanticweb.kaist.ac.kr/home/index.php/HanNanum
    .. _Semantic Web Research Center (SWRC): http://semanticweb.kaist.ac.kr/
    """

    def morph(self, phrase):
        """Morphological analyzer."""

        phrase = utils.preprocess(phrase)
        result = self.jhi.morphAnalyzer(phrase)
        return parse(result)

    def nouns(self, phrase):
        """Noun extractor."""

        phrase = utils.preprocess(phrase)
        return list(self.jhi.extractNoun(phrase))

    def pos(self, phrase, ntags=9):
        """POS tagger. The number of tags (`ntags`), can be either 9 or 22."""

        phrase = utils.preprocess(phrase)
        if ntags==9:
            result = self.jhi.simplePos09(phrase)
        elif ntags==22:
            result = self.jhi.simplePos22(phrase)
        else:
            raise Exception('ntags in [9, 22]')
        return parse(result, flatten=True)

    def __init__(self, jvmpath=None):
        jhannanumJavaPackage = jpype.JPackage('kr.lucypark.jhannanum.comm')
        HannanumInterfaceJavaClass = jhannanumJavaPackage.HannanumInterface
        self.jhi = HannanumInterfaceJavaClass() # Java instance


if __name__=='__main__':
    from init_jvm import init_jvm
    from pprint import pprint

    phrase = u'(학교에서조차도) 1/2+3/2이 2이라는 사실을 모르고 있었다!'

    init_jvm()
    hi = Hannanum()

    print '\nMorph:'; pprint(hi.morph(phrase))
    print '\nNouns:'; pprint(hi.nouns(phrase))
    print '\nPos09:'; pprint(hi.pos(phrase))
    print '\nPos22:'; pprint(hi.pos(phrase, ntags=22))
