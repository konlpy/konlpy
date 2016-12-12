#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import jpype

from .. import jvm
from .. import utils


class Twitter():
    """
    Wrapper for `Twitter Korean Text <https://github.com/twitter/twitter-korean-text>`_.

    Twitter Korean Text is an open source Korean tokenizer written in Scala,
    developed by Will Hohyon Ryu.

    .. code-block:: python

        >>> from konlpy.tag import Twitter
        >>> twitter = Twitter()
        >>> print(twitter.morphs(u'단독입찰보다 복수입찰의 경우'))
        ['단독', '입찰', '보다', '복수', '입찰', '의', '경우', '가']
        >>> print(twitter.nouns(u'유일하게 항공기 체계 종합개발 경험을 갖고 있는 KAI는'))
        ['유일하', '항공기', '체계', '종합', '개발', '경험']
        >>> print(twitter.phrases(u'날카로운 분석과 신뢰감 있는 진행으로'))
        ['분석', '분석과 신뢰감', '신뢰감', '분석과 신뢰감 있는 진행', '신뢰감 있는 진행', '진행', '신뢰']
        >>> print(twitter.pos(u'이것도 되나욬ㅋㅋ'))
        [('이', 'Determiner'), ('것', 'Noun'), ('도', 'Josa'), ('되나욬', 'Noun'), ('ㅋㅋ', 'KoreanParticle')]
        >>> print(twitter.pos(u'이것도 되나욬ㅋㅋ', norm=True))
        [('이', 'Determiner'), ('것', 'Noun'), ('도', 'Josa'), ('되', 'Verb'), ('나요', 'Eomi'), ('ㅋㅋ', 'KoreanParticle')]
        >>> print(twitter.pos(u'이것도 되나욬ㅋㅋ', norm=True, stem=True))
        [('이', 'Determiner'), ('것', 'Noun'), ('도', 'Josa'), ('되다', 'Verb'), ('ㅋㅋ', 'KoreanParticle')]

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    """

    def pos(self, phrase, norm=False, stem=False):
        """POS tagger.
        In contrast to other classes in this subpackage,
        this POS tagger doesn't have a `flatten` option,
        but has `norm` and `stem` options.
        Check the parameter list below.

        :param norm: If True, normalize tokens.
        :param stem: If True, stem tokens.
        """

        tokens = self.jki.tokenize(
                    phrase,
                    jpype.java.lang.Boolean(norm),
                    jpype.java.lang.Boolean(stem)).toArray()
        return [tuple(t.rsplit('/', 1)) for t in tokens]

    def nouns(self, phrase):
        """Noun extractor."""

        tagged = self.pos(phrase)
        return [s for s, t in tagged if t == 'Noun']

    def morphs(self, phrase, norm=False, stem=False):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase)]

    def phrases(self, phrase):
        """Phrase extractor."""

        return [p for p in self.jki.phrases(phrase).toArray()]

    def __init__(self, jvmpath=None):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath)

        tktJavaPackage = jpype.JPackage('kr.lucypark.tkt')
        TktInterfaceJavaClass = tktJavaPackage.TktInterface
        self.jki = TktInterfaceJavaClass()
        self.tagset = utils.read_json('%s/data/tagset/twitter.json' % utils.installpath)
