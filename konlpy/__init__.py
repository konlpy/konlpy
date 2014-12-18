__title__ = 'KoNLPy'
__version__ = '0.4.0'
__author__ = 'Lucy Park'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2014 Lucy Park'

from .downloader import download
from .jvm import init_jvm
from . import corpus
from . import data
from . import tag
