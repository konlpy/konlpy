# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from konlpy.stream import DCInsideStreamer
import glob
import pytest


@pytest.mark.parametrize("is_async", [(True), (False)])
def test_dcinside_streamer(is_async):
    streamer = DCInsideStreamer(is_async=is_async)
    streamer.options.gallery_id = 'cat'
    streamer.options.verbose = True
    streamer.options.final_post_id = 5
    streamer.stream()
