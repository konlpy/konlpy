# Inspired from:
# https://packaging.python.org/guides/single-sourcing-package-version/
# https://github.com/pypa/warehouse/blob/master/warehouse/__about__.py
# https://github.com/explosion/spaCy/blob/master/spacy/about.py

__all__ = [
    '__author__',
    '__copyright__',
    '__email__',
    '__license__',
    '__summary__',
    '__title__',
    '__url__',
    '__version__',
]

__title__ = 'KoNLPy'
__version__ = '0.5.1'

__author__ = 'Team KoNLPy'
__email__ = 'konlpy@googlegroups.com'
__url__ = 'http://konlpy.org'

__summary__ = 'Python package for Korean natural language processing.'
__description__ = """Korean, the 13th most widely spoken language in the world, is a beautiful, yet complex language. Myriad Korean NLP engines were built by numerous researchers, to computationally extract meaningful features from the labyrinthine text.

KoNLPy is not just to create another, but to unify and build upon their shoulders, and see one step further. It is built particularly in the Python (programming) language, not only because of its its simplicity and elegance, but its powerful string processing modules and applicability to various tasks - including crawling, Web programming, and data analysis."""
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2018 {}'.format(__author__)
