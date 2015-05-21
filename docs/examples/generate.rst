Generating random text
======================

Say you want to generate random text in Korean.
How would you do it?

The easiest way would probably be to have your cat walk across your keyboard
which would result in something like this [#]_::

    ㅕ키ㅔ츄ㅑㅋ응아 ㅝㄴㅇ 쿄ㅛㅍㄹㅎ튜허ㅓㅎㅠㅅㄴ마

However a sequence of random letters like this does not make any sense.
Normally, Korean text is formed with a sequence of words, formed by a sequence of syllables, which are each formed with two to three types of the keyboard, each uniquely called choseong, jungseong, jongseong [#]_.
(though in casual chatting, just one type of the keyboard is common as well, ex: "ㅋㅋㅋ")
So now we educate our cat to type syllables::

    로켘불됴약 니앙굷 췡바이꿻노기

Then we notice that in Korean, the syllable '이' is more frequently used than '앙' and definitely much more than '꿻' or '굷'.
If our cat knew that, he would have typed something like this::

    다이는가 고다하에지 요그이데습

But then, this still doesn't make any sense because the syllables don't form words.
Rather than generating each syllable independently, we can generate a syllable base on its precedent so that after '하' follows '다', and after '그' we get '리' and '고'.
In mathematical terms, this process is better known as a `Markov chain <http://en.wikipedia.org/wiki/Markov_chain>`_::
    
    국의의하되고인정부가는 요구한 대통령은 2조 사면 기밀과 헌법률로 위하의 위하며

Our "sentence" above was generated with "bigrams", or "2-grams".
If we wish to make more sense out of it, we could try "3-grams" (better known as trigrams) or "4-grams".
Or, we could extend the same idea to longer sequences of letters, such as morphemes.
Let's try this with actual code.


.. warning::

    The code below works with Python3, and not with Python2! You can run the code by typing `python3 generate.py` on your terminal.

.. literalinclude:: generate.py
    :language: python

- Console::

    0. 국민 은 법률 로 인한 배상 은 특별 한 영장 을 청구 할 수 있 어서 최고 득표자 가 제출 한 유일 한 때 에 의하 여 는 경우 를 선거 관리 할 수 없 을 포함 한 사항 은 청구 할 수 있 다
    1. 국민 투표 의 범죄 에 의하 여 발언 하 지 아니한 회의 는 요건 은 1988 년 으로 대통령 이 의결 한다
    2. 국민 경제 자문 기구 를 타파 하 기 위하 여 긴급 한 형태 로 정한다
    3. 국민 은 이 정하 는 헌법 시행 당시 의 심사 할 수 있 다
    4. 국민 의 기본 질서 를 진다

Well, that's a lot better than the random string typed by our cat!
The sentences look a bit ugly because there are whitespaces between all morphemes, whereas in actual Korean text, they would be stuck together.
Also note that this text generation model was built from a single document.
If you were to build a model with a much larger corpus, you wouldn't even have to do morpheme analysis because you would have enough data for any potential `initstr`.
Other than that, there are much more ways to improve this model!
Feel free to experiment.

For more on generating text, you can refer to Jon Bently's `Programming Pearls (Section 15.3) <http://www.cs.bell-labs.com/cm/cs/pearls/sec153.html>`_.

Furthermore, if you use `language models <http://en.wikipedia.org/wiki/Language_model>`_, you can evaluate your random texts and figure out whether they actually make sense in a statistical point of view.


.. [#] This story would actually feature a monkey instead of a cat. Namely by the `Infinite monkey theorem <http://en.wikipedia.org/wiki/Infinite_monkey_theorem>`_.
.. [#] Please refer to the Hangul Jamo in `Unicode character code charts <http://www.unicode.org/charts/>`_.
