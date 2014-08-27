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
git clone https://github.com/HiroyukiHaga/mecab-python.git
cd mecab-python
python setup.py build
sudo python setup.py install
