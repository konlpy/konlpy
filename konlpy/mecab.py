#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import MeCab
import utils


# 참고: https://docs.google.com/spreadsheet/ccc?key=0ApcJghR6UMXxdEdURGY2YzIwb3dSZ290RFpSaUkzZ0E&usp=sharing#gid=6
attrs = ['tags', # 품사 태그
         'semantic', # 의미 부류
         'has_jongsung', # 종성 유무
         'read', # 읽기
         'type', # 타입
         'first_pos', # 첫번째 품사
         'last_pos', # 마지막 품사
         'original', # 원형
         'indexed'] # 인덱스 표현

def parse(result, allattrs=False):
    def split(elem, allattrs):
        if allattrs:
            s, t = elem.split('\t')
            return (s, dict(zip(attrs, t.split(','))))
        else:
            s, t = elem.split('\t')
            return (s, t.split(',', 1)[0])

    elems = result.splitlines()
    return [split(elem, allattrs=False) for elem in elems[:-1]]

class Mecab():

    def pos(self, phrase, ntags=43):
        phrase = utils.preprocess(phrase).encode('utf-8')
        result = self.tagger.parse(phrase).decode('utf-8')
        return parse(result)

    def __init__(self, dicpath='/usr/local/lib/mecab/dic/mecab-ko-dic'):
        try:
            self.tagger = MeCab.Tagger('-d %s' % dicpath)
        except RuntimeError:
            raise Exception('Invalid MeCab dictionary path: "%s"\nInput the correct path when initiializing class: "Mecab(\'/some/dic/path\')"' % dicpath)

if __name__=='__main__':
    from pprint import pprint

    phrase = u'자연주의 쇼핑몰은 어떤 곳인가?'
    mc = Mecab()
    print '\nPos43:'; pprint(mc.pos(phrase))
