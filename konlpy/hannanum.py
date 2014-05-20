#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import pkgutil
import sys

import jpype


def parse(result, flatten=False):
    elems = result.strip().split('\n')
    index = [i for i, e in enumerate(elems) if not e]

    i = 0
    formatted = []
    if flatten:
        for j in index:
            token = filter(None, elems[i:j])[1:]
            fmt = [tuple(u.split('/')) for t in token\
                    for u in t.strip().split('+')]
            formatted.extend(fmt)
            i = j
    else:
        for j in index:
            token = filter(None, elems[i:j])[1:]
            fmt = [[tuple(u.split('/')) for u in t.strip().split('+')]\
                    for t in token]
            formatted.append(fmt)
            i = j
    return formatted

class Hannanum():

    def morph(self, phrase):
        result = self.jhi.morphAnalyzer(phrase)
        return parse(result)

    def nouns(self, phrase):
        return list(self.jhi.extractNoun(phrase))

    def pos(self, phrase, ntags=9):
        if ntags==9:
            result = self.jhi.simplePos09(phrase)
        elif ntags==22:
            result = self.jhi.simplePos22(phrase)
        else:
            raise Exception('ntags in [9, 22]')
        return parse(result, flatten=True)

    def __init__(self, jvmpath=None):
        if sys.platform.startswith('win'):
            divchar = '\\'
        else:
            divchar = '/'
        folder_suffix = ['{0}', '{0}{1}bin', '{0}{1}jhannanum-0.8.4.jar']
        javadir = '%s%sjava'\
                % (os.path.dirname(os.path.realpath(__file__)), divchar)
        args = [javadir, divchar]
        classpath = ':'.join(f.format(*args) for f in folder_suffix)

        os.chdir(javadir)
        jvmpath = jvmpath or jpype.getDefaultJVMPath()
        jpype.startJVM(jvmpath, '-Djava.class.path=%s' % classpath, '-ea')

        jhannanum = jpype.JPackage('kr.lucypark.jhannanum.comm')
        HannanumInterface = jhannanum.HannanumInterface

        self.jhi = HannanumInterface()


if __name__=='__main__':
    phrase = u'롯데마트가 판매하고 있는 흑마늘'
    hi = Hannanum()

    from pprint import pprint
    print '\nMorph:'; pprint(hi.morph(phrase))
    print '\nNouns:'; pprint(hi.nouns(phrase))
    print '\nPos09:'; pprint(hi.pos(phrase))
    print '\nPos22:'; pprint(hi.pos(phrase, ntags=22))
