#!/bin/bash
INSTALL_LIB=${PWD}/lib/systemc-2.3.3

## build systemc-2.3.3
cd systemc-2.3.3
mkdir -p build && cd build

../configure --prefix=${INSTALL_LIB} CXXFLAGS="-std=c++14"

make -j8
make install