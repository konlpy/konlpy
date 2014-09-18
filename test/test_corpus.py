#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


def test_corpus_kolaw():
    from konlpy.corpus import kolaw

    fids = kolaw.fileids()

    kolaw.abspath()
    kolaw.abspath(fids[0])

    assert kolaw.name == 'kolaw'
    assert kolaw.open('constitution.txt').read(10) ==\
            u'\ub300\ud55c\ubbfc\uad6d\ud5cc\ubc95\n\n\uc720\uad6c'
