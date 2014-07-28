#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

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

def PrettyPrinter(src, dpth=0):
    tabs = lambda n: ' ' * n * 1 # or 2 or 8 or...

    if isinstance(src, list):
        printing_list = []

        if isinstance(src[0], tuple) :
            [printing_list.append("+".join(litem)) for litem in src]
            changed_value = ",".join(printing_list)
        elif isinstance(src[0], unicode) :
            [printing_list.append("".join(litem)) for litem in src]
            changed_value = ",".join(printing_list)
        else:
            for litem in src:
                llist = PrettyPrinter(litem,dpth+1)
                if not (llist is None): printing_list.append(llist+",\n"+tabs(dpth))
            changed_value = "".join(printing_list)
        return "["+changed_value+"]"

def concat(phrase):
    return phrase.replace('\n', '')

class Hannanum():

    def morph(self, phrase):
        phrase = concat(phrase)
        result = self.jhi.morphAnalyzer(phrase)
        return parse(result)

    def nouns(self, phrase):
        phrase = concat(phrase)
        return list(self.jhi.extractNoun(phrase))

    def pos(self, phrase, ntags=9):
        phrase = concat(phrase)
        if ntags==9:
            result = self.jhi.simplePos09(phrase)
        elif ntags==22:
            result = self.jhi.simplePos22(phrase)
        else:
            raise Exception('ntags in [9, 22]')
        return parse(result, flatten=True)

    def __init__(self, jvmpath=None):
        jhannanumJavaPackage = jpype.JPackage('kr.lucypark.jhannanum.comm')
        HannanumInterfaceJavaClass = jhannanumJavaPackage.HannanumInterface
        self.jhi = HannanumInterfaceJavaClass() # Java instance


if __name__=='__main__':
    from init_jvm import init_jvm
    from pprint import pprint

    phrase = u'롯데마트가 판매하고 있는 흑마늘'

    init_jvm()
    hi = Hannanum()

    print '\n'+PrettyPrinter(hi.morph(phrase))
    print '\n'+PrettyPrinter(hi.nouns(phrase))
    print '\n'+PrettyPrinter(hi.pos(phrase))

    print '\nMorph:'; pprint(hi.morph(phrase))
    print '\nNouns:'; pprint(hi.nouns(phrase))
    print '\nPos09:'; pprint(hi.pos(phrase))
    print '\nPos22:'; pprint(hi.pos(phrase, ntags=22))

