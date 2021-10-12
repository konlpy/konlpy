# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
import os
import sys
try:
    import jpype
except ImportError:
    pass

from konlpy import utils


def init_jvm(jvmpath=None, max_heap_size=1024):
    """Initializes the Java virtual machine (JVM).

    :param jvmpath: The path of the JVM. If left empty, inferred by :py:func:`jpype.getDefaultJVMPath`.
    :param max_heap_size: Maximum memory usage limitation (Megabyte). Default is 1024 (1GB). If you set this value too small, you may got out of memory. We recommend that you set it 1024 ~ 2048 or more at least. However, if this value is too large, you may see inefficient memory usage.

    """

    if jpype.isJVMStarted():
        logging.warning('JVM is already running. Do not init twice!')
        return

    folder_suffix = [
        # JAR
        '{0}',
        # Java sources
        '{0}{1}bin',
        '{0}{1}*',
        # Hannanum
        '{0}{1}jhannanum-0.8.4.jar',
        # Kkma
        '{0}{1}kkma-2.0.jar',
        # Komoran3
        '{0}{1}aho-corasick.jar',
        '{0}{1}shineware-common-1.0.jar',
        '{0}{1}shineware-ds-1.0.jar',
        '{0}{1}komoran-3.0.jar',
        # Twitter (Okt)
        '{0}{1}snakeyaml-1.12.jar',
        '{0}{1}scala-library-2.12.3.jar',
        '{0}{1}open-korean-text-2.1.0.jar',
        '{0}{1}twitter-text-1.14.7.jar',
        '{0}{1}*'
    ]

    javadir = '%s%sjava' % (utils.installpath, os.sep)

    args = [javadir, os.sep]
    classpath = [f.format(*args) for f in folder_suffix]

    jvmpath = jvmpath or jpype.getDefaultJVMPath()

    # NOTE: Temporary patch for Issue #76. Erase when possible.
    if sys.platform == 'darwin'\
            and jvmpath.find('1.8.0') > 0\
            and jvmpath.endswith('libjvm.dylib'):
        jvmpath = '%s/lib/jli/libjli.dylib' % jvmpath.split('/lib/')[0]

    if jvmpath:
        jpype.startJVM(jvmpath, '-Dfile.encoding=UTF8',
                                '-ea', '-Xmx{}m'.format(max_heap_size),
                                classpath=classpath,
                                convertStrings=True)
    else:
        raise ValueError("Please specify the JVM path.")
