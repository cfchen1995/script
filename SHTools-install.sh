#!/bin/sh
# shtools安装，该包依赖于fftw3, blas, lapack
# 另一方面，lapack依赖blas，因此在编译lapack前需要提供blas包，所幸lapack里已经集成了blas包，但默认并不编译它。要想编译lapack前先编译blas，需要修改一下Makefile。将第11行并将内容改为：
# lib: blaslib lapacklib tmglib
#
# 该脚本文件依次安装fftw3, blas, lapack.
# 
# 05/01/2017 西南交通大学

# SHTOOLS
# http://www.ipgp.fr/~wieczor/SHTOOLS2.8.tar.Z

# 源码下载
wget http://www.fftw.org/fftw-3.3.3.tar.gz
wget http://www.netlib.org/blas/blas.tgz
wget http://www.netlib.org/lapack/lapack.tgz		# 依据官网修改选择相应的最新包下载，不写明版本号可以下载最新包lapack-3.7.0.tgz
git clone git@github.com:SHTOOLS/SHTOOLS.git

# 检查下列依赖问题
sudo apt-get install libblas-dev liblapack-dev g++ gfortran libfftw3-dev tcsh
sudo apt-get install python-pip		# 安装pip

# fftw编译安装
tar -xzf fftw*.tar.gz
cd fftw*
make
# make check		# 可进行相应的测试
sudo make install

# blas编译安装
cd ..
tar -xzf blas.tgz
cd BLAS*
make
cp blas_LINUX.a libblas.a		# 重命名
# mv blas_LINUX.a libblas.a
sudo cp libblas.a /usr/local/lib

# lapack编译安装
cd ..
tar -zxvf lapack*.tgz
# make之前，需要先创建一个make.inc文件，对于Linux系统，可以直接根据make.inc.example创建：
cd lapack*
cp make.inc.example make.inc
# 进行make的时候，若存在如下问题，可能是blas库名称问题。
# gfortran  -o ../xblat1s sblat1.o ../../librefblas.a
# gfortran: error: ../../librefblas.a: No such file or directory
# 若仅将第11行注释，第12行注释打开，就会出现如下问题：
# Makefile:39: recipe for target 'variants' failed。
# 删除variants
# Makefile:469: recipe for target 'znep.out' failed
# 这个情况下，函数库liblapack.a、librefblas.a和libtmglib.a是生成。
# lapack编译完成后，目录下将生成liblapack.a、librefblas.a和libtmglib.a三个文件
make		# 编译所有的lapack文件  
cd lapacke	# 进入lapacke 文件夹，这个文件夹包含lapack的C语言接口文件
# cd LAPACKE
make		# 编译lapacke  
sudo cp include/*.h /usr/local/include	# 将lapacke的头文件复制到系统头文件目录  
cd ..									# 返回到lapack目录  
sudo cp *.a /usr/local/lib				# 将生成的所有库文件复制到系统库目录
# 通过官网的例子可以正常输出结果
# gfortran lapack_test.c  -llapacke -llapack -lrefblas

# SHTools编译安装
cd ../SHTOOLS
pip install pyshtools
# Or, to install a developer version, download or clone the SHTOOLS repository, enter the SHTOOLS folder and then execute one of the following commands:
pip install .  # installs into the active python environment lib folder
sudo pip install -v -e .  # installs into the SHTOOLS/pyshtools folder and links to the active python environment
make fortran
# gfortran -I/home/changfu/SHTOOLS/modules -fopenmp -m64 -fPIC -O3 -ffast-math -L/home/changfu/SHTOOLS/lib -lSHTOOLS-mp -L/usr/local/lib -lfftw3 -lm -llapack -lblas
make fortran-mp		# # Open-MP Fortran routines
# gfortran -I/home/changfu/SHTOOLS/modules -m64 -fPIC -O3 -ffast-math -L/home/changfu/SHTOOLS/lib -lSHTOOLS -L/usr/local/lib -lfftw3 -lm -llapack -lblas

make
# gfortran -I/modules -m64 -fPIC -O3 -ffast-math -L/lib -lSHTOOLS -L/usr/local/lib -lfftw3 -lm -llapack -lblas
