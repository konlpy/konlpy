#! /bin/bash

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
