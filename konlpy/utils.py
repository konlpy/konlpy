#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os

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

def concat(phrase):
    """Concatenates lines into a unified string."""
    return phrase.replace(os.linesep, ' ')

def select(phrase):
    """Replaces some ambiguous punctuation marks to simpler ones."""
    # TODO: document replacements
    # TODO: do not replace unless explicitly noticed
    # TODO: add 'only hangul' option
    for a, b in replace_set:
        phrase = phrase.replace(a, b)
    return phrase

def preprocess(phrase):
    """Preprocesses a phrase in the following steps:.

    - :py:func:`.concat`
    """
    return select(concat(phrase))

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

def partition(list_, indices):
    """Partitions a list to several parts using indices.

    :param list_: The target list.
    :param indices: Indices to partition the target list.
    """
    return [list_[i:j] for i, j in zip([0]+indices, indices+[None])]
