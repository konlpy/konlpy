#! /usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
import sys
try:
    import jpype
except ImportError:
    pass

from . import utils


def init_jvm(jvmpath=None):
    """Initializes the Java virtual machine (JVM).

    :param jvmpath: The path of the JVM. If left empty, inferred by :py:func:`jpype.getDefaultJVMPath`.

    """

    if jpype.isJVMStarted():
        logging.warning('JVM is already running. Do not init twice!')
        return

    folder_suffix = [
        '{0}', '{0}{1}bin',
        '{0}{1}jhannanum-0.8.4.jar',
        '{0}{1}kkma-2.0.jar',
        '{0}{1}komoran-2.4-e.jar',
        '{0}{1}shineware-common-2.0.jar', '{0}{1}shineware-ds-1.0.jar',
        '{0}{1}snakeyaml-1.12.jar', '{0}{1}scala-library-2.11.4.jar', '{0}{1}twitter-korean-text-2.4.3.jar', '{0}{1}twitter-text-1.10.1.jar',
        '{0}{1}*']

    javadir = '%s%sjava' % (utils.installpath, os.sep)

    args = [javadir, os.sep]
    classpath = os.pathsep.join(f.format(*args) for f in folder_suffix)

    jvmpath = jvmpath or jpype.getDefaultJVMPath()

    # NOTE: Temporary patch for Issue #76. Erase when possible.
    if sys.platform=='darwin'\
            and jvmpath.find('1.8.0') > 0\
            and jvmpath.endswith('libjvm.dylib'):
        jvmpath = '%s/lib/jli/libjli.dylib' % jvmpath.split('/lib/')[0]

    if jvmpath:
        jpype.startJVM(jvmpath, '-Djava.class.path=%s' % classpath,
                                '-Dfile.encoding=UTF8',
                                '-ea', '-Xmx768m')
    else:
        raise ValueError("Please specify the JVM path.")
