from __future__ import absolute_import

__title__ = 'KoNLPy'
__author__ = 'Lucy Park'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2015 Lucy Park'

# Single-source package version
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('koshort').version
except pkg_resources.DistributionNotFound:
    __version__ = "dev"

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
