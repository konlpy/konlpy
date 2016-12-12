CONTRIBUTING
============

KoNLPy는 오픈소스 프로젝트입니다.
누구든지 원하면 KoNLPy의 컨트리뷰터가 될 수 있습니다.


1. 토론하고 배우기
------------------

다음의 채널들을 통해 궁금한 점을 해소할 수 있습니다.

- 홈페이지: http://konlpy.org
- 이슈트래커: http://github.com/konlpy/konlpy/issues
- 메일링 리스트: `konlpy@googlegroups.com <http://groups.google.com/forum/#!forum/konlpy>`_
- 토론방: http://gitter.im/konlpy/konlpy


2. 궁금증 해결하기
------------------

1. KoNLPy를 사용하다가 막히는 부분이 있다면 먼저 `이슈가 제기되었는지 확인 <http://github.com/konlpy/konlpy/issues>`_ 해봅니다.
2. 같은 이슈가 이미 제기되었고,
    - 이슈가 해결되었다면(closed): 최신 릴리즈에서 문제가 해결되었을 가능성이 높습니다. 쓰레드에서 다른 분들이 어떻게 해결했는지 파악해보는 것도 좋은 방법입니다.
    - 이슈가 아직 해결되지 않았다면(open): 댓글로 문제 상황을 설명해주세요. 같은 상황을 겪고 있는 사람들이 많이 모일수록 문제는 빠르게 해결될 수 있습니다.
3. 같은 이슈가 아직 제기되지 않았다면, "New Issue" 버튼을 눌러 이슈를 새로 생성해주시면 됩니다. 이슈를 새로 생성하시는 경우에는 사용하는 OS나 패키지 버젼 등을 같이 적어주시면 문제를 빠르게 해결하는데 도움이 됩니다.


3. 이슈 제안/해결하기
---------------------

- `깃헙 이슈 <https://github.com/konlpy/konlpy/issues>`_ 에 코드를 개선할 수 있는 방법을 제안하거나, 제안된 이슈에 대해 토론/해결하실 수 있습니다.
- 코드를 작성할 때는 다음에 유의해주세요.
    1. 탭 대신 공백 4개 사용
    2. 문서에서 특별히 언급되지 않은 사항은 일단 코드의 다른 부분들을 참고해서 작성 (+ 다른 분들의 편의를 위해 이 문서를 업데이트 해주세요)
    3. 커밋 로그는 설명력 있게 작성
- 코드 작성을 완료한 후 코드가 모든 테스트를 통과하는지 확인해주세요.
    1. 자바 코드를 수정한 경우::

        # Install `Apache Ant <http://ant.apache.org/manual/install.html>`_
        make java

    1. 코드를 단 한 줄이라도 수정한 모든 경우::

        pip install -r requirements-dev.txt
        pip3 install -r requirements-dev.txt
        make build      # create tar.gz
        make check      # check code styles
        make testall    # run tests

- PR을 보내기 전 다음을 확인해주세요.
    1. PR을 보내면 해당 코드는 KoNLPy의 오픈소스 라이센스를 따름
    1. PR를 보낸 후 코드의 일부를 변경하도록 요청될 경우, ``git commit --amend`` 로 커밋을 수정


4. 문서 수정하기
----------------

- 오류 수정: 사소한 오타 등을 발견하여 수정을 요청하고 싶은 경우, 문서를 직접 수정하실 수 있습니다.
- 내용 추가: 그 외에도 내용이 잘 이해되지 않는 부분이 있다거나, 설명이 부족한 부분에도 내용을 추가하실 수 있습니다. 특히, KoNLPy는 예제가 풍부한 문서를 지향합니다. 문서에 추가하면 좋을 법한 예제가 있으면 공유해주세요.
- 번역: KoNLPy의 문서 영문과 한국어를 지원합니다. 표현이 어색하거나 번역이 덜 된 부분을 수정하실 수 있습니다.

> Note: 기왕이면 기여하신 부분에 대해 정확한 attribution을 할 수 있도록, 다음의 과정대로 문서를 설치하고 수정한 후, PR을 보내주시기 바랍니다. 만일 이 과정이 너무 어렵거나 번거롭고, attribution은 따로 받지 않아도 된다면, konlpy@googlegroups.com로 메일을 보내주셔도 됩니다.


Setup docs
''''''''''

1. Fork and clone KoNLPy::

    git clone git@github.com:[your_github_id]/konlpy.git

2. Include the following lines in your `~/.bashrc`::

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

3. Install dependencies::

    $ make init_i18n


Modify and push docs
''''''''''''''''''''

1. Modify a document file::

    $ cd docs             # Move to the `docs` folder
    $ vi some_file.rst    # Modify corresponding `*.rst` files

2. Build docs::

    $ make html

3. Extract translation phrases::

    $ make extract_i18n

4. Modify translations::

    $ cd locale/ko/LC_MESSAGES
    $ vi some_file.po

5. Update translations::

    $ make update_i18n

6. Commit and push your repository

7. Send a pull request


5. 테스트 추가하기
------------------

- 코드의 커버리지가 최대화될 수 있도록, 아직 커버되지 않은 테스트 케이스를 추가해주세요.
