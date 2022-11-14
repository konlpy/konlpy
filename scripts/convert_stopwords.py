#!/usr/bin/env python3


import os
import sys
import json
import argparse


VERBOSE = 0


def read_bab2min(fname):
    '''
    $ head -3 /tmp/bab2min.txt
    이  VCP 0.018279601
    있  VA  0.011699048
    하  VV  0.009773658
    '''
    stopwords = []
    with open(fname) as fp:
        for buf in fp:
            line = buf.rstrip().split('\t')
            if len(line) != 3:
                continue
            morph, tag, ratio = line
            stopword = '{}/{}'.format(morph, tag)
            stopwords.append(stopword)
    return stopwords


def read_6(fname):
    '''
    $ head -3 /tmp/6.txt
    ["!","\"","$","%","&","'","(",")","*","+",",","-", ...]
    '''
    stopwords = []
    with open(fname) as fp:
        line = fp.read().rstrip()
        stopwords = json.loads(line)
    return stopwords


def read_lined_stopwords(fname):
    '''
    $ head -3 /tmp/spikeekips.txt
    가
    가까스로
    가령
	...
    '''
    stopwords = []
    with open(fname) as fp:
        for buf in fp:
            line = buf.rstrip()
            word = line
            stopwords.append(word)
    return stopwords


def read_stopwords_iso(fname):
    stopwords = []
    with open(fname) as fp:
        line = fp.read().rstrip()
        stopwords = json.loads(line)
        if 'ko' in stopwords:
            stopwords = stopwords['ko']
        else:
            stopwords = [] 
    return stopwords


def read_many_stop_words(fname):
    stopwords = []
    import many_stop_words as mstopwords
    stopwords = list(mstopwords.get_stop_words('kr'))
    return stopwords


STOPWORDS = {
    'morph': [
        {'name': 'bab2min', 'func': read_bab2min, 'file': '/tmp/cfile2.uf@241D6F475873C2B1010DEA.txt'}
    ],
    'word': [
        {'name': '6', 'func': read_6 , 'file': '/tmp/ko.json'},
        {'name': 'spikeekips', 'func': read_lined_stopwords, 'file': '/tmp/stopwords-ko.txt'},
        {'name': 'stopwords-iso', 'func': read_stopwords_iso, 'file': '/tmp/stopwords-iso.json'},
        {'name': 'many-stop-words', 'func': read_many_stop_words, 'file': None}
    ]
}


def fit_stopwords_to_analyzer(stopwords, c_table):
    n_stopwords = []
    for stopword in stopwords:
        morph, tag = stopword.rsplit('/')
        if tag in c_table:
            # print(c_table[tag])
            a_stopword = []
            for a_tags in c_table[tag]:
                if a_tags == '':
                    a_morph_tag = ''
                else:
                    a_tags = a_tags.split(',')
                    a_morph_tag = ','.join(['{}/{}'.format(morph, a_tag) for a_tag in a_tags])
                a_stopword.append(a_morph_tag)
            a_stopword = '\t'.join(a_stopword)
            n_stopwords.append(a_stopword)
    return n_stopwords


def read_stopwords(unit, c_table=None):
    global VERBOSE
    if VERBOSE > 0:
        print('{}\t{}\t{}\t{}'.format('UNIT', 'NAME', 'FUNC', 'FNAME'))

    all_stopwords = []
    for item in STOPWORDS[unit]:
        name, func, fname = item['name'], item['func'], item['file']
        stopwords = func(fname)
        if c_table:
            stopwords = fit_stopwords_to_analyzer(stopwords, c_table)
        all_stopwords.extend(stopwords)

        if VERBOSE > 0:
            print('{}\t{}\t{}\t{}'.format(unit, name, func, fname))
            print('{}'.format(', '.join(stopwords[:10])))

    all_stopwords = sorted(list(set(all_stopwords)))
    return all_stopwords


def dump_stopwords(stopwords, unit, c_table, install_path):
    fname = '{}/stopwords.{}.txt'.format(install_path, unit)
    with open(fname, 'w') as fp:
        if c_table:
            fp.writelines('\t'.join(c_table['sejong']) + '\n')
        fp.writelines('\n'.join(stopwords))


def read_convert_table(fname):
    '''
    {'NNG': [], 'NNP': []}
    '''
    c_table = {}
    fp_c_table = open(fname, 'r')

    if fp_c_table.readable() is False:
        print('convert table file is not readable.', file=sys.stderr)
        sys.exit(1)

    for idx, buf in enumerate(fp_c_table):
        line = buf.rstrip().split('\t')
        sejong_tag, analyzer_tags = line[0], line[2: ]
        c_table[sejong_tag] = analyzer_tags

    fp_c_table.close()

    return c_table


if __name__ == '__main__':
    '''
    여러 source에서 수집한 stopwords 파일들을 konlpy에서 사용할 형태로 가공합니다.
    
    stopwords의 형태는 unit에 따라 2가지로 나눠집니다.
    unit = morph or word

    두가지 unit을 한번에 처리하기 위해서는 unit을 all로 지정합니다.

    입력된 unit에 맞게 미리 지정된 경로에서 stopword를 읽어옵니다.
    중복된 stopword를 제거하고, 지정된 파일로 저장합니다.

    morph = stopwords.morph.txt
    word = stopwords.word.txt
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', dest='verbose', default=0, help='set verbosity level')
    parser.add_argument('-u', '--unit', action='store', dest='unit', default='all', help='set update stopwords unit(morph | word | all(default))')
    parser.add_argument('-t', '--conv-table', action='store', dest='c_table_file', default='convert_table.txt', help='set convert table path for stopwords.morphs.txt')
    parser.add_argument('-p', '--install-path', action='store', dest='install_path', default=os.getcwd(), help='set install path')
    options = parser.parse_args()

    VERBOSE = options.verbose
    unit = options.unit
    c_table_file = options.c_table_file
    install_path = options.install_path

    if unit not in ['all', 'morph', 'word']:
        print('UNIT is not acceptable', file=sys.stderr)
        sys.exit(1)

    c_table = read_convert_table(c_table_file)

    if unit in ['all', 'morph']:
        stopwords = read_stopwords('morph', c_table)
        dump_stopwords(stopwords, 'morph', c_table, install_path)

    if unit in ['all', 'word']:
        stopwords = read_stopwords('word')
        dump_stopwords(stopwords, 'word', None, install_path)
