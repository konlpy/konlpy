# KoNLPy

Korean morpheme analyzer on Python.


## Requirements

- Python 2.x


## Install

    # pip install git+https://github.com/e9t/konlpy.git

or

    $ git clone git@github.com:e9t/konlpy.git
    $ cd konlpy
    # python setup.py install



## Usage

    >>> import konlpy
    >>> hannanum = konlpy.Hannanum()

    >>> hannanum.morph(u'롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다.)
    [[[(u'\ub86f\ub370\ub9c8\ud2b8', u'ncn'), (u'\uac00', u'jcc')],
      [(u'\ub86f\ub370\ub9c8\ud2b8', u'ncn'), (u'\uac00', u'jcs')],
      [(u'\ub86f\ub370\ub9c8\ud2b8\uac00', u'ncn')],
      [(u'\ub86f\ub370\ub9c8\ud2b8', u'nqq'), (u'\uac00', u'jcc')],
      [(u'\ub86f\ub370\ub9c8\ud2b8', u'nqq'), (u'\uac00', u'jcs')],
      [(u'\ub86f\ub370\ub9c8\ud2b8\uac00', u'nqq')]],
     [[(u'\ud310\ub9e4', u'ncpa'), (u'\ud558\uace0', u'jcj')],
      [(u'\ud310\ub9e4', u'ncpa'), (u'\ud558\uace0', u'jct')],
      [(u'\ud310\ub9e4', u'ncpa'), (u'\ud558', u'xsva'), (u'\uace0', u'ecc')],
      [(u'\ud310\ub9e4', u'ncpa'), (u'\ud558', u'xsva'), (u'\uace0', u'ecs')],
      [(u'\ud310\ub9e4', u'ncpa'), (u'\ud558', u'xsva'), (u'\uace0', u'ecx')],
      [(u'\ud310\ub9e4', u'ncpa'),
       (u'\ud558', u'xsva'),
       (u'\uc5b4', u'ef'),
       (u'\uace0', u'jcr')]],
        ...
     [[(u'\uc788', u'paa'), (u'\ub2e4', u'ef')],
      [(u'\uc788', u'px'), (u'\ub2e4', u'ef')]]]

    >>> hannanum.nouns(u'다람쥐 헌 쳇바퀴 타고파')
    [u'\ub2e4\ub78c\uc950', u'\uccc7\ubc14\ud034', u'\ud0c0\uace0', u'\ud30c']

    >>> hannanum.pos(u'웃으면 더 행복합니다!')
    [(u'\uc6c3', u'P'),
     (u'\uc73c\uba74', u'E'),
     (u'\ub354', u'M'),
     (u'\ud589\ubcf5', u'N'),
     (u'\ud558', u'X'),
     (u'\u3142\ub2c8\ub2e4', u'E')]

    >>> hannanum.pos(u'웃으면 더 행복합니다!', ntags=22)
    [(u'\uc6c3', u'PV'),
     (u'\uc73c\uba74', u'EC'),
     (u'\ub354', u'MA'),
     (u'\ud589\ubcf5', u'NC'),
     (u'\ud558', u'XS'),
     (u'\u3142\ub2c8\ub2e4', u'EF')]

    
## Todos

- Add user dic
- Add function `load_common_dic`
- nltk 데이터 폴더 구조 참고해서 그처럼 저장하기
- lucene 형태소 분석기도 넣기


## License
- [Apache v2.0](http://choosealicense.com/licenses/apache/)
