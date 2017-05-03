#!/bin/sh

# SHTools安装，该包依赖于fftw3, blas, lapack
# 
# 05/01/2017 西南交通大学
# 最初自己将两种安装方法交叉使用，出现了使用方面的问题。
# 说明：
# 其依赖的函数库libblas-dev liblapack-dev libfftw3-dev在Ubuntu软件源已有。
# Python的使用应当要调用matplotlib, numpy和pySHTools。

# 利用make进行编译的时候，总是出现Fortran和Python2可以正常编译，同时Python2和Python3依赖于Fortran的正确安装，就是总出现如下的错误：
# In file included from /tmp/tmpu0oah8f_/src.linux-x86_64-3.5/fortranobject.c:2:0:
# /tmp/tmpu0oah8f_/src.linux-x86_64-3.5/fortranobject.h:7:20: fatal error: Python.h: No such file or directory
# ...
# 问题主要来源于f2py3的运行问题。
# 通过不断查阅相关资源，发现这些错误说明系统中的Python3没有正确安装，因此重新安装Python3，可以实现正确安装。
# 运行make可以正常通过，说明该程序的编译实现需要Python2, Python3, fftw3, blas, lapack的正确安装，利用源码编译时确保配置正确设置，初步推荐使用apt-get进行安装。

# ./configure是生成Makefile文件
# make命令主要是在build目录下生成library
# 利用make check或是make test来测试正确相应的二进制文件
# 安装到系统需要使用make install命令

# 编译测试
# 参考：https://SHTools.oca.eu/SHTools/www/install.html
# sudo make
# or
sudo make fortran fortran-mp python2 python3
# To compile and run the Fortran 95 and Python test suites, use
sudo make fortran-tests
sudo make python2-tests
sudo make python3-tests
# 以上测试运行可以正常通过
sudo make clean
sudo make install
# To get started, import the standard matplotlib library for graphics, numpy for mathematical extensions to Python, and pySHTools:
# 编译测试
gfortran -m64 -fPIC -O3 TestCilmPlus.f95 -I/usr/local/include/ -L/usr/local/lib -lSHTools -lfftw3 -lm -llapack -lblas -o TestCilmPlus		# 来源SHTools的测试例子
# 加深对相关包的理解和测试使用，，主要是相关函数的调用方法的实现



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #########################################################################################
# +++++++++++++++++++++++自动安装++++++++++++++++++++++++++++++
# #########################################################################################
# 
sudo apt-get install libblas-dev liblapack-dev g++ gfortran libfftw3-dev tcsh
# Python Library
pip install pySHTools
# Fortran Library - 用于生成Fortran library，但是并没有安装SHTools
make fortran
sudo make fortran-mp  # Open-MP Fortran routines
# 以上这种安装方法可能会使Python包缺少，不能正确安装。可以通过使用example中的算例进行测试，缺少相应的包就去安装相应的包。
sudo pip install matplotlib
# 源码安装容易出现依赖包fftw3, blas, lapack等不能正确安装，主要是相关参量的设置。
# 运行make还是会出问题。
# SHTools can be installed in several ways. If you will be using only the Python components, it is recommended to use the pip package manager. If you will be writing and compiling Fortran 95 code, it is recommended to use either the Brew package manager (on OSX), or to compile using the Makefile.

# #########################################################################################
# +++++++++++++++++++++++源码安装++++++++++++++++++++++++++++++
# #########################################################################################
# SHTools - 为加深对相关包的理解程度
# http://www.ipgp.fr/~wieczor/SHTools2.8.tar.Z

# 源码安装，lapack依赖blas，因此在编译lapack前需要提供blas包，所幸lapack里已经集成了blas包，但默认并不编译它。要想编译lapack前先编译blas，需要修改一下Makefile。将第11行并将内容改为：
# lib: blaslib lapacklib tmglib
#
# 该脚本文件依次安装fftw3, blas, lapack.

# 源码下载
wget http://www.fftw.org/fftw-3.3.3.tar.gz
wget http://www.netlib.org/blas/blas.tgz
wget http://www.netlib.org/lapack/lapack.tgz		# 依据官网修改选择相应的最新包下载，不写明版本号可以下载最新包lapack-3.7.0.tgz
git clone git@github.com:SHTools/SHTools.git

# 检查下列依赖问题
# sudo apt-get install libblas-dev liblapack-dev g++ gfortran libfftw3-dev tcsh
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
cd ../SHTools
pip install pySHTools
# Or, to install a developer version, download or clone the SHTools repository, enter the SHTools folder and then execute one of the following commands:
pip install .  # installs into the active python environment lib folder
sudo pip install -v -e .  # installs into the SHTools/pySHTools folder and links to the active python environment
make fortran
# gfortran -I/home/changfu/SHTools/modules -fopenmp -m64 -fPIC -O3 -ffast-math -L/home/changfu/SHTools/lib -lSHTools-mp -L/usr/local/lib -lfftw3 -lm -llapack -lblas
make fortran-mp		# # Open-MP Fortran routines
# gfortran -I/home/changfu/SHTools/modules -m64 -fPIC -O3 -ffast-math -L/home/changfu/SHTools/lib -lSHTools -L/usr/local/lib -lfftw3 -lm -llapack -lblas

make
# gfortran -I/modules -m64 -fPIC -O3 -ffast-math -L/lib -lSHTools -L/usr/local/lib -lfftw3 -lm -llapack -lblas
