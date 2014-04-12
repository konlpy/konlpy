# KoNLPy

Korean morpheme analyzer on Python.

## Requirements

- Python 2.x

## Install

    $ git clone git@github.com:e9t/KoNLPy.git
    $ cd KoNLPy
    # python setup.py install

## Usage

    >>> import konlpy
    >>> n = konlpy.nouns(u'롯데마트가 판매하고 있는 흑마늘 양념 치킨이 논란이 되고 있다.)
    >>> print n
    (u'\ub86f\ub370\ub9c8\ud2b8', u'\ud310\ub9e4', u'\ud751\ub9c8\ub298', u'\uc591\ub150', u'\uce58\ud0a8', u'\ub17c\ub780')
    >>> ','.join(n)
    롯데마트,판매,흑마늘,양념,치킨,논란

    
## License
- [Apache v2.0](http://choosealicense.com/licenses/apache/)
