# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from konlpy.stream import DCInsideStreamer
import glob


def test_dcinside_streamer():
    streamer = DCInsideStreamer()
    streamer.options.gallery_id = 'cat'
    streamer.options.verbose = True
    streamer.options.final_post_id = 5
    streamer.stream()
