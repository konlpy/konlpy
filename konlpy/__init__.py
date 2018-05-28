from __future__ import absolute_import

from konlpy.about import *

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
