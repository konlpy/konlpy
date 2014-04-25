#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import pkgutil

import jpype


def format_result(result):
    elements = result.strip().split('\n')
    formatted = {}
    idx = 0
    split = [i for i, e in enumerate(elements) if not e]
    for s in split:
        tmp = filter(None, elements[idx:s])
        idx = s
        formatted[tmp[0]] = [t.strip() for t in tmp[1:]]
    return formatted


class Hannanum():

    def morph(self, phrase):
        result = self.hi.morphAnalyzer(phrase)
        return format_result(result)

    def nouns(self, phrase):
        return list(self.hi.extractNoun(phrase))

    def pos(self, phrase, ntags=9):
        if ntags==9:
            result = self.hi.simplePos09(phrase)
        elif ntags==22:
            result = self.hi.simplePos22(phrase)
        else:
            raise Exception('ntags in [9, 22]')
        return format_result(result)

    def __init__(self):
        print 'Initializing Hannanum...',
        folder_suffix = ['{0}', '{0}/bin', '{0}/jhannanum.jar']
        javadir = '%s/java' % os.path.dirname(os.path.realpath(__file__))
        classpath = ':'.join(f.format(javadir) for f in folder_suffix)
        jpype.startJVM(jpype.getDefaultJVMPath(),\
                '-Djava.class.path=%s' % classpath, '-ea')

        jhannanum = jpype.JPackage('kr.lucypark.jhannanum.comm')
        HannanumInterface = jhannanum.HannanumInterface

        self.hi = HannanumInterface()
        print 'done.'


if __name__=='__main__':
    phrase = u'다람쥐, 헌 서울대공원 쳇바퀴에 타고파.'
    hi = Hannanum()

    from pprint import pprint
    print '\nMorph:'; pprint(hi.morph(phrase))
    print '\nNouns:'; pprint(hi.nouns(phrase))
    print '\nPos09:'; pprint(hi.pos(phrase))
    print '\nPos22:'; pprint(hi.pos(phrase, ntags=22))
