FROM ubuntu:{{ docker_image_version | default('latest') }} AS install_phase

RUN apt-get update

RUN apt-get install -y g++ openjdk-8-jdk python3-dev python3-pip
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install {{ konlpy_package_definition | default('konlpy') }}

RUN apt-get install -y curl git
RUN curl -s https://raw.githubusercontent.com/{{ github_repo_mecab | default('konlpy/konlpy') }}/{{ github_branch_mecab | default('master') }}/scripts/mecab.sh | bash

# XXX: Stop Here with `docker build --target install_phase ...`
FROM install_phase AS test_phase

RUN apt-get install -y git
RUN git clone https://github.com/{{ github_repo_konlpy | default('konlpy/konlpy') }} konlpy.git
WORKDIR konlpy.git
RUN git checkout {{ github_branch_konlpy | default('master') }}
RUN python3 -m pip install -r requirements-dev.txt
CMD python3 -m pytest -v .