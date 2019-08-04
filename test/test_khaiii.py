# -*- coding: utf-8 -*-

import pytest

@pytest.fixture
def khaiii_instance():
    from konlpy.tag import Khaiii
    k = Khaiii()
    return k

@pytest.fixture
def string():
    return '꽃가마 타고 강남 가자!'

def test_khaiii_nouns(khaiii_instance, string):
    assert khaiii_instance.nouns(string) == ['꽃가마', '강남']

def test_khaiii_morphs(khaiii_instance, string):
    assert khaiii_instance.morphs(string) ==\
        ['꽃가마', '타', '고', '강남', '가', '자', '!']

def test_khaiii_pos(khaiii_instance, string):
    assert khaiii_instance.pos(string) ==\
        [('꽃가마', 'NNG'),
         ('타', 'VV'),
         ('고', 'EC'),
         ('강남', 'NNP'),
         ('가', 'VV'),
         ('자', 'EF'),
         ('!', 'SF')]

def test_khaiii_pos_join(khaiii_instance, string):
    assert khaiii_instance.pos(string, join=True) ==\
        ['꽃가마/NNG',
         '타/VV',
         '고/EC',
         '강남/NNP',
         '가/VV',
         '자/EF',
         '!/SF']
