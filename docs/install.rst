Installation
============

.. note::

    For troubleshooting information, see these pages:
    `Linux <https://github.com/konlpy/konlpy/issues?q=label%3Alinux>`_.
    `Mac OS <https://github.com/konlpy/konlpy/issues?q=label%3A"mac+os">`_.
    `Windows <https://github.com/konlpy/konlpy/issues?q=label%3Awindows>`_.
    Please record a `"New Issue" <https://github.com/konlpy/konlpy/issues/new>`_ if you have an error that is not listed.
    You can also see testing logs `here <https://docs.google.com/spreadsheets/d/1Ii_L9NF9gSLbsJOGqsf-zfqTtyhhthmJWNC2kgUDIsU/edit#gid=0>`_.

Ubuntu
------

1. From the command prompt, install KoNLPy.

.. sourcecode:: bash

    $ sudo apt-get install g++ openjdk-7-jdk # Install Java 1.7+
    $ sudo apt-get install python-dev; pip install konlpy     # Python 2.x
    $ sudo apt-get install python3-dev; pip3 install konlpy   # Python 3.x

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

    $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

Windows
-------

1. Do you have Java 1.7+ installed?
2. Set `JAVA_HOME <http://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/index.html>`_.
3. Download and install `JPype1 (>=0.5.7) <http://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype>`_. [#]_ You may have to upgrade your `pip` version in order to install the downloaded `.whl` file.

.. sourcecode:: guess

    > pip install --upgrade pip
    > pip install JPype1-0.5.7-cp27-none-win_amd64.whl

4. From the command prompt, install KoNLPy.

.. sourcecode:: guess

    > pip install konlpy

.. warning::

    - KoNLPy's ``Mecab()`` class is not supported on Windows machines.

.. [#] `win-amd64` for 64-bit Windows, `win32` for 32-bit Windows.
.. [#] Having MinGW/MSYS or Cygwin installed may be more convenient. If you plan to use Git, `Git BASH <https://msysgit.github.io/>`_ is another good option. Otherwise, you can use `7zip <http://7-zip.org>`_ for the extraction of `tar` files.
