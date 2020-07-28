# -*- coding: utf-8 -*-
from __future__ import absolute_import
from konlpy import utils

import os


class CorpusLoader():
    """Loader for corpora.
    For a complete list of corpora available in KoNLPy,
    refer to :ref:`corpora`.

    .. code-block:: python

        >>> from konlpy.corpus import kolaw
        >>> fids = kolaw.fileids()
        >>> fobj = kolaw.open(fids[0])
        >>> print fobj.read(140)
        대한민국헌법

        유구한 역사와 전통에 빛나는 우리 대한국민은 3·1운동으로 건립된 대한민국임시정부의 법통과 불의에 항거한 4·19민주이념을 계승하고, 조국의 민주개혁과 평화적 통일의 사명에 입각하여 정의·인도와 동포애로써 민족의 단결을 공고히 하고, 모든 사회적 폐습과 불의를 타파하며, 자율과 조화를 바 바
    """

    def __init__(self, name=None):
        if not name:
            raise Exception("You need to input the name of the corpus")
        else:
            self.name = name

    def abspath(self, filename=None):
        """Absolute path of corpus file.
        If ``filename`` is *None*, returns absolute path of corpus.

        :param filename: Name of a particular file in the corpus.
        """
        basedir = '%s/data/corpus/%s' % (utils.installpath, self.name)
        if filename:
            return '%s/%s' % (basedir, filename)
        else:
            return '%s/' % basedir

    def fileids(self):
        """List of file IDs in the corpus."""
        return os.listdir(self.abspath())

    def open(self, filename):
        """Method to open a file in the corpus.
        Returns a file object.

        :param filename: Name of a particular file in the corpus.
        """
        return utils.load_txt(self.abspath(filename))


kolaw = CorpusLoader('kolaw')
kobill = CorpusLoader('kobill')
