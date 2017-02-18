#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def kkma_instance():
    from konlpy.tag import Kkma
    k = Kkma()
    return k

@pytest.fixture
def string():
    return u"꽃가마 타고 강남 가자!"

def test_kkma_nouns(kkma_instance, string):
    assert kkma_instance.nouns(string) ==\
        [u'\uaf43\uac00\ub9c8', u'\ud0c0\uace0', u'\uac15\ub0a8',
         u'\uac00\uc790']

def test_kkma_nouns(kkma_instance, string):
    assert kkma_instance.morphs(string) ==\
        [u'\uaf43\uac00\ub9c8',
         u'\ud0c0\uace0',
         u'\uac15\ub0a8',
         u'\uac00\uc790',
         u'!']

def test_kkma_pos(kkma_instance, string):
    assert kkma_instance.pos(string) ==\
        [(u'\uaf43\uac00\ub9c8', u'NNG'),
         (u'\ud0c0\uace0', u'NNG'),
         (u'\uac15\ub0a8', u'NNG'),
         (u'\uac00\uc790', u'NNG'),
         (u'!', u'SF')]

def test_kkma_pos_join(kkma_instance, string):
    assert kkma_instance.pos(string, join=True) ==\
        [u'\uaf43\uac00\ub9c8/NNG',
         u'\ud0c0\uace0/NNG',
         u'\uac15\ub0a8/NNG',
         u'\uac00\uc790/NNG',
         u'!/SF']

def test_kkma_sentences(kkma_instance, string):
    assert kkma_instance.sentences(string) ==\
        [u'\uaf43\uac00\ub9c8 \ud0c0\uace0 \uac15\ub0a8 \uac00\uc790!']
