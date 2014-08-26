Installation
============

Requirements
------------

- Python 2.6 or higher [#]_
- JRE 1.7 or higher


Linux
-----

.. sourcecode:: bash

    $ apt-get install openjdk-7-jdk
    $ pip install JPype1
    $ pip install konlpy
    $ bash <(curl -s https://raw.githubusercontent.com/e9t/konlpy/master/scripts/mecab.sh) # (Optional) Install MeCab


Windows
-------

1. Download and install `jpype <http://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype>`_ [#]_

2. From the command prompt, install KoNLPy.

.. sourcecode:: guess

    C:\> pip install konlpy

3. (Optional) Download, extract [#]_, and install the most recent version of MeCab from the following links:

    - `mecab-ko <https://bitbucket.org/eunjeon/mecab-ko/downloads>`_
    - `mecab-ko-dic <https://bitbucket.org/eunjeon/mecab-ko-dic/downloads>`_
    - `mecab-python <https://code.google.com/p/mecab/downloads/list?q=python>`_

.. [#] Python 3.x not supported yet.
.. [#] `win-amd64` for 64-bit Windows, `win32` for 32-bit Windows.
.. [#] Having MinGW/MSYS or Cygwin installed may be more convenient. Otherwise, you can use `7zip <http://7-zip.org>`_ for the extraction of `tar` files.
