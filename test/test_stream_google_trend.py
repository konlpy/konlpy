# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from konlpy.stream import GoogleTrendStreamer
import pytest

# FIXME: init_date가 고정되어 시간이 지났을 때 test에 실패할 가능성이 있음.
@pytest.mark.parametrize("is_async", [(True), (False)])
def test_google_trend_streamer(is_async):
    streamer = GoogleTrendStreamer(is_async=is_async)
    streamer.options.verbose = True
    streamer.options.init_date = '20180514'
    streamer.options.final_date = '20180601'
    streamer.stream()
