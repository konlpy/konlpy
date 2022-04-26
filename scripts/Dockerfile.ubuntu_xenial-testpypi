FROM ubuntu:xenial

RUN apt-get update

RUN apt-get install -y g++ openjdk-8-jdk python3-dev python3-pip
RUN python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ konlpy==0.5.2-rc.2

RUN apt-get install -y curl git
RUN curl -s https://raw.githubusercontent.com/minhoryang/konlpy/issues/271/scripts/mecab.sh | bash

RUN apt-get install -y git
RUN git clone https://github.com/konlpy/konlpy konlpy.git
WORKDIR konlpy.git
RUN git checkout master
RUN python3 -m pip install -r requirements-dev.txt
CMD python3 -m pytest -v .