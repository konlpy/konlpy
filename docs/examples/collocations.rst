Finding collocations
====================

We can find collocations with the help of `NLTK <http://nltk.org>`_.

In order to find trigram collocations, replace `BigramAssocMeasures` with `TrigramAssocMeasures`, and `BigramCollocationFinder` with `TrigramCollocationFinder`.

.. literalinclude:: collocations.py
    :language: python

- Console::

    Collocations among tagged words:
    [((가부, NNG), (동수, NNG)),
     ((강제, NNG), (노역, NNG)),
     ((경자, NNG), (유전, NNG)),
     ((고, ECS), (채취, NNG)),
     ((공무, NNG), (담임, NNG)),
     ((공중, NNG), (도덕, NNG)),
     ((과반, NNG), (수가, NNG)),
     ((교전, NNG), (상태, NNG)),
     ((그러, VV), (나, ECE)),
     ((기본적, NNG), (인권, NNG))]
    
    Collocations among words:
    [(현행, 범인),
     (형의, 선고),
     (내부, 규율),
     (정치적, 중립성),
     (누구, 든지),
     (회계, 연도),
     (지체, 없이),
     (평화적, 통일),
     (형사, 피고인),
     (지방, 자치)]
    
    Collocations among tags:
    [(XR, XSA),
     (JKC, VCN),
     (VCN, ECD),
     (ECD, VX),
     (ECD, VXV)]
