# -*- coding: utf-8 -*-
from __future__ import absolute_import

import jpype

from konlpy import jvm, utils


def Twitter(jvmpath=None):
    """
    The ``Twitter()`` backend has changed to ``Okt()`` since KoNLPy v0.5.0.
    See :issue:`141` for details.
    """

    from warnings import warn
    warn('"Twitter" has changed to "Okt" since KoNLPy v0.4.5.')
    return Okt(jvmpath)


class Okt():
    """
    Wrapper for `Open Korean Text <https://github.com/open-korean-text/open-korean-text>`_.

    Open Korean Text is an open source Korean tokenizer written in Scala,
    developed by Will Hohyon Ryu.

    .. code-block:: python

        >>> from konlpy.tag import Okt
        >>> okt = Okt()
        >>> print(okt.morphs(u'단독입찰보다 복수입찰의 경우'))
        ['단독', '입찰', '보다', '복수', '입찰', '의', '경우']
        >>> print(okt.nouns(u'유일하게 항공기 체계 종합개발 경험을 갖고 있는 KAI는'))
        ['항공기', '체계', '종합', '개발', '경험']
        >>> print(okt.phrases(u'날카로운 분석과 신뢰감 있는 진행으로'))
        ['날카로운 분석', '날카로운 분석과 신뢰감', '날카로운 분석과 신뢰감 있는 진행', '분석', '신뢰', '진행']
        >>> print(okt.pos(u'이것도 되나욬ㅋㅋ'))
        [('이', 'Determiner'), ('것', 'Noun'), ('도', 'Josa'), ('되나욬', 'Noun'), ('ㅋㅋ', 'KoreanParticle')]
        >>> print(okt.pos(u'이것도 되나욬ㅋㅋ', norm=True))
        [('이', 'Determiner'), ('것', 'Noun'), ('도', 'Josa'), ('되나요', 'Verb'), ('ㅋㅋ', 'KoreanParticle')]
        >>> print(okt.pos(u'이것도 되나욬ㅋㅋ', norm=True, stem=True))
        [('이', 'Determiner'), ('것', 'Noun'), ('도', 'Josa'), ('되다', 'Verb'), ('ㅋㅋ', 'KoreanParticle')]

    :param jvmpath: The path of the JVM passed to :py:func:`.init_jvm`.
    :param max_heap_size: Maximum memory usage limitation (Megabyte) :py:func:`.init_jvm`.
    """

    def pos(self, phrase, norm=False, stem=False, join=False):
        """POS tagger.
        In contrast to other classes in this subpackage,
        this POS tagger doesn't have a `flatten` option,
        but has `norm` and `stem` options.
        Check the parameter list below.

        :param norm: If True, normalize tokens.
        :param stem: If True, stem tokens.
        :param join: If True, returns joined sets of morph and tag.
        """

        tokens = self.jki.tokenize(
                    phrase,
                    jpype.java.lang.Boolean(norm),
                    jpype.java.lang.Boolean(stem)).toArray()
        if join:
            return [t for t in tokens]
        else:
            return [tuple(t.rsplit('/', 1)) for t in tokens]

    def nouns(self, phrase):
        """Noun extractor."""

        tagged = self.pos(phrase)
        return [s for s, t in tagged if t == 'Noun']

    def morphs(self, phrase, norm=False, stem=False):
        """Parse phrase to morphemes."""

        return [s for s, t in self.pos(phrase, norm=norm, stem=stem)]

    def phrases(self, phrase):
        """Phrase extractor."""

        return [p for p in self.jki.phrases(phrase).toArray()]
    
    def normalize(self, phrase):
        text = self.jki.normalize(phrase)
        return text

    def __init__(self, jvmpath=None, max_heap_size=1024):
        if not jpype.isJVMStarted():
            jvm.init_jvm(jvmpath, max_heap_size)

        oktJavaPackage = jpype.JPackage('kr.lucypark.okt')
        OktInterfaceJavaClass = oktJavaPackage.OktInterface
        self.jki = OktInterfaceJavaClass()
        self.tagset = utils.read_json('%s/data/tagset/twitter.json' % utils.installpath)
