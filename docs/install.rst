Installation
============

KoNLPy is not registered in PyPI yet.
Please install from source until further notice.

- Requirements
    - Python 2.6 or higher
    - JRE 1.7 or higher


Linux
-----

Install KoNLPy
''''''''''''''
    
.. sourcecode:: bash

    $ pip install git+https://github.com/e9t/konlpy.git

or

.. sourcecode:: bash

    $ git clone https://github.com/e9t/konlpy.git
    $ cd konlpy
    $ python setup.py install


.. _optional-installations:

Optional installations
''''''''''''''''''''''

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

Windows
-------

KoNLPy's compatibility with Windows is not stable yet.
However, if you would still like to put in some effort you can try the following.

1. Download the most recent release of KoNLPy from `GitHub <https://github.com/e9t/konlpy/releases>`_, and extract files. (Otherwise, you can just `clone` it).

    - Current release: |release|

2. In a terminal, go to the KoNLPy directory, and type ``python setup.py install``.

.. note::

    If you have installation errors with dependency packages, try installing them with `Christoph Gohlke's Windows Binaries <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ [#]_:

    - `jpype <http://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype>`_
    - `regex <http://www.lfd.uci.edu/~gohlke/pythonlibs/#regex>`_

3. (Optional) Download, extract [#]_, and install the most recent version of MeCab from the following links:

    - `mecab-ko <https://bitbucket.org/eunjeon/mecab-ko/downloads>`_
    - `mecab-ko-dic <https://bitbucket.org/eunjeon/mecab-ko-dic/downloads>`_
    - `mecab-python <https://code.google.com/p/mecab/downloads/list?q=python>`_


.. [#] `win-amd64` for 64-bit Windows, `win32` for 32-bit Windows.
.. [#] Having MinGW/MSYS or Cygwin installed may be more convenient. Otherwise, you can use `7zip <http://7-zip.org>`_ for the extraction of `tar` files.
