FROM centos:{{ docker_image_version | default('latest') }} AS install_phase

RUN yum update -y
RUN yum install --assumeyes gcc-c++ python3 python3-devel python3-pip java-1.8.0-openjdk-devel make diffutils
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install {{ konlpy_package_definition | default('konlpy') }}

RUN yum install --assumeyes curl git
RUN curl -s https://raw.githubusercontent.com/{{ github_repo_mecab | default('konlpy/konlpy') }}/{{ github_branch_mecab | default('master') }}/scripts/mecab.sh | bash

ENTRYPOINT python3

# XXX: Stop Here with `docker build --target install_phase ...`
FROM install_phase AS test_phase

RUN yum install --assumeyes git
RUN git clone https://github.com/{{ github_repo_konlpy | default('konlpy/konlpy') }} konlpy.git
WORKDIR konlpy.git
RUN git checkout {{ github_branch_konlpy | default('master') }}
RUN python3 -m pip install -r requirements-dev.txt
CMD -m pytest -v .
