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


class StopwordsLoader(CorpusLoader):
    """Loader for stopwords.
    For a complete list of stopwords available in KoNLPy,
    refer to :ref:`stopwords`.

    .. code-block:: python

        >>> from konlpy.corpus import stopwords
        >>> stopwords.words()
        ['!', '"', '$', ... ]
        >>> stopwords.morphs(analyzer='kkma')
        ['가/VV', '가지/VV', '같/VA', ... ]
        >>> stopwords.include('word', ['헐', '네'])
        >>> stopwords.exclude('word', ['진짜'])
    """

    def load_stopwords(self, filename, stype='word'):
        stopwords_obj = self.open(filename)
        stopwords = stopwords_obj.read().split('\n')
        if stype == 'morph':
            n_stopwords = [[] for _ in range(len(stopwords[0].split('\t')))]
            for stopword in stopwords:
                for idx, word in enumerate(stopword.split('\t')):
                    if word == '':
                        continue
                    n_stopwords[idx].extend(word.split(','))
            stopwords = {stopwords[0]: stopwords[1:] for stopwords in n_stopwords}
        return stopwords

    def __init__(self, name):
        if not name:
            raise Exception("You need to input the name of the corpus")
        else:
            self.name = name

        self.base_morphs = self.load_stopwords('stopwords.morph.txt', 'morph')
        self.base_words = self.load_stopwords('stopwords.word.txt', 'word')
        self.include_morphs = []
        self.include_words = []
        self.exclude_morphs = []
        self.exclude_words = []

    def words(self):
        return list(set(self.base_words) | set(self.include_words) - set(self.exclude_words))

    def morphs(self, analyzer):
        if analyzer not in self.base_morphs:
            raise Exception("You need to set the valid analyzer")
        else:
            return list(set(self.base_morphs[analyzer]) | set(self.include_morphs) - set(self.exclude_morphs))

    def include(self, unit, words):
        if unit == 'word':
            self.include_word = words
        else:
            self.include_morph = words

    def exclude(self, analyzer='kkma'):
        return self.morphs


kolaw = CorpusLoader('kolaw')
kobill = CorpusLoader('kobill')
stopwords = StopwordsLoader('stopwords')
