# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import sys

if sys.version_info[0] >= 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen

from bs4 import BeautifulSoup
from argparse import ArgumentParser
from time import sleep

from konlpy.data import StringWriter
from konlpy.stream import BaseStreamer
from konlpy.utils import PropagatingThread, pprint


def get_current_trend():
    """Get current top trending words from naver

    Returns:
        counts: list of count
        keywords: list of keyword
    """

    url = 'https://www.daum.net/'
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    counts = []
    keywords = []

    item_list = soup.find("div", {"class": "realtime_part"}).findAll("div", {"class": "roll_txt"})
    item_list = [item.find("div", {"class": "rank_cont"}) for item in item_list]

    for item in item_list:
        count = item.find("span", {"class": "ir_wa"}).getText()
        keyword = item.find("span", {"class": "txt_issue"}).getText()
        counts.append(count)
        keywords.append(keyword)

    return counts, keywords


class DaumStreamer(BaseStreamer):
    """DaumStreamer helps to stream daum trending keywords asynchronously.

    .. code-block:: python

        >>> from konlpy.stream import daum
        >>> streamer = daum.DaumStreamer()
        >>> streamer.stream()
        김민승
        이유애린
        훈남정음
        소유진
        ...

    """

    def __init__(self, is_async=True):
        super(DaumStreamer, self).__init__(is_async=is_async)
        self.is_async = is_async

        parser = self.get_parser()
        parser.add_argument(
            '-d', '--display_rank',
            help="display rank in results and commandline.",
            action="store_true"
        )
        parser.add_argument(
            '-i', '--interval',
            help="streaming interval(secs)",
            default=60,
            type=int
        )
        parser.add_argument(
            '-n', '--n_limits',
            help="stop when this amount of trends are collected. 0 for forever",
            default=10,
            type=int
        )
        parser.add_argument(
            '--filename',
            help="filename to be saved.",
            default="trends.txt"
        )

        self.options, _ = parser.parse_known_args()
        self.writer = StringWriter(self.options.filename)

    def save_and_print(self):
        """collect current trending words and save or print"""

        counts, keywords = get_current_trend()
        if self.options.display_rank:
            for count, keyword in zip(counts, keywords):
                pair = "{}.{}".format(count, keyword)
                self.writer.write(pair)
                if self.options.verbose:
                    pprint(pair)

        else:
            for keyword in keywords:
                self.writer.write(keyword)
                if self.options.verbose:
                    pprint(keyword)

    def job(self):
        """Streaming job with intervals.

        Args:
            interval (int): Time interval
        """

        n_try = 0
        while (self.options.n_limits == 0) | (self.options.n_limits > n_try):
            n_try += 1
            self.save_and_print()
            sleep(self.options.interval)


def main():
    app = DaumStreamer(is_async=False)
    app.options.verbose = True
    app.show_options()
    app.stream()


if __name__ == '__main__':
    main()
