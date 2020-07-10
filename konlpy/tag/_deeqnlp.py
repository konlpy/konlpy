#!/usr/bin/env python3

import sys
from deeq_nlp_client import BaikalLanguageServiceClient

class DeeqNlp():
    """Wrapper for `deeq-nlp v1.2.1 <https://github.com/deeq-ai>`_.
    'DeeqNlp' is a morphological analyzer developed by Baikal-ai.

    In order to use DeeqNlp within KoNLPy, follow the directions in
    :ref:`optional-installations`.

    .. code-block:: python
        :emphasize-lines: 1

        >>> from konlpy.tag import DeeqNlp
        >>> dqnlp = DeeqNlp()
        >>> print(dqnlp.morphs('안녕하세요, 만나서 반갑습니다.'))
        ['안녕', '하', '시', '어요', ',', '만나', '아서', '반갑', '습니다', '.']
        >>> print(dqnlp.nouns('나비 허리에 새파란 초생달이 시리다.'))
        ['나비', '허리', '초생달']
        >>> print(dqnlp.pos('햇빛이 선명하게 나뭇잎을 핥고 있었다.'))
        [('햇빛', 'NNG'), ('이', 'JKS'), ('선명', 'NNG'), ('하', 'XSA'), ('게', 'EC'), ('나뭇잎', 'NNG'),
         ('을', 'JKO'), ('핥', 'VV'), ('고', 'EC'), ('있', 'VX'), ('었', 'EP'), ('다', 'EF'), ('.', 'SF')]
    """

    def __init__(self):
        self.client = BaikalLanguageServiceClient("220.72.157.144:5656")

    def pos(self, phrase, flatten=True, join=False):
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
        return [m for (m, l) in self.pos(phrase)]

    def nouns(self, phrase):
        return[s for (s,t) in self.pos(phrase) if t.startswith('N')]
    
