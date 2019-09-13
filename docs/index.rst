KoNLPy: Korean NLP in Python
============================

.. image:: https://travis-ci.org/konlpy/konlpy.svg?branch=master
    :alt: Build status
    :target: https://travis-ci.org/konlpy/konlpy
    :height: 18px

.. image:: https://readthedocs.org/projects/konlpy/badge/?version=latest
    :alt: Documentation Status
    :target: https://readthedocs.org/projects/konlpy/?badge=latest
    :height: 18px

KoNLPy (pronounced *"ko en el PIE"*) is a Python package for natural language processing (NLP) of the Korean language.
For installation directions, see :doc:`here <install>`.

For users new to NLP, go to :ref:`start`.
For step-by-step instructions, follow the :ref:`guide`.
For specific descriptions of each module, go see the :ref:`api` documents.

.. sourcecode:: python

    >>> from konlpy.tag import Kkma
    >>> from konlpy.utils import pprint
    >>> kkma = Kkma()
    >>> pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
    [네, 안녕하세요..,
     반갑습니다.]
    >>> pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
    [질문,
     건의,
     건의사항,
     사항,
     깃헙,
     이슈,
     트래커]
    >>> pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))
    [(오류, NNG),
     (보고, NNG),
     (는, JX),
     (실행, NNG),
     (환경, NNG),
     (,, SP),
     (에러, NNG),
     (메세지, NNG),
     (와, JKM),
     (함께, MAG),
     (설명, NNG),
     (을, JKO),
     (최대한, NNG),
     (상세히, MAG),
     (!, SF),
     (^^, EMO)]


Standing on the shoulders of giants
-----------------------------------

Korean, the `13th most widely spoken language in the world <http://www.koreatimes.co.kr/www/news/nation/2014/05/116_157214.html>`_, is a beautiful, yet complex language.
Myriad :ref:`engines` were built by numerous researchers, to computationally extract meaningful features from the labyrinthine text.

KoNLPy is not just to create another, but to unify and build upon their shoulders, and see one step further.
It is built particularly in the `Python (programming) language <http://python.org>`_, not only because of the language's simplicity and elegance, but also the powerful string processing modules and applicability to various tasks - including crawling, Web programming, and data analysis.

The three main philosophies of this project are:

- Keep it simple.
- Make it easy. For humans.
- :ref:`"Democracy on the web works." <contribute>`

Please `report <https://github.com/konlpy/konlpy/issues>`_ when you think any have gone stale.

License
-------

KoNLPy is Open Source Software, and is released under the license below:

- `GPL v3 or above <http://gnu.org/licenses/gpl.html>`_

You are welcome to use the code under the terms of the license, however please acknowledge its use with a citation.

- Eunjeong L. Park, Sungzoon Cho. "`KoNLPy: Korean natural language processing in Python <http://dmlab.snu.ac.kr/~lucypark/docs/2014-10-10-hclt.pdf>`_", Proceedings of the 26th Annual Conference on Human & Cognitive Language Technology, Chuncheon, Korea, Oct 2014.

Here is a BibTeX entry.::

    @inproceedings{park2014konlpy,
      title={KoNLPy: Korean natural language processing in Python},
      author={Park, Eunjeong L. and Cho, Sungzoon},
      booktitle={Proceedings of the 26th Annual Conference on Human & Cognitive Language Technology},
      address={Chuncheon, Korea},
      month={October},
      year={2014}
    }


.. _contribute:

Contribute
----------

KoNLPy isn't perfect,
but it will continuously evolve and you are invited to participate!

Found a bug?
Have a good idea for improving KoNLPy?
Visit the `KoNLPy GitHub page <https://github.com/konlpy/konlpy>`_
and `suggest an idea <https://github.com/konlpy/konlpy/issues>`_
or `make a pull request <https://github.com/konlpy/konlpy/pulls>`_.

You are also welcome to join
our `gitter <https://gitter.im/konlpy/konlpy>`_
and the `mailing list <https://groups.google.com/forum/#!forum/konlpy>`_.
Gitter is more focused on development discussions
while the mailing list is a better place to ask questions,
but nobody stops you from going the other way around.

Please note that
*asking questions through these channels is also a great contribution*,
because it gives the community feedback as well as ideas.
Don't hesitate to ask.

.. _start:

Getting started
---------------

.. toctree::
  :glob:
  :maxdepth: 2

  start

.. _guide:

User guide
----------

.. toctree::
  :glob:
  :maxdepth: 2

  install
  morph
  data
  examples
  test
  references

.. _api:

API
---

.. toctree::
  :glob:

  api/konlpy


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
* :doc:`changelog`
