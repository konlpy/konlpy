# -*- coding: utf-8 -*-

import sys
from deeq.deeq_nlp_client import BaikalLanguageServiceClient


class Deeq():
    """Wrapper for `deeq-nlp v1.2.1 <https://github.com/deeq-ai>`_.
    'Deeq' is a morphological analyzer developed by Baikal-ai.

    In order to use Deeq within KoNLPy, follow the directions in
    :ref:`optional-installations`.

    .. code-block:: python
        :emphasize-lines: 1

        >>> from konlpy.tag import Deeq
        >>> deeq = Deeq()
        >>> print(deeq.morphs('안녕하세요, 반갑습니다.'))
        ['안녕', '하', '시', '어요', ',', '반갑', '습니다', '.']
        >>> print(deeq.nouns('나비 허리에 새파란 초생달이 시리다.'))
        ['나비', '허리', '초생달']
        >>> print(deeq.pos('햇빛이 선명하게 나뭇잎을 핥고 있었다.'))
        [('햇빛', 'NNG'), ('이', 'JKS'), ('선명', 'NNG'), ('하', 'XSA'), ('게', 'EC'), ('나뭇잎', 'NNG'),
         ('을', 'JKO'), ('핥', 'VV'), ('고', 'EC'), ('있', 'VX'), ('었', 'EP'), ('다', 'EF'), ('.', 'SF')]

    :param host : host num
    :param port : port num
    """

    def __init__(self, host=None, port=None):
        if host is None:
            host = 'nlp.deeq.ai'
        if port is None:
            port = '5656'
        addr = host + ':' + port
        self.client = BaikalLanguageServiceClient(addr)


    def pos(self, phrase, flatten=True, join=False):
        """POS tagger.
        :param flatten : If False, returns original morphs.
        :param join    : If True, returns joined sets of morph and tag.
        """
        if len(phrase) is 0:
            print("OOPS, no sentences.")        
            return []
        res = self.client.analyze_syntax(phrase)
        res = [token.tagged.split('+') for token in res.sentences[0].tokens]        
        if join:
            res = [m for token in res for m in token]
        if flatten:
            res = [tuple(m.split('/')) for token in res for m in token]
        return res


    def morphs(self, phrase):
        """Parse phrase to morphemes."""
        return [m for (m, l) in self.pos(phrase)]


    def nouns(self, phrase):
        """Noun extractor."""
        return[s for (s,t) in self.pos(phrase) if t.startswith('N')]
