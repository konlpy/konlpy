#! /bin/bash
#
# Copyright 2019 Team KoNLPy
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

# Set mecab related variable(s)
mecab_dicdir="/usr/local/lib/mecab/dic/mecab-ko-dic"

# Exit as soon as we fail
set -e

# Determine OS
os=$(uname)
if [[ ! $os == "Linux" ]] && [[ ! $os == "Darwin" ]]; then
    echo "This script does not support this OS."
    echo "Try consulting https://github.com/konlpy/konlpy/blob/master/scripts/mecab.sh"
    exit 0
fi

# Determine sudo
if hash "sudo" &>/dev/null; then
    sudo="sudo"
else
    sudo=""
fi

install_mecab_ko(){
    cd /tmp
    curl -LO https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
    tar zxfv mecab-0.996-ko-0.9.2.tar.gz
    cd mecab-0.996-ko-0.9.2
    ./configure
    make
    make check
    $sudo make install
}

install_automake(){
    ## install requirement automake1.11
    # TODO: if not [automake --version]
    if [ "$os" == "Linux" ]; then
        if [ "$(grep -Ei 'debian|buntu|mint' /etc/*release)" ]; then
            $sudo apt-get update && $sudo apt-get install -y automake
        elif [ "$(grep -Ei 'fedora|redhat' /etc/*release)" ]; then
            $sudo yum install -y automake
        else
            ##
            # Autoconf
            #
            # stage directory
            builddir=`mktemp -d` && cd $builddir

            # download and extract source
            curl -LO http://ftpmirror.gnu.org/autoconf/autoconf-latest.tar.gz
            tar -zxvf autoconf-*

            # configure, make, install --prefix=/usr/local
            cd autoconf*
            ./configure
            make
            $sudo make install

            # erase stage dir
            rm -rf $builddir


            ##
            # Automake
            #
            # stage directory
            builddir=`mktemp -d` && cd $builddir

            # download and extract source
            curl -LO http://ftpmirror.gnu.org/automake/automake-1.11.tar.gz
            tar -zxvf automake-1.11.tar.gz

            # configure, make, install --prefix=/usr/local
            cd automake-1.11
            ./configure
            make
            $sudo make install

            # erase stage dir
            rm -rf $builddir
        fi

    elif [ "$os" == "Darwin" ]; then
        brew install automake
    fi
}

install_mecab_ko_dic(){
    echo "Install mecab-ko-dic"
    cd /tmp
    curl -LO https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
    tar -zxvf mecab-ko-dic-2.1.1-20180720.tar.gz
    cd mecab-ko-dic-2.1.1-20180720
    ./autogen.sh
    ./configure
    make
    $sudo sh -c 'echo "dicdir=/usr/local/lib/mecab/dic/mecab-ko-dic" > /usr/local/etc/mecabrc'
    $sudo make install
}

install_mecab_python(){
    pushd /tmp
    if [[ ! -d "mecab-python-0.996" ]]; then
        git clone https://bitbucket.org/eunjeon/mecab-python-0.996.git
    fi
    popd
    pip install /tmp/mecab-python-0.996
}


if ! hash "automake" &>/dev/null; then
    echo "Installing automake (A dependency for mecab-ko)"
    install_automake
fi

if hash "mecab" &>/dev/null; then
    echo "mecab-ko is already installed"
else
    echo "Install mecab-ko-dic"
    install_mecab_ko
fi

if [[ -d $mecab_dicdir ]]; then
    echo "mecab-ko-dic is already installed"
else
    echo "Install mecab-ko-dic"
    install_mecab_ko_dic
fi

if [[ $(python -c 'import pkgutil; print(1 if pkgutil.find_loader("MeCab") else 0)') == "1" ]]; then
    echo "mecab-python is already installed"
else
    echo "Install mecab-python"
    install_mecab_python
fi

echo "Done."
