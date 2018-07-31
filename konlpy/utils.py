# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import json
import os
import pprint as pp
import sys


installpath = os.path.dirname(os.path.realpath(__file__))
replace_set = [
    ('·', '/'),     # \xb7
    ('․', '/'),     # \u2024
    ('ㆍ', '/'),    # \u318d (hangul letter araea)
    ('･', '/'),     # \uff65 (katakana)
    ('～', '~'),    # \uff5e
    ('❑', '-'),     # \u2751
    ('‘', "'"),     # \u2018
    ('’', "'"),     # \u2019
    ('“', '"'),     # \u201c
    ('”', '"'),     # \u201d
    ('「', '<'),    # \u300c
    ('」', '>')]    # \u300d


if sys.version_info[0] < 3:
    class UnicodePrinter(pp.PrettyPrinter):
        def format(self, object, context, maxlevels, level):
            """Overrided method to enable Unicode pretty print."""
            if isinstance(object, unicode):
                encoding = sys.stdout.encoding or 'utf-8'
                return (object.encode(encoding), True, False)
            return pp.PrettyPrinter.format(self, object, context, maxlevels, level)


def concordance(phrase, text, show=False):
    """Find concordances of a phrase in a text.

    The farmost left numbers are indices, that indicate the location
    of the phrase in the text (by means of tokens).
    The following string, is part of the text surrounding the phrase
    for the given index.

    :param phrase: Phrase to search in the document.
    :param text: Target document.
    :param show: If ``True``, shows locations of the phrase on the console.

    .. code-block:: python

        >>> from konlpy.corpus import kolaw
        >>> from konlpy.tag import Mecab
        >>> from konlpy import utils
        >>> constitution = kolaw.open('constitution.txt').read()
        >>> idx = utils.concordance(u'대한민국', constitution, show=True)
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
    if show:
        for i in indexes:
            print('%d\t%s' % (i, ' '.join(terms[max(0, i - 3):i + 3])))
    return indexes


if sys.version_info[0] < 3:
    from konlpy import csvutils

    def csvread(f, encoding='utf-8'):
        """Reads a csv file.

        :param f: File object.

        .. code-block:: python

            >>> from konlpy.utils import csvread
            >>> with open('some.csv', 'r') as f:
                    print csvread(f)
            [[u'\uc774 / NR', u'\ucc28 / NNB'], [u'\ub098\uac00 / VV', u'\ub124 / EFN']]
        """
        reader = csvutils.UnicodeReader(f)
        return [row for row in reader]

    def csvwrite(data, f):
        """Writes a csv file.

        :param data: A list of list.

        .. code-block:: python

            >>> from konlpy.utils import csvwrite
            >>> d = [[u'\uc774 / NR', u'\ucc28 / NNB'], [u'\ub098\uac00 / VV', u'\ub124 / EFN']]
            >>> with open('some.csv', 'w') as f:
                    csvwrite(d, f)
        """
        return csvutils.UnicodeWriter(f).writerows(data)


def partition(list_, indices):
    """Partitions a list to several parts using indices.

    :param list_: The target list.
    :param indices: Indices to partition the target list.
    """
    return [list_[i:j] for i, j in zip([0] + indices, indices + [None])]

if sys.version_info[0] < 3:
    def pprint(obj, **kwargs):
        """Unicode pretty printer.

        .. code-block:: python

            >>> import pprint, konlpy
            >>> pprint.pprint([u"Print", u"유니코드", u"easily"])
            [u'Print', u'\uc720\ub2c8\ucf54\ub4dc', u'easily']
            >>> konlpy.utils.pprint([u"Print", u"유니코드", u"easily"])
            ['Print', '유니코드', 'easily']

        :param stream: Option to stream to a particular destination. Can be either sys.stdout (default) or sys.stderr. See #179 for details.
        """

        # quick patch to use sys.stderr stream
        if 'stream' in kwargs.keys():
            return UnicodePrinter(stream=kwargs['stream']).pprint(obj)
        return UnicodePrinter().pprint(obj)
else:
    pprint = pp.pprint


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


if sys.version_info[0] >= 3:
    unichr = chr


def hex2char(h):
    """Converts a hex character to unicode.

    .. code-block:: python

        >>> print hex2char('c74c')
        음
        >>> print hex2char('0xc74c')
        음
    """
    return unichr(int(h, 16))


def load_txt(filename, encoding='utf-8'):
    """Text file loader.
    To read a file, use ``read_txt()``instead.
    """
    return io.open(filename, 'r', encoding=encoding)


def read_txt(filename, encoding='utf-8'):
    """Text file reader."""
    with io.open(filename, 'r', encoding=encoding) as f:
        return f.read()


def read_json(filename, encoding='utf-8'):
    """JSON file reader."""
    with io.open(filename, 'r', encoding=encoding) as f:
        return json.load(f)
