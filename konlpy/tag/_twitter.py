#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import jpype

from .. import jvm
from .. import utils


class Twitter():
    """Wrapper for `Twitter Korean Text <https://github.com/twitter/twitter-korean-text>`_.

    Twitter Korean Text is an open source Korean tokenizer written in Scala,
    developed by Will Hohyon Ryu.

    .. code-block:: python

        from konlpy.tag import Twitter

        twitter = Twitter()
        print twitter.pos(u'이것도 되나요')

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    """

    def pos(self, phrase, norm=False, stem=False):
        tokens  = self.jki.tokenize(phrase,\
                jpype.java.lang.Boolean(norm), jpype.java.lang.Boolean(stem)).toArray()
        return [tuple(t.rsplit('/', 1)) for t in tokens]

    def phrases(self, phrase):
        return [p for p in self.jki.phrases(phrase).toArray()]

    def __init__(self, jvmpath=None):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath)

        tktJavaPackage = jpype.JPackage('kr.lucypark.tkt')
        TktInterfaceJavaClass = tktJavaPackage.TktInterface
        self.jki = TktInterfaceJavaClass()
