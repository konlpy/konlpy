#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def test_utils_pprint(capsys): # Fixture `capsys` allows stdout/stderr captures
    from konlpy.utils import pprint
    pprint([u"저는 소프트웨어 관련학과 입니다."])
    out, err = capsys.readouterr()
    assert out == u"[저는 소프트웨어 관련학과 입니다.]\n"
