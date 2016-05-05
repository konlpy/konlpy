__title__ = 'KoNLPy'
__version__ = '0.4.4'
__author__ = 'Lucy Park'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2015 Lucy Park'

try:
    from .downloader import download
except IOError:
    pass
from .jvm import init_jvm
from . import corpus
from . import data
from . import internals
from . import tag
