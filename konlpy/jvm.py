#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import logging
import os
import jpype


def init_jvm(jvmpath=None):
    """Initializes the Java virtual machine (JVM)."""

    if jpype.isJVMStarted():
        logging.warning('JVM is already running. Do not init twice!')
        return

    folder_suffix = ['{0}', '{0}{1}bin', '{0}{1}jhannanum-0.8.4.jar']
    javadir = '%s%sjava'\
            % (os.path.dirname(os.path.realpath(__file__)), os.sep)
    args = [javadir, os.sep]
    classpath = os.pathsep.join(f.format(*args) for f in folder_suffix)

    jvmpath = jvmpath or jpype.getDefaultJVMPath()
    jpype.startJVM(jvmpath, '-Djava.class.path=%s' % classpath, '-ea')
