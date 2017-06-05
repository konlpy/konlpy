#! /bin/bash
#
# Copyright 2014 Lucy Park
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


os=$(uname)
if [ $os == "Linux" ]; then
    echo "Installing MeCab-ko"
elif [ $os == "Darwin" ]; then
    echo "Installing MeCab-ko"
else
    echo "This script does not support this OS."
    echo "Try consulting https://github.com/konlpy/konlpy/blob/master/scripts/mecab.sh"
    exit 0
fi

# install mecab-ko
cd /tmp
curl -LO https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.1.tar.gz
tar zxfv mecab-0.996-ko-0.9.1.tar.gz
cd mecab-0.996-ko-0.9.1
./configure
make
make check
sudo make install

# install mecab-ko-dic
## install requirement automake1.11
# TODO: if not [automake --version]
cd /tmp
curl -LO http://ftpmirror.gnu.org/automake/automake-1.11.tar.gz
tar -zxvf automake-*.tar.gz
cd automake-*
./configure
make
sudo make install

cd /tmp
curl -LO https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.0.1-20150920.tar.gz
tar -zxvf mecab-ko-dic-2.0.1-*.tar.gz
cd mecab-ko-dic-2.0.1-*
./autogen.sh
./configure
make
sudo sh -c 'echo "dicdir=/usr/local/lib/mecab/dic/mecab-ko-dic" > /usr/local/etc/mecabrc'
sudo make install

# install mecab-python
cd /tmp
git clone https://bitbucket.org/eunjeon/mecab-python-0.996.git
cd mecab-python-0.996

python setup.py build
python setup.py install

if hash "python3" &>/dev/null
then
    python3 setup.py build
    python3 setup.py install
fi
