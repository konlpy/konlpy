#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

try:
    from MeCab import Tagger
except ImportError:
    pass
from .. import utils


__all__ = ['Mecab']


attrs = ['tags', # 품사 태그
         'semantic', # 의미 부류
         'has_jongsung', # 종성 유무
         'read', # 읽기
         'type', # 타입
         'first_pos', # 첫번째 품사
         'last_pos', # 마지막 품사
         'original', # 원형
         'indexed'] # 인덱스 표현

def parse(result, allattrs=False):
    def split(elem):
        if not elem: return ('','SY')
        s, t = elem.split('\t')
        return (s, t.split(',', 1)[0])

    return [split(elem) for elem in result.splitlines()[:-1]]

class Mecab():
    """Wrapper for MeCab-ko morphological analyzer.

    `MeCab`_, originally a Japanese morphological analyzer and a POS tagger developed by the Graduate School of Informatics in Kyoto University, was modified to MeCab-ko by the `Eunjeon Project`_ to adapt to the Korean language.

    In order to use MeCab-ko within KoNLPy, follow the directions in :ref:`optional-installations`.

    .. code-block:: python
        :emphasize-lines: 2

        from konlpy.tag import Mecab
        # MeCab installation needed

        mecab = Mecab()
        print mecab.pos(u'자연주의 쇼핑몰은 어떤 곳인가?')
        print mecab.morphs(u'영등포구청역에 있는 맛집 좀 알려주세요.')
        print mecab.nouns(u'우리나라에는 무릎 치료를 잘하는 정형외과가 없는가!')

    :param dicpath: The path of the MeCab-ko dictionary.

    .. _MeCab: https://code.google.com/p/mecab/
    .. _Eunjeon Project: http://eunjeon.blogspot.kr/
    """

    # TODO: check whether flattened results equal non-flattened
    def pos(self, phrase, flatten=True):
        """POS tagger."""

        if sys.version_info[0] < 3:
            phrase = utils.preprocess(phrase).encode('utf-8')
            if flatten:
                result = self.tagger.parse(phrase).decode('utf-8')
                return parse(result)
            else:
                return [parse(self.tagger.parse(eojeol).decode('utf-8'))\
                        for eojeol in phrase.split()]
        else:
            phrase = utils.preprocess(phrase)
            if flatten:
                result = self.tagger.parse(phrase)
                return parse(result)
            else:
                return [parse(self.tagger.parse(eojeol).decode('utf-8'))\
                        for eojeol in phrase.split()]

    def morphs(self, phrase):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase)]

    def nouns(self, phrase):
        """Noun extractor."""

        tagged = self.pos(phrase)
        return [s for s, t in tagged if t.startswith('N')]


    def __init__(self, dicpath='/usr/local/lib/mecab/dic/mecab-ko-dic'):
        try:
            self.tagger = Tagger('-d %s' % dicpath)
        except RuntimeError:
            raise Exception('Invalid MeCab dictionary path: "%s"\nInput the correct path when initiializing class: "Mecab(\'/some/dic/path\')"' % dicpath)
