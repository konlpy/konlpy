# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from konlpy.stream.daum import DaumStreamer
from konlpy.constants import DATA_DIR
import glob


def test_daum_streamer():
    daum = DaumStreamer()
    daum.options.n_limits = 1
    daum.options.display_rank = True
    daum.options.verbose = True
    daum.options.interval = 3
    daum.stream()


def test_result_exists():
    """Check if files are correctly created. """

    items = glob.glob(DATA_DIR+"*trend*")
    assert len(items) > 0
