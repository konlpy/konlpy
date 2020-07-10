import pytest

@pytest.fixture
def deeq_instance():
    from konlpy.tag import Deeq
    d = Deeq()
    return d

@pytest.fixture
def string():
    return u'꽃가마 타고 강남 가자!'

def test_deeq_nouns(deeq_instance, string):
    assert deeq_instance.nouns(string) == \
        [u'\uaf43\uac00\ub9c8', u'\uac15\ub0a8']

def test_deeq_morphs(deeq_instance, string):
    assert deeq_instance.morphs(string) ==\
        [u'\uaf43\uac00\ub9c8', u'\ud0c0', u'\uace0', u'\uac15\ub0a8', u'\uac00', u'\uc790', u'!']

def test_deeq_pos(deeq_instance, string):
    assert deeq_instance.pos(string) ==\
        [(u'\uaf43\uac00\ub9c8', u'NNG'),
         (u'\ud0c0', u'VV'),
         (u'\uace0', u'EC'),
         (u'\uac15\ub0a8', u'NNP'),
         (u'\uac00', u'VV'),
         (u'\uc790', u'EF'),
         (u'!', u'SF')]

def test_deeq_pos_join(deeq_instance, string):
    assert deeq_instance.pos(string, join=True) ==\
        [u'\uaf43\uac00\ub9c8/NNG',
         u'\ud0c0/VV',
         u'\uace0/EC',
         u'\uac15\ub0a8/NNP',
         u'\uac00/VV',
         u'\uc790/EF',
         u'!/SF']