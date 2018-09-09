from __future__ import absolute_import

from konlpy.about import *

try:
    from konlpy.downloader import download
except IOError:
    pass
<<<<<<< master
=======
<<<<<<< HEAD
from .jvm import init_jvm
from . import corpus
from . import data
from . import internals
from . import tag
=======
>>>>>>> Revert "update experimental streaming interface from koshort"

from konlpy.jvm import init_jvm
from konlpy import (
    corpus,
    data,
<<<<<<< master
    stream,
    internals,
    tag
)
=======
    internals,
    tag
)
>>>>>>> parent of 82368b6... update experimental streaming interface from koshort
>>>>>>> Revert "update experimental streaming interface from koshort"
