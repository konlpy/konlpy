Installation
============

.. note::

    For troubleshooting information, see these pages:
    `Linux <https://github.com/konlpy/konlpy/issues?q=label%3AOS%2FLinux>`_.
    `Mac OS <https://github.com/konlpy/konlpy/issues?q=label%3AOS%2FMacOS>`_.
    `Windows <https://github.com/konlpy/konlpy/issues?q=label%3AOS%2FWindows>`_.
    Please record a `"New Issue" <https://github.com/konlpy/konlpy/issues/new>`_ if you have an error that is not listed.

.. Warning::

    Python 2 End of Life Announced as January 1st 2020.

    This page covers Python 3 only.  The last-known version for Python 2 is v0.5.2, install it via `pip install konlpy==v0.5.2`.


Ubuntu
------

Supported: Xenial(16.04.3 LTS), Bionic(18.04.3 LTS), Disco(19.04), Eoan(19.10)

1. Install dependencies

    .. sourcecode:: bash

        # Install Java 1.8 or up
        $ sudo apt-get install g++ openjdk-8-jdk python3-dev python3-pip curl

2. Install KoNLPy

    .. sourcecode:: bash

        $ python3 -m pip install --upgrade pip
        $ python3 -m pip install konlpy       # Python 3.x

3. Install MeCab (*optional*)

    .. sourcecode:: bash

        $ sudo apt-get install curl git
        $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)


CentOS
------

Supported: CentOS 7, 8

1. Install dependencies

    .. sourcecode:: bash

        $ sudo yum install gcc-c++ java-1.8.0-openjdk-devel python3 python3-devel python3-pip make diffutils

2. Install KoNLPy

    .. sourcecode:: bash

        $ python3 -m pip install --upgrade pip
        $ python3 -m pip install konlpy     # Python 3.x

3. Install MeCab (*optional*)

    .. sourcecode:: bash

        $ sudo yum install curl git
        $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)


Mac OS
------

1. Install KoNLPy

    .. sourcecode:: bash

       $ python3 -m pip install --upgrade pip
       $ python3 -m pip install konlpy        # Python 3.x

2. Install MeCab (*optional*)

    .. sourcecode:: bash

        $ bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)


Windows
-------

1. Does your Python installation's "bit version" match your Windows OS? If you're using a 64 bit Windows you need a 64 bit Python, and if you have a 32 bit Windows, you need a 32 bit Python. Reinstall your Python if your bit versions do not match.
    - How to check your Windows bit version

        .. image:: images/windows-bits.png
            :width: 600px

    - How to check your Python bit version

        .. image:: images/python-bits.png
            :width: 400px

2. Do you have a Java of version 1.7 or above installed, that matches your OS bit version? If not, `download and install a JDK <http://www.oracle.com/technetwork/java/javase/downloads/index.html>`_. Note again, that the bit versions must match.
3. Set `JAVA_HOME <http://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/index.html>`_.
4. Download and install the `JPype1 (>=0.5.7) <http://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype>`_ that matches your bit version: `win32` for 32 bit and `win-amd64` for 64 bit. You may have to `upgrade your pip <https://pip.pypa.io/en/stable/installing.html#upgrade-pip>`_ in order to install the downloaded `.whl` file.

    .. sourcecode:: guess

        > pip install --upgrade pip
        > pip install JPype1-0.5.7-cp27-none-win_amd64.whl

5. From the command prompt, install KoNLPy.

    .. sourcecode:: guess

        > pip install konlpy

.. warning::

    - KoNLPy's ``Mecab()`` class is not supported on Windows machines.


Docker
------

If you are familiar with Docker, it is easy to install `konlpy` and `java-1.7-openjdk` on `python:3` image.

    .. sourcecode:: docker

        > FROM python:3

        > ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk/jre
        > RUN apt-get update && apt-get install -y g++ default-jdk
        > RUN pip install konlpy

        > # Write left part as you want
