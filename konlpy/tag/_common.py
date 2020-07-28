# -*- coding: utf-8 -*-
""" Common utility function for tagger classes """
from __future__ import absolute_import
from __future__ import unicode_literals
import sys


# For both Python 2 and Python 3 compatibility
if sys.version_info[0] >= 3:
    basestring = str


def validate_phrase_inputs(phrase):
    """validate if phrase input is provided in str format

    Args:
        phrase (str): phrase input
    """
    msg = "phrase input should be string, not %s" % type(phrase)
    assert isinstance(phrase, basestring), msg
