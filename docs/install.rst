Installation
============

KoNLPy is not registered in PyPI yet.
Please install from source until further notice.

Requirements
------------

- Linux
- Python 2.x
- JRE 1.7

Install KoNLPy
--------------
    
.. sourcecode:: bash

    $ pip install git+https://github.com/e9t/konlpy.git

or

.. sourcecode:: bash

    $ git clone git@github.com:e9t/konlpy.git
    $ cd konlpy
    $ python setup.py install


.. _optional-installations:

Optional installations
----------------------

In order to use the MeCab morpheme analyzer in KoNLPy, install the followings:

- `mecab-ko <https://bitbucket.org/eunjeon/mecab-ko/downloads>`_

.. sourcecode:: bash

    $ wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.1.tar.gz
    $ tar zxfv mecab-0.996-ko-0.9.1.tar.gz
    $ cd mecab-0.996-ko-0.9.1
    $ ./configure
    $ make
    $ make check
    $ sudo make install

- `mecab-ko-dic <https://bitbucket.org/eunjeon/mecab-ko-dic/downloads>`_

.. sourcecode:: bash

    $ wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-1.6.1-20140814.tar.gz
    $ tar zxfv mecab-ko-dic-1.6.1-20140814.tar.gz
    $ cd mecab-ko-dic-1.6.1-20140814
    $ ./configure
    $ sudo ldconfig
    $ make
    $ sudo sh -c 'echo "dicdir=/usr/local/lib/mecab/dic/mecab-ko-dic" > /usr/local/etc/mecabrc'
    $ sudo make install

- `mecab-python <https://github.com/HiroyukiHaga/mecab-python>`_

.. sourcecode:: bash

    $ git clone https://github.com/HiroyukiHaga/mecab-python.git
    $ cd mecab-python
    $ python setup.py build
    $ sudo python setup.py install
