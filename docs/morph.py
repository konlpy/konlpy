#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import csv
from time import time

from konlpy import tag
from konlpy.corpus import kolaw
from konlpy.utils import pprint


def tagging(tagger, text):
    return getattr(tag, tagger)().pos(text)

def measure(taggers, mult=6):
    doc = kolaw.open('constitution.txt').read()*6
    data = [[''] + taggers]
    for i in range(mult):
        doclen = 10**i
        times = [time()]
        diffs = [doclen]
        for tagger in taggers:
            r = tagging(tagger, doc[:doclen])
            times.append(time())
            diffs.append(times[-1] - times[-2])
            print '%s\t%s\t%s' % (tagger[:5], doclen, diffs[-1])
            pprint(r[:5])
        data.append(diffs)
        print
    return data


if __name__=='__main__':
    taggers = [t for t in dir(tag) if t[0].isupper()]
    data = measure(taggers, mult=6)
    with open('morph.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
