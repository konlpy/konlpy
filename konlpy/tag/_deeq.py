# -*- coding: utf-8 -*-

import sys
from deeq.deeq_nlp_client import BaikalLanguageServiceClient
from deeq.custom_dict_client import CustomDictionaryServiceClient


def read_dic_file(fn):
    dict_set = set()
    with open(fn, 'r') as r:
        while True:
            w = r.readline()
            if not w:
                break
            if w[0] != '#':
                w2 = w.strip()
                if len(w2) > 0:
                    dict_set.add(w2)
    return dict_set


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

    :param domain       : str. domain of newly added custom dict. 
                          There is no fixed name; users can set use any words according to their needs. (example : "law")
    :param np_dict      : str. path where np_dict text file exists 
                          (custom dict for noun. This dict will be included in designated domain.)
    :param cp_dict      : str. path where cp_dict text file exists 
                          (custom dict for compound noun. This dict will be included in designated domain.)
    :param caret_cp_dict: str. path where cp_dict text file exists 
                          (custom dict for separation of compound noun. This dict will be included in designated domain.)
    :param host         : str. host num
    :param port         : str. port num
    """

    def __init__(self, domain = None, np_dict = None, cp_dict = None, caret_cp_dict = None, host=None, port=None):

        if host is None:
            host = 'nlp.deeq.ai'
        if port is None:
            port = '5656'
        addr = host + ':' + port

        # Update customer dict.
        try:
            if domain is not None:
                np_set = read_dic_file(np_dict) if np_dict is not None else set()
                cp_set = read_dic_file(cp_dict) if cp_dict is not None else set()
                caret_cp_set = read_dic_file(caret_cp_dict) if caret_cp_dict is not None else set()
                dic_client = CustomDictionaryServiceClient(addr)
                res = dic_client.update(domain, np_set, cp_set, caret_cp_set)
                if res:
                    print(f"Domain {domain} is updated with np={len(np_set)}, cp={len(cp_set)}, caret={len(caret_cp_set)}.")
                else:
                    print(f"Domain {domain} was not updated!")
            else:
                print("To update customer dictionary, param domain should not be None.")
        except Exception as e:
            print(e)

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
