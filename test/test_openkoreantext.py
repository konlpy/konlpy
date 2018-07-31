#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import warnings

import pytest


@pytest.fixture
def tkorean_instance():
    from konlpy.tag import Okt
    t = Okt()
    return t

@pytest.fixture
def string():
    return u"꽃가마 타고 강남 가나욬ㅋㅋㅋㅋ"

def test_tkorean_pos(tkorean_instance, string):
    assert tkorean_instance.pos(string) ==\
        [(u'\uaf43', u'Noun'), (u'\uac00\ub9c8', u'Noun'), (u'\ud0c0\uace0', u'Noun'), (u'\uac15\ub0a8', u'Noun'), (u'\uac00\ub098', u'Noun'), (u'\uc6ac', u'Noun'), (u'\u314b\u314b\u314b\u314b', u'KoreanParticle')]

def test_tkorean_pos_1(tkorean_instance, string):
    assert tkorean_instance.pos(string, stem=True) ==\
        [(u'\uaf43', u'Noun'), (u'\uac00\ub9c8', u'Noun'), (u'\ud0c0\uace0', u'Noun'), (u'\uac15\ub0a8', u'Noun'), (u'\uac00\ub098', u'Noun'), (u'\uc6ac', u'Noun'), (u'\u314b\u314b\u314b\u314b', u'KoreanParticle')]

def test_tkorean_pos_2(tkorean_instance, string):
    assert tkorean_instance.pos(string, norm=True) ==\
        [(u'\uaf43', u'Noun'), (u'\uac00\ub9c8', u'Noun'), (u'\ud0c0\uace0', u'Noun'), (u'\uac15\ub0a8', u'Noun'), (u'\uac00\ub098', u'Noun'), (u'\uc694', u'Josa'), (u'\u314b\u314b\u314b', u'KoreanParticle')]

def test_tkorean_pos_3(tkorean_instance, string):
    assert tkorean_instance.pos(string, stem=True, norm=True) ==\
        [(u'\uaf43', u'Noun'), (u'\uac00\ub9c8', u'Noun'), (u'\ud0c0\uace0', u'Noun'), (u'\uac15\ub0a8', u'Noun'), (u'\uac00\ub098', u'Noun'), (u'\uc694', u'Josa'), (u'\u314b\u314b\u314b', u'KoreanParticle')]

def test_tkorean_pos_join(tkorean_instance, string):
    assert tkorean_instance.pos(string, join=True) ==\
        [u'\uaf43/Noun', u'\uac00\ub9c8/Noun', u'\ud0c0\uace0/Noun', u'\uac15\ub0a8/Noun', u'\uac00\ub098/Noun', u'\uc6ac/Noun', u'\u314b\u314b\u314b\u314b/KoreanParticle']

def test_tkorean_nouns(tkorean_instance, string):
    assert tkorean_instance.nouns(string) ==\
        [u'\uaf43', u'\uac00\ub9c8', u'\ud0c0\uace0', u'\uac15\ub0a8', u'\uac00\ub098', u'\uc6ac']

def test_tkorean_phrases(tkorean_instance, string):
    assert tkorean_instance.phrases(string) ==\
        [u'\uaf43\uac00\ub9c8', u'\uaf43\uac00\ub9c8 \ud0c0\uace0', u'\uaf43\uac00\ub9c8 \ud0c0\uace0 \uac15\ub0a8', u'\uaf43\uac00\ub9c8 \ud0c0\uace0 \uac15\ub0a8 \uac00\ub098\uc6ac', u'\uac00\ub9c8', u'\ud0c0\uace0', u'\uac15\ub0a8', u'\uac00\ub098']

def test_tkorean_morphs(tkorean_instance, string):
    assert tkorean_instance.morphs(string) ==\
        [u'\uaf43', u'\uac00\ub9c8', u'\ud0c0\uace0', u'\uac15\ub0a8', u'\uac00\ub098', u'\uc6ac', u'\u314b\u314b\u314b\u314b']
