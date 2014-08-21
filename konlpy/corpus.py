import os

from . import utils


class CorpusLoader():
    """Loader for corpuses.

    .. code-block:: python

        from konlpy.corpus import kolaw
        fids = kolaw.fileids()
        fobj = kolaw.open(fids[0])
        print fobj.read(140)

    List of available corpuses:

    - *kolaw*: Korean law corpus.
    """

    def abspath(self, filename=None):
        """Absolute path of corpus file.
        If ``filename`` is *None*, returns absolute path of corpus.

        :param filename: Name of a particular file in the corpus.
        """
        basedir = '%s/data/%s' % (utils.installpath, self.name)
        if filename:
            return '%s/%s' % (basedir, filename)
        else:
            return '%s/' % basedir

    def fileids(self):
        """List of file IDs in the corpus."""
        return os.listdir(self.abspath())

    def open(self, filename):
        """Method to open a file in the corpus.
        Returns a file object.

        :param filename: Name of a particular file in the corpus.
        """
        return utils.load_txt(self.abspath(filename))

    def __init__(self, name=None):
        if not name:
            raise Exception("You need to input the name of the corpus")
        else:
            self.name = name


kolaw = CorpusLoader('kolaw')
