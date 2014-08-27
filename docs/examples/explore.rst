Exploring a document
====================

Exploring a document can consist of various components:

- Counts (characters, words, etc.)
- Checking Zipf's laws: :math:`fr=k`
- Concordances

.. literalinclude:: explore.py
    :language: python

- Console::

    nchars  : 19240
    ntokens : 4178
    nmorphs : 1501

    Top 20 frequent morphemes:
    [((의, J), 398),
     ((., S), 340),
     ((하, X), 297),
     ((에, J), 283),
     ((ㄴ다, E), 242),
     ((ㄴ, E), 226),
     ((이, J), 218),
     ((을, J), 211),
     ((은, J), 184),
     ((어, E), 177),
     ((를, J), 148),
     ((ㄹ, E), 135),
     ((/, S), 131),
     ((하, P), 124),
     ((는, J), 117),
     ((법률, N), 115),
     ((,, S), 100),
     ((는, E), 97),
     ((있, P), 96),
     ((되, X), 95)]

    Locations of "대한민국" in the document:
    0 대한민국헌법 유구한 역사와
    9 대한국민은 3·1운동으로 건립된 대한민국임시정부의 법통과 불의에
    98 총강 제1조 ① 대한민국은 민주공화국이다. ②대한민국의
    100 ① 대한민국은 민주공화국이다. ②대한민국의 주권은 국민에게
    110 나온다. 제2조 ① 대한민국의 국민이 되는
    126 의무를 진다. 제3조 대한민국의 영토는 한반도와
    133 부속도서로 한다. 제4조 대한민국은 통일을 지향하며,
    147 추진한다. 제5조 ① 대한민국은 국제평화의 유지에
    787 군무원이 아닌 국민은 대한민국의 영역안에서는 중대한
    1836 파견 또는 외국군대의 대한민국 영역안에서의 주류에
    3620 경제 제119조 ① 대한민국의 경제질서는 개인과

- zipf.png:
    .. image:: zipf.png
        :width: 100%
