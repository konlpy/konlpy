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
if [ $os == "Linux" ] then
    echo "Installing MeCab-ko"
elif [ $os == "Darwin" ] then
    wgetpath=`command -v wget`
    if [ ! -x wgetpath ] then
        echo "Installing wget"
        echo "You must install wget first."
        exit 0
    echo "Installing MeCab-ko"
else
    echo "This script does not support this OS."
    echo "Try consulting https://github.com/konlpy/konlpy/blob/master/scripts/mecab.sh"
    exit 0
fi


# install mecab-ko
cd /tmp
wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.1.tar.gz
tar zxfv mecab-0.996-ko-0.9.1.tar.gz
cd mecab-0.996-ko-0.9.1
./configure
make
make check
sudo make install

# install mecab-ko-dic
cd /tmp
wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-1.6.1-20140814.tar.gz
tar zxfv mecab-ko-dic-1.6.1-20140814.tar.gz
cd mecab-ko-dic-1.6.1-20140814
./configure
sudo ldconfig
make
sudo sh -c 'echo "dicdir=/usr/local/lib/mecab/dic/mecab-ko-dic" > /usr/local/etc/mecabrc'
sudo make install

# install mecab-python
cd /tmp
git clone https://bitbucket.org/eunjeon/mecab-python-0.996.git
cd mecab-python-0.996
python setup.py build
sudo python setup.py install
python3 setup.py build
sudo python3 setup.py install
