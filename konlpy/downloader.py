#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


import hashlib
import json
import os
import subprocess
import sys
import tarfile
import zipfile
if sys.version_info[0] < 3:
    import urllib
else:
    import urllib.request as urllib

from . import internals


def default_download_dir():
    """
    Returns the directory to which packages will be downloaded by default.
    This value can be overriden using the constructor,
    or on a case-by-case basis using the ``download_dir`` argument
    when calling ``download()``.

    On Windows, the default download directory is ``PYTHONHOME/lib/konlpy``,
    where *PYTHONHOME* is the directory containing Python e.g., ``C:\\Python27``.

    On all other platforms, the default directory is the first of the following
    which exists or which can be created with write permission:
    ``/usr/share/konlpy_data``, ``/usr/local/share/konlpy_data``,
    ``/usr/lib/konlpy_data``, ``/usr/local/lib/konlpy_data``, ``~/konlpy_data``.
    """

    konlpydir = internals.get_datadir()

    # On Windows, use %APPDATA%
    if sys.platform == 'win32' and 'APPDATA' in os.environ:
        homedir = os.environ['APPDATA']

    # Otherwise, install in the user's home directory
    else:
        homedir = os.path.expanduser('~/')
        if homedir == '~/':
            raise ValueError("Could not find a default download directory")

    return os.path.join(homedir, 'konlpy_data')


class Downloader(object):
    """
    A class used to access the KoNLPy data server, which can be used to download packages.
    """

    PACKAGE_URL = 'http://konlpy.github.io/konlpy-data/packages/%s.%s'
    SCRIPT_URL = 'http://konlpy.github.io/konlpy-data/packages/%s.sh'
    INDEX_URL = 'http://konlpy.github.io/konlpy-data/index.json'

    INSTALLED = 'installed'
    NOT_INSTALLED = 'not installed'
    STALE = 'corrupt or out of date'

    def download(self, id=None, download_dir=None):
        """The KoNLPy data downloader.
        With this module you can download corpora, models and other data packages
        that can be used with KoNLPy.

        Downloading packages
        ====================

        Individual packages can be downloaded by passing a single argument, the package identifier for the package that should be downloaded:

        >>> download('corpus/kobill')
        [konlpy_data] Downloading package 'kobill'...
        [konlpy_data]   Unzipping corpora/kobill.zip.

        To download all packages, simply call ``download`` with the argument 'all':

        >>> download('all')
        [konlpy_data] Downloading package 'kobill'...
        [konlpy_data]   Unzipping corpora/kobill.zip.
        ...

        """
        if download_dir is None:
            download_dir = self._download_dir

        if id is None:
            raise ValueError("Please specify a package to download. To download all available packages, pass 'all' to the argument: ``konlpy.download('all')``.")
        elif id == 'all':
            raise NotImplementedError("This function is not implemented yet. Please download each package individually until further notice.")
        else:
            info = self._get_info(id)
            for msg in self._download_package(info, download_dir):
                print(msg)

    def status(self, info_or_id=None, download_dir=None):
        self.index = json.loads(urllib.urlopen(self.INDEX_URL).read().decode())
        """
        Return a constant describing the local status of the given package.
        Status can be one of ``INSTALLED``, ``NOT_INSTALLED``, or ``STALE``.
        """

        if info_or_id is None:
            raise ValueError("Please specify a package to download.")
        if isinstance(info_or_id, dict):
            info = info_or_id
        else:
            id = info_or_id
            try:
                info = self.index[id]
            except KeyError:
                raise ValueError("Package does not exist. Please check the package name.")

        if download_dir is None:
            download_dir = self._download_dir

        filepath = os.path.join(download_dir, info['filepath'], info['ext'])

        return self._pkg_status(info, filepath)

    def _pkg_status(self, info, filepath):
        if not os.path.exists(filepath):
            return self.NOT_INSTALLED

        # Check if the file has the correct size
        try:
            filestat = os.stat(filepath)
        except OSError:
            return self.NOT_INSTALLED

        if filestat.st_size != int(info['size']):
            return self.STALE

        # Check if the file's checksum matches
        checksum = hashlib.md5(open(filepath, 'rb').read()).hexdigest()
        if checksum != info['checksum']:
            return self.STALE

        # TODO: Check if file has been properly unzipped

        # TODO: Check if file has been properly installed
        if info.get('install'):
            return self.NOT_INSTALLED

        # Otherwise, everything looks good
        return self.INSTALLED

    def _download_package(self, info, download_dir, force=False):
        yield "KoNLPy downloader"

        # Do we already have the current version?
        status = self.status(info, download_dir)
        if not force and status == self.INSTALLED:
            yield "[konlpy_data] '%s' is already installed" % info['id']
            return

        # Check for (and remove) any old/stale version
        filepath = os.path.join(download_dir, '%s.%s' % (info['filepath'], info['ext']))
        if os.path.exists(filepath):
            if status == self.STALE:
                yield "[konlpy_data] This file is stale"
            os.remove(filepath)

        # Ensure the download_dir exists
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        subdir = os.path.dirname(filepath)
        if not os.path.exists(subdir):
            os.mkdir(subdir)

        # Download file. This will raise an IOError if the URL is not found.
        url = self.PACKAGE_URL % (info['filepath'], info['ext'])
        try:
            yield "[konlpy_data] Downloading package '%s'..." % info['id']
            # TODO: progress bar
            urllib.urlretrieve(url, filepath)
        except IOError as e:
            yield "[konlpy_data] Error downloading file"
            return
        yield "[konlpy_data] Download finished"

        # If it's a zipfile, uncompress it.
        ext = os.path.splitext(filepath)[-1]
        if ext in ['.zip', '.tar']:
            yield "[konlpy_data] Unzipping file %s" % filepath
            self._unzip_file(filepath, ext)

        # If it says to install, use a shell script for installation
        if info.get('install'):
            url = self.SCRIPT_URL % info['filepath']
            shpath = os.path.join(download_dir, '%s.sh' % info['filepath'])
            self._exec_shell(url, shpath, download_dir)

        yield "Done"

    def _exec_shell(self, url, shpath, download_dir):
        urllib.urlretrieve(url, shpath)
        internals.chmod(shpath)
        subprocess.call(['sudo', shpath, download_dir])

    def _unzip_file(self, filepath, ext):
        try:
            if ext == '.zip':
                zf = zipfile.ZipFile(filepath)
                zf.extractall(os.path.dirname(filepath))
                zf.close()
            elif ext == '.tar':
                tf = tarfile.open(filepath)
                tf.extractall(os.path.dirname(filepath))
                tf.close()
        except Exception as e:
            raise ValueError('Error reading file %r!\n%s' % (filepath, e))

    def _get_info(self, id):
        self.index = json.loads(urllib.urlopen(self.INDEX_URL).read().decode())
        if self.index.get(id):
            return self.index.get(id)
        else:
            raise ValueError("Could not find a matching item to download")

    def __init__(self, download_dir=None):
        self._download_dir = download_dir

# Aliases
_downloader = Downloader(default_download_dir())
download = _downloader.download
