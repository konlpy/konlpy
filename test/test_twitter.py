#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import warnings

import pytest


@pytest.fixture
def tkorean_instance():
    from konlpy.tag import Twitter
    t = Twitter()
    return t

@pytest.fixture
def string():
    return u"꽃가마 타고 강남 가자!"

def test_tkorean_pos(tkorean_instance, string):
    assert tkorean_instance.pos(string) ==\
        [(u'\uaf43', u'Noun'),
         (u'\uac00\ub9c8', u'Noun'),
         (u'\ud0c0\uace0', u'Noun'),
         (u'\uac15\ub0a8', u'Noun'),
         (u'\uac00\uc790', u'Verb'),
         (u'!', u'Punctuation')]
