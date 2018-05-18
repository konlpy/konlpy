# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import sys
import textwrap

if sys.version_info[0] >= 3:
    import pickle
else:
    import cPickle as pickle

from konlpy import utils


#: A dictionary describing the formats that are supported by
#: ``konlpy.data.load()``.
#: Keys are format names and values are format descriptions.
FORMATS = {
    'pickle': 'A serialized Python object, stored using the ``pickle`` module.',
    'raw': 'The raw (byte string) contents of a file.',
}

#: A list of directories where the KoNLPy data package might reside.
#: These directories will be checked in order when looking for a resource.
#: Note that this allows users to substitute their own versions of resources.
path = []

# User-specified locations
path += [d for d in os.environ.get('KONLPY_DATA', '').split(os.pathsep) if d]
if os.path.expanduser('~/') != '~/':
        path += [os.path.expanduser('~/konlpy_data')]

# Windows common locations
if sys.platform.startswith('win'):
    path += [
        r'C:\konlpy_data', r'D:\konlpy_data', r'E:\konlpy_data',
        os.path.join(sys.prefix, 'konlpy_data'),
        os.path.join(sys.prefix, 'lib', 'konlpy_data'),
        os.path.join(os.environ.get('APPDATA', 'C:\\'), 'konlpy_data')]

# UNIX & OS X common locations
else:
    path += [
        '/usr/share/konlpy_data',
        '/usr/local/share/konlpy_data',
        '/usr/lib/konlpy_data',
        '/usr/local/lib/konlpy_data']

# Include KoNLPy installpath
path += ['%s/data' % utils.installpath]


def find(resource_url):
    """Find the path of a given resource URL by searching through
    directories in ``konlpy.data.path``.
    If the given resource is not found, raise a ``LookupError``,
    whose message gives a pointer to the installation instructions
    for ``konlpy.download()``.

    :type resource_url: str
    :param resource_url: The URL of the resource to search for.
        URLs are posix-style relative path names, such as ``corpora/kolaw``.
        In particular, directory names should always be separated by
        the forward slash character (i.e., '/'), which will be automatically
        converted to a platform-appropriate path separator by KoNLPy.
    """
    for p in path:
        f = os.path.join(p, resource_url)
        if os.path.exists(f):
            return FileSystemPathPointer(f)

    # Display message if the resource wasn't found
    sep = '*' * 70
    msg = textwrap.fill(
        'Resource %s not found. Please use the KoNLPy data downloader to obtain the resource: >>> konlpy.download()' % resource_url,
        initial_indent='  ',
        subsequent_indent='  ',
        width=66)
    msg += '\n  Searched in:' + ''.join('\n  - %s' % p for p in path)
    raise LookupError('\n%s\n%s\n%s' % (sep, msg, sep))


def load(resource_url, format='auto'):
    """Load a given resource from the KoNLPy data package.
    If no format is specified, ``load()`` will attempt to determine a format
    based on the resource name's file extension.
    If that fails, ``load()`` will raise a ``ValueError`` exception.

    :type resource_url: str
    :param resource_url: A URL specifying where the resource should be loaded from.
    :param format: Format type of resource.
    """

    if format == 'auto':
        format = os.path.splitext(resource_url)[-1].strip('.')

    if format == 'pickle':
        resource_val = pickle.load(find(resource_url))
    elif format == 'raw':
        resource_val = find(resource_url).open()
    else:
        assert format not in FORMATS
        raise ValueError('Unknown format type: %s' % format)

    return resource_val


class PathPointer(object):
    """An abstract base class for path pointers. One subclass exists:
    1. ``FileSystemPathPointer``: Identifies a file by an absolute path.
    """
    def open(self, encoding='utf-8'):
        raise NotImplementedError('Abstract base class')

    def file_size(self):
        raise NotImplementedError('Abstract base class')


class FileSystemPathPointer(PathPointer, str):
    """A path pointer that identifies a file by an absolute path."""

    def __init__(self, path):
        path = os.path.abspath(path)
        if not os.path.exists(path):
            raise IOError('No such file or directory: %s' % path)
        self.path = path

    def open(self, encoding='utf-8'):
        return utils.load_txt(self.path)

    def file_size(self):
        return os.stat(self.path).st_size


__all__ = [
    'find', 'load',
    'path', 'FileSystemPathPointer', 'PathPointer']
