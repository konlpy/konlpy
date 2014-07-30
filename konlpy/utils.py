#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

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

def char2hex(c):
    # u'음' -> '0xc74c'
    return hex(ord(c))

def hex2char(h):
    # 'c74c' or '0xc74c' -> u'음'
    return unichr(int(h, 16))

