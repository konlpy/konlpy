Installation
============

.. note::

    For troubleshooting information, see these pages:
    `Linux <https://github.com/konlpy/konlpy/issues?q=label%3Alinux>`_.
    `Mac OS <https://github.com/konlpy/konlpy/issues?q=label%3A"mac+os">`_.
    `Windows <https://github.com/konlpy/konlpy/issues?q=label%3Awindows>`_.
    Please record a `"New Issue" <https://github.com/konlpy/konlpy/issues/new>`_ if you have an error that is not listed.
    You can also see testing logs `here <https://docs.google.com/spreadsheets/d/1Ii_L9NF9gSLbsJOGqsf-zfqTtyhhthmJWNC2kgUDIsU/edit#gid=0>`_.

Linux
-----

1. From the command prompt, install KoNLPy.

.. sourcecode:: bash

    $ sudo apt-get install python-dev python3-dev
    $ pip install konlpy    # Python 2.x
    $ pip3 install konlpy   # Python 3.x

2. Install MeCab (*optional*)

.. sourcecode:: bash

    $ sudo apt-get install curl
    $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

Mac OS
------

1. From the command prompt, install KoNLPy.

.. sourcecode:: bash

   $ pip install konlpy     # Python 2.x
   $ pip3 install konlpy    # Python 3.x

2. Install MeCab (*optional*)

.. sourcecode:: bash

   $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh) # (Optional) Install MeCab

Windows
-------

1. Download and install `JPype1 <http://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype>`_ (>=0.5.7) [#]_

.. sourcecode:: guess

    > pip install --upgrade pip
    > pip install --use-wheel --no-index --find-links=/download/path/to/JPype1‑0.5.7‑cp27‑none‑win_amd64.whl JPype1

2. From the command prompt, install KoNLPy.

.. sourcecode:: guess

    > pip install konlpy

3. Download, extract [#]_, and install the most recent version of MeCab from the following links (*optional*):

    - `mecab-ko <https://bitbucket.org/eunjeon/mecab-ko/downloads>`_
    - `mecab-ko-dic <https://bitbucket.org/eunjeon/mecab-ko-dic/downloads>`_
    - `mecab-python <https://code.google.com/p/mecab/downloads/list?q=python>`_

.. [#] `win-amd64` for 64-bit Windows, `win32` for 32-bit Windows.
.. [#] Having MinGW/MSYS or Cygwin installed may be more convenient. If you plan to use Git, `Git BASH <https://msysgit.github.io/>`_ is another good option. Otherwise, you can use `7zip <http://7-zip.org>`_ for the extraction of `tar` files.
