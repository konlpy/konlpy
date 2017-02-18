#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys
import warnings

import pytest


if sys.version_info[0] < 3:
    pass

else:
    @pytest.fixture
    def komoran_instance():
        from konlpy.tag import Komoran
        k = Komoran()
        return k

    @pytest.fixture
    def string():
        return u"꽃가마 타고 강남 가자!"

    def test_komoran_nouns(komoran_instance, string):
        assert komoran_instance.nouns(string) ==\
            [u'\uaf43\uac00\ub9c8', u'\uac15\ub0a8']

    def test_komoran_pos(komoran_instance, string):
        assert komoran_instance.pos(string) ==\
            [(u'\uaf43\uac00\ub9c8', u'NNG'),
             (u'\ud0c0', u'VV'),
             (u'\uace0', u'EC'),
             (u'\uac15\ub0a8', u'NNP'),
             (u'\uac00', u'VV'),
             (u'\uc790', u'EF'),
             (u'!', u'SF')]

    def test_komoran_pos_join(komoran_instance, string):
        assert komoran_instance.pos(string, join=True) ==\
            [u'\uaf43\uac00\ub9c8/NNG',
             u'\ud0c0/VV',
             u'\uace0/EC',
             u'\uac15\ub0a8/NNP',
             u'\uac00/VV',
             u'\uc790/EF',
             u'!/SF']
