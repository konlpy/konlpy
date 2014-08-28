#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def hannanum_instance():
    from konlpy import init_jvm
    from konlpy.tag import Hannanum
    init_jvm()
    h = Hannanum()
    return h

@pytest.fixture
def string():
    return u"꽃가마 타고 강남 가자!"


def test_hannanum_analyze(hannanum_instance, string):
    assert hannanum_instance.analyze(string) ==\
        [[[(u'\uaf43\uac00', u'ncn'), (u'\uc774', u'jp'), (u'\ub9c8', u'ef')],
          [(u'\uaf43\uac00\ub9c8', u'ncn')],
          [(u'\uaf43\uac00', u'nqq'), (u'\uc774', u'jp'), (u'\ub9c8', u'ef')],
          [(u'\uaf43\uac00\ub9c8', u'nqq')]],
         [[(u'\ud0c0', u'pvg'), (u'\uace0', u'ecc')],
          [(u'\ud0c0', u'pvg'), (u'\uace0', u'ecs')],
          [(u'\ud0c0', u'pvg'), (u'\uace0', u'ecx')]],
         [[(u'\uac15\ub0a8', u'ncn')]],
         [[(u'\uac00', u'pvg'), (u'\uc790', u'ecc')],
          [(u'\uac00', u'pvg'), (u'\uc790', u'ecs')],
          [(u'\uac00', u'pvg'), (u'\uc790', u'ef')],
          [(u'\uac00', u'px'), (u'\uc790', u'ecc')],
          [(u'\uac00', u'px'), (u'\uc790', u'ecs')],
          [(u'\uac00', u'px'), (u'\uc790', u'ef')]],
         [[(u'!', u'sf')]]]

def test_hannanum_nouns(hannanum_instance, string):
    assert hannanum_instance.nouns(string) ==\
        [u'\uaf43\uac00\ub9c8', u'\uac15\ub0a8']

def test_hannanum_morphs(hannanum_instance, string):
    assert hannanum_instance.morphs(string) ==\
        [u'\uaf43\uac00\ub9c8',
         u'\ud0c0',
         u'\uace0',
         u'\uac15\ub0a8',
         u'\uac00',
         u'\uc790',
         u'!']

def test_hannanum_pos_9(hannanum_instance, string):
    assert hannanum_instance.pos(string) ==\
        [(u'\uaf43\uac00\ub9c8', u'N'),
         (u'\ud0c0', u'P'),
         (u'\uace0', u'E'),
         (u'\uac15\ub0a8', u'N'),
         (u'\uac00', u'P'),
         (u'\uc790', u'E'),
         (u'!', u'S')]

def test_hannanum_pos_22(hannanum_instance, string):
    assert hannanum_instance.pos(string, ntags=22) ==\
        [(u'\uaf43\uac00\ub9c8', u'NC'),
         (u'\ud0c0', u'PV'),
         (u'\uace0', u'EC'),
         (u'\uac15\ub0a8', u'NC'),
         (u'\uac00', u'PX'),
         (u'\uc790', u'EC'),
         (u'!', u'SF')]
