#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import codecs
import os
import pprint as pp


installpath = os.path.dirname(os.path.realpath(__file__))
replace_set = [
        (u'·', u'/'), # \xb7
        (u'․', u'/'), # \u2024
        (u'ㆍ', u'/'), # \u318d (hangul letter araea)
        (u'･', u'/'), # \uff65 (katakana)
        (u'～', u'~'), # \uff5e
        (u'❑', u'-'), # \u2751
        (u'‘', u"'"), # \u2018
        (u'’', u"'"), # \u2019
        (u'“', u'"'), # \u201c
        (u'”', u'"'), # \u201d
        (u'「', u'<'), # \u300c
        (u'」', u'>')] # \u300d

class UnicodePrinter(pp.PrettyPrinter):
    def format(self, object, context, maxlevels, level):
        """Overrided method to enable Unicode pretty print."""
        if isinstance(object, unicode):
            return (object.encode('utf8'), True, False)
        return pp.PrettyPrinter.format(self, object, context, maxlevels, level)

def concordance(phrase, text):
    """Find concordances of a phrase in a text.

    The farmost left numbers are indices, that indicate the location of the phrase in the text (by means of tokens). The following string, is part of the text surrounding the phrase for the given index.

    .. code-block:: python

        >>> from konlpy.corpus import kolaw
        >>> from konlpy.tag import Mecab
        >>> from konlpy import utils
        >>> constitution = kolaw.open('constitution.txt').read()
        >>> idx = utils.concordance(u'대한민국', constitution)
        0       대한민국헌법 유구한 역사와
        9       대한국민은 3·1운동으로 건립된 대한민국임시정부의 법통과 불의에
        98      총강 제1조 ① 대한민국은 민주공화국이다. ②대한민국의
        100     ① 대한민국은 민주공화국이다. ②대한민국의 주권은 국민에게
        110     나온다. 제2조 ① 대한민국의 국민이 되는
        126     의무를 진다. 제3조 대한민국의 영토는 한반도와
        133     부속도서로 한다. 제4조 대한민국은 통일을 지향하며,
        147     추진한다. 제5조 ① 대한민국은 국제평화의 유지에
        787     군무원이 아닌 국민은 대한민국의 영역안에서는 중대한
        1836    파견 또는 외국군대의 대한민국 영역안에서의 주류에
        3620    경제 제119조 ① 대한민국의 경제질서는 개인과
        >>> idx
        [0, 9, 98, 100, 110, 126, 133, 147, 787, 1836, 3620]
    """

    terms = text.split()
    indexes = [i for i, term in enumerate(terms) if phrase in term]
    for i in indexes:
        print i, ' '.join(terms[max(0, i-3):i+3])
    return indexes

def concat(phrase):
    """Concatenates lines into a unified string."""
    return phrase.replace(os.linesep, ' ')

def partition(list_, indices):
    """Partitions a list to several parts using indices.

    :param list_: The target list.
    :param indices: Indices to partition the target list.
    """
    return [list_[i:j] for i, j in zip([0]+indices, indices+[None])]

def pprint(obj):
    """Unicode pretty printer.

    .. code-block:: python

        >>> import pprint, konlpy
        >>> pprint.pprint([u"Print", u"유니코드", u"easily"])
        [u'Print', u'\uc720\ub2c8\ucf54\ub4dc', u'easily']
        >>> konlpy.utils.pprint([u"Print", u"유니코드", u"easily"])
        ['Print', '유니코드', 'easily']
    """
    return UnicodePrinter().pprint(obj)

def preprocess(phrase):
    """Preprocesses a phrase in the following steps:.

    - :py:func:`.concat`
    """
    return select(concat(phrase))

def select(phrase):
    """Replaces some ambiguous punctuation marks to simpler ones."""
    # TODO: document replacements
    # TODO: do not replace unless explicitly noticed
    # TODO: add 'only hangul' option
    for a, b in replace_set:
        phrase = phrase.replace(a, b)
    return phrase


def char2hex(c):
    """Converts a unicode character to hex.

    .. code-block:: python

        >>> char2hex(u'음')
        '0xc74c'
    """
    return hex(ord(c))

def hex2char(h):
    """Converts a hex character to unicode.

    .. code-block:: python

        >>> print hex2char('c74c')
        음
        >>> print hex2char('0xc74c')
        음
    """
    return unichr(int(h, 16))


def load_txt(filename):
    """Text file loader."""
    return codecs.open(filename, encoding='utf-8')
