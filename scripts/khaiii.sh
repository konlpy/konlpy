#! /bin/bash

set -e

os=$(uname)
if [[ ! $os == "Linux" ]] && [[ ! $os == "Darwin" ]]; then
    echo "This script does not support this OS."
    echo "FIXME"
    exit 0
fi

if ! hash "gcc" &>/dev/null && ! hash "clang" &>/dev/null; then 
    echo "Khaiii requires a C++ compiler."
    echo "Refer to the following link."
    echo https://github.com/kakao/khaiii/wiki/%EB%B9%8C%EB%93%9C-%EB%B0%8F-%EC%84%A4%EC%B9%98
    exit 0
fi

install_cmake(){
    pip install cmake
}

install_khaiii(){
    pushd /tmp
    curl -LO https://github.com/kakao/khaiii/archive/v0.4.tar.gz
    tar xzvf v0.4.tar.gz
    pushd khaiii-0.4
    mkdir -p build
    pushd build

    INSTALL_PATH=~/konlpy_data
    if [[ -r /usr/share/konlpy_data ]]; then
        INSTALL_PATH=/usr/share/konlpy_data
    elif [[ -w /usr/share ]]; then
        mkdir -p /usr/share/konlpy_data
        INSTALL_PATH=/usr/share/konlpy_data
    elif [[ -r /usr/local/share/konlpy_data ]]; then
        INSTALL_PATH=/usr/local/share/konlpy_data
    elif [[ -w /usr/local/share ]]; then
        mkdir -p /usr/local/share/konlpy_data
        INSTALL_PATH=/usr/local/share/konlpy_data
    elif [[ -r /usr/lib/konlpy_data  ]]; then
        INSTALL_PATH=/usr/lib/konlpy_data
    elif [[ -w /usr/lib ]]; then
        mkdir -p /usr/lib/konlpy_data
        INSTALL_PATH=/usr/lib/konlpy_data
    elif [[ -r /usr/local/lib/konlpy_data  ]]; then
        INSTALL_PATH=/usr/local/lib/konlpy_data
    elif [[ -w /usr/local/lib ]]; then
        mkdir -p /usr/local/lib/konlpy_data
        INSTALL_PATH=/usr/local/lib/konlpy_data
    fi
    cmake -DCMAKE_INSTALL_PREFIX=$INSTALL_PATH ..
    make all
    make large_resource
    make install
    make package_python
    pushd package_python
    pip install .
    popd
    popd
    popd
    popd
}

install_cmake
install_khaiii
