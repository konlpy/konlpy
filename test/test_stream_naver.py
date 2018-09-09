# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from konlpy.stream.naver import NaverStreamer
from konlpy.constants import DATA_DIR
import glob
import pytest


@pytest.mark.parametrize("is_async", [(True), (False)])
def test_naver_streamer(is_async):
    naver = NaverStreamer(is_async=is_async)
    naver.options.n_limits = 1
    naver.options.display_rank = True
    naver.options.verbose = True
    naver.options.interval = 3
    naver.stream()


def test_result_exists():
    """Check if files are correctly created. """

    items = glob.glob(DATA_DIR+"*trend*")
    assert len(items) > 0
