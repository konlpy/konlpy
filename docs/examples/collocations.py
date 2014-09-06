#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from konlpy.tag import Kkma
from konlpy.corpus import kolaw
from konlpy.utils import pprint
from nltk import collocations


bigram_measures = collocations.BigramAssocMeasures()
trigram_measures = collocations.TrigramAssocMeasures()

doc = kolaw.open('constitution.txt').read()
pos = Kkma().pos(doc)
words = [s for s, t in pos]
tags = [t for s, t in pos]


print('\nCollocations among tagged words:')
finder = collocations.BigramCollocationFinder.from_words(pos)
pprint(finder.nbest(bigram_measures.pmi, 10)) # top 5 n-grams with highest PMI

print('\nCollocations among words:')
ignored_words = [u'안녕']
finder = collocations.BigramCollocationFinder.from_words(words)
finder.apply_word_filter(lambda w: len(w) < 2 or w in ignored_words)
finder.apply_freq_filter(3) # only bigrams that appear 3+ times
pprint(finder.nbest(bigram_measures.pmi, 10))

print('\nCollocations among tags:')
finder = collocations.BigramCollocationFinder.from_words(tags)
pprint(finder.nbest(bigram_measures.pmi, 5))
