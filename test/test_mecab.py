#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def mecab_instance():
    import konlpy
    m = konlpy.Mecab()
    return m

@pytest.fixture
def string():
    return u"꽃가마 타고 강남 가자!"

def test_hannanum_pos_22(mecab_instance, string):
    assert mecab_instance.pos(string, ntags=22) ==\
        [(u'\uaf43\uac00\ub9c8', u'NNG'),
         (u'\ud0c0', u'VV'),
         (u'\uace0', u'EC'),
         (u'\uac15\ub0a8', u'NNP'),
         (u'\uac00\uc790', u'NNP'),
         (u'!', u'SY'),
         (u'.', u'SF')]
