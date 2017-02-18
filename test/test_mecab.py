#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import pytest

@pytest.fixture
def mecab_instance():
    from konlpy.tag import Mecab
    m = Mecab()
    return m

@pytest.fixture
def string():
    return u"꽃가마 타고 강남 가자!"

def test_mecab_pos_43(mecab_instance, string):
    assert mecab_instance.pos(string) ==\
        [(u'\uaf43\uac00\ub9c8', u'NNG'),
         (u'\ud0c0', u'VV'),
         (u'\uace0', u'EC'),
         (u'\uac15\ub0a8', u'NNP'),
         (u'\uac00', u'VV'),
         (u'\uc790', u'EF'),
         (u'!', u'SF')]

def test_mecab_pos_join(mecab_instance, string):
    assert mecab_instance.pos(string, join=True) ==\
        [u'\uaf43\uac00\ub9c8/NNG',
         u'\ud0c0/VV',
         u'\uace0/EC',
         u'\uac15\ub0a8/NNP',
         u'\uac00/VV',
         u'\uc790/EF',
         u'!/SF']

def test_mecab_morphs(mecab_instance, string):
    assert mecab_instance.morphs(string) ==\
        [u'\uaf43\uac00\ub9c8',
         u'\ud0c0',
         u'\uace0',
         u'\uac15\ub0a8',
         u'\uac00',
         u'\uc790',
         u'!']

def test_mecab_nouns(mecab_instance, string):
    assert mecab_instance.nouns(string) ==\
        [u'\uaf43\uac00\ub9c8', u'\uac15\ub0a8']
