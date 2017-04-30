git clone --recursive https://github.com/geodynamics/mineos.git
git checkout --recursive https://github.com/geodynamics/mineos
cd mineos
autoreconf -i
./configure --prefix=$HOME/cig
make
make install
