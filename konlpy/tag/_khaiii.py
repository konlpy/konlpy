# -*- coding: utf-8 -*-
from khaiii import KhaiiiApi


class Khaiii():
    """
    Wrapper for `Kakao Hangul Analyzer III <https://github.com/kakao/khaiii>`_.

    `Khaiii`_, is a morphological analyzer developed by Kakao.

    In order to use Khaiii within KoNLPy, follow the directions in
    :ref:`optional-installations`.

    .. code-block:: python
        :emphasize-lines: 1

        >>> from konlpy.tag import Khaiii
        >>> khaiii = Khaiii()
        >>> print(khaiii.morphs('단순함이 궁극의 정교함이다.'))
        ['단순', '하', 'ㅁ', '이', '궁극', '의', '정교', '하', 'ㅁ', '이', '다', '.']
        >>> print(khaiii.nouns('말은 쉽지. 코드를 보여줘.'))
        ['말', '코드']
        >>> print(khaiii.pos('인생은 짧고 고양이는 귀엽다.'))
        [('인생', 'NNG'), ('은', 'JX'), ('짧', 'VA'), ('고', 'EC'), ('고양이', 'NNG'), ('는', 'JX'), ('귀엽', 'VA'), ('다', 'EF'), ('.', 'SF')]

    .. _Khaiii: https://github.com/kakao/khaiii
    """

    def __init__(self):
        self.tagger = KhaiiiApi()

    def pos(self, phrase, flatten=True, join=False):
        result = self.tagger.analyze(phrase)
        result = [[(morph.lex, morph.tag) for morph in word.morphs] for word in result]
        if join:
            result = [['/'.join(morph) for morph in word] for word in result]
        if flatten:
            result = [item for sublist in result for item in sublist]

        return result

    def morphs(self, phrase):
        return [s for s, t in self.pos(phrase)]

    def nouns(self, phrase):
        tagged = self.pos(phrase)
        return [s for s, t in tagged if t.startswith('N')]
