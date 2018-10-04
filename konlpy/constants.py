# -*- coding: utf-8 -*-
"""Constants used in konlpy library. """
import os

DATA_DIR = "data/"
ALPHABET = ["가", "나", "다", "라", "마", "바", "사", "아", "자", "차", "카", "타", "파", "하"]


def make_dir(directory=DATA_DIR):
    """make konlpy data directory to store streaming data"""

    if not os.path.exists(directory):
        os.mkdir(directory)
