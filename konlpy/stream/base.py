# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import sys

from argparse import ArgumentParser
from konlpy.utils import PropagatingThread, pprint

if sys.version_info[0] >= 3:
    import urllib3 as urllib
else:
    import urllib2 as urllib

    class RecursionError(Exception):
        pass


__all__ = ['KonlpyStreamerError', 'BaseStreamer']


class KonlpyStreamerError(Exception):
    def __init__(self, message, streamer):
        self.message = message
        self.streamer = streamer

    def __str__(self):
        return "%s has crashed. \n%s" % (self.streamer, self.message)


class BaseStreamer(object):
    """BaseStreamer class contains:

    Methods:
        get_parser: returns initial argument parser
        show_options: show options that can be used or parsed
        stream: try asynchronous streaming using job method
    """

    def __init__(self, is_async=True):
        self.is_async = is_async
        self.retry = 3
        self.recursion = 0

    def get_parser(self):
        """customized argument parser to set various parameters

        Returns:
            object: argument parser.
        """

        parser = ArgumentParser()
        parser.add_argument(
            '-v', '--verbose',
            help="increase verbosity",
            action="store_true"
        )
        return parser

    def show_options(self):
        """Print out options available and predefined values."""

        for attr, value in sorted(vars(self.options).items()):
            pprint("{} = {}".format(attr, value))

    def stream(self):
        try:
            if self.is_async:
                self._thread = PropagatingThread(target=self.job)
                self._thread.start()
                self._thread.join()
            else:
                self.job()
        except RecursionError:
            return False
        except KeyboardInterrupt:
            pprint("User has interrupted.")
            return False
        except:
            if self.recursion < self.retry:
                pprint("Error has raised but continue to stream.")
                self.recursion += 1
                self.stream()
            else:
                raise
