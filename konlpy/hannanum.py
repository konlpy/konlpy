#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
import jpype

import utils


tag_re = ur'(.+?\/\w+)\+?'

def parse(result, flatten=False):
    elems = result.strip().splitlines()
    index = [i for i, e in enumerate(elems) if not e]

    i = 0
    formatted = []
    if flatten:
        for j in index:
            token = filter(None, elems[i:j])[1:]
            fmt = [tuple(u.rsplit('/', 1)) for t in token\
                    for u in re.findall(tag_re, t.strip())]
            formatted.extend(fmt)
            i = j
    else:
        for j in index:
            token = filter(None, elems[i:j])[1:]
            fmt = [[tuple(u.rsplit('/', 1))\
                    for u in re.findall(tag_re, t.strip())] for t in token]
            formatted.append(fmt)
            i = j
    return formatted

class Hannanum():

    def morph(self, phrase):
        phrase = utils.preprocess(phrase)
        result = self.jhi.morphAnalyzer(phrase)
        return parse(result)

    def nouns(self, phrase):
        phrase = utils.preprocess(phrase)
        return list(self.jhi.extractNoun(phrase))

    def pos(self, phrase, ntags=9):
        phrase = utils.preprocess(phrase)
        if ntags==9:
            result = self.jhi.simplePos09(phrase)
        elif ntags==22:
            result = self.jhi.simplePos22(phrase)
        else:
            raise Exception('ntags in [9, 22]')
        return parse(result, flatten=True)

    def __init__(self, jvmpath=None):
        jhannanumJavaPackage = jpype.JPackage('kr.lucypark.jhannanum.comm')
        HannanumInterfaceJavaClass = jhannanumJavaPackage.HannanumInterface
        self.jhi = HannanumInterfaceJavaClass() # Java instance


if __name__=='__main__':
    from init_jvm import init_jvm
    from pprint import pprint

    phrase = u'(학교에서조차도) 1/2+3/2이 2이라는 사실을 모르고 있었다!'

    init_jvm()
    hi = Hannanum()

    print '\nMorph:'; pprint(hi.morph(phrase))
    print '\nNouns:'; pprint(hi.nouns(phrase))
    print '\nPos09:'; pprint(hi.pos(phrase))
    print '\nPos22:'; pprint(hi.pos(phrase, ntags=22))
