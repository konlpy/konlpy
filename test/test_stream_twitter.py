import subprocess
import time
import glob
import os


def test_twitter_streamer():
    from konlpy.stream import TwitterStreamer
    os.system("stream_twitter")
