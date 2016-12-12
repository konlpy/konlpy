#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys

def test_utils_pprint(capsys): # Fixture `capsys` allows stdout/stderr captures
    from konlpy.utils import pprint
    pprint([u"저는 소프트웨어 관련학과 입니다."])
    out, err = capsys.readouterr()
    if sys.version_info[0] < 3:
        assert out == u"[저는 소프트웨어 관련학과 입니다.]\n"
    else:
        assert out == u"['저는 소프트웨어 관련학과 입니다.']\n"

def test_utils_concordance():
    from konlpy.corpus import kolaw
    from konlpy.utils  import concordance
    doc = kolaw.open('constitution.txt').read()
    ccd = concordance(u'대한민국', doc, show=True)
    assert ccd == [0, 9, 98, 100, 110, 126, 133, 147, 787, 1836, 3620]

def test_utils_concordance_show(capsys):
    from konlpy.corpus import kolaw
    from konlpy.utils  import concordance
    doc = kolaw.open('constitution.txt').read()
    ccd = concordance(u'대한민국', doc, show=True)
    out, err = capsys.readouterr()
    assert out == u"0\t대한민국헌법 유구한 역사와\n9\t대한국민은 3·1운동으로 건립된 대한민국임시정부의 법통과 불의에\n98\t총강 제1조 ① 대한민국은 민주공화국이다. ②대한민국의\n100\t① 대한민국은 민주공화국이다. ②대한민국의 주권은 국민에게\n110\t나온다. 제2조 ① 대한민국의 국민이 되는\n126\t의무를 진다. 제3조 대한민국의 영토는 한반도와\n133\t부속도서로 한다. 제4조 대한민국은 통일을 지향하며,\n147\t추진한다. 제5조 ① 대한민국은 국제평화의 유지에\n787\t군무원이 아닌 국민은 대한민국의 영역안에서는 중대한\n1836\t파견 또는 외국군대의 대한민국 영역안에서의 주류에\n3620\t경제 제119조 ① 대한민국의 경제질서는 개인과\n"
