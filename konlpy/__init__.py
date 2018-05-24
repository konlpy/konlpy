from __future__ import absolute_import

__title__ = 'KoNLPy'
__author__ = 'Team KoNLPy'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2018 Team KoNLPy'
__version__ = '0.4.5'

try:
    from konlpy.downloader import download
except IOError:
    pass

from konlpy.jvm import init_jvm
from konlpy import (
    corpus,
    data,
    internals,
    tag
)
