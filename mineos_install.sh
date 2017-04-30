#!/bin/sh
# 源码安装mineos软件，进行软件的编译安装
#
# 04/30/2017 西南交通大学
#

git clone --recursive https://github.com/geodynamics/mineos.git
git checkout --recursive https://github.com/geodynamics/mineos
cd mineos
autoreconf -i
./configure --prefix=$HOME/cig
make
make install

