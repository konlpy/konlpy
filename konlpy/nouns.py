#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os
import jpype

def init_hannanum():
    currentdir = os.path.dirname(os.path.realpath(__file__))
    classpath = "%s/java:%s/java/jhannanum.jar" % (currentdir, currentdir)

    jpype.startJVM(jpype.getDefaultJVMPath(),\
            "-Djava.class.path=%s" % classpath, "-ea")

    jhannanum = jpype.JPackage('kr.lucypark.jhannanum.comm')
    HannanumInterface = jhannanum.HannanumInterface

    return HannanumInterface()

def nouns(phrase):
    hi = init_hannanum()
    return hi.extractNoun(phrase)

if __name__=='__main__':
    n = nouns(u'롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다.')
    print n
    print ','.join(n)
