# -q -y options in apt-get install will assume “yes” to everything (and do it quietly). v.g. sudo apt-get -q -y install <package_name> 

sudo apt-get update

sudo apt-get install tcsh
sudo apt-get install gfortran

sudo apt-get install xaw3dg-dev
sudo apt-get install xaw3dg
sudo apt-get install libxt6
sudo apt-get install libxt-dev
sudo apt-get install x11-common
sudo apt-get install libxau-dev
sudo apt-get install libxau6
sudo apt-get install libxaw7
sudo apt-get install libxaw7-dev
sudo apt-get install libx11-6
sudo apt-get install libx11-dev
sudo apt-get install x11-utils
sudo apt-get install libx11-data
sudo apt-get install libncurses5-dev
sudo apt-get install ncurses-term
sudo apt-get install libncurses5
sudo apt-get install libncursesw5
sudo apt-get install libncursesw5-dev
sudo apt-get install ncurses-base
sudo apt-get install build-essential
sudo apt-get install python-scipy
sudo apt-get install python-pyfits
sudo apt-get install python-pip

#install kapteyin following the instructions at
#http://www.astro.rug.nl/software/kapteyn/intro.html
cd ~
mkdir kapteyn
cd kapteyn
wget http://www.astro.rug.nl/software/kapteyn/kapteyn-2.3.tar.gz
tar -xzf kapteyn*.tar.gz
cd kapteyn*
sudo python setup.py install


cd ~
wget ftp://ftp.astro.rug.nl/gipsy/gipsy_install.csh
chmod +x gipsy_install.csh
mkdir gipsy
./gipsy_install.csh
#you have to provide the gipsy installation folder e.g. /home/ubunyu/gipsy

#graphic libraries are not resolved

#According to installation guide lines: http://www.astro.rug.nl/~gipsy/installation/installation.html
#Se up the environment:
#vim ~/.cshrc
#insert:
#setenv gip_root <PATH_TO_GIPSY_ROOT_DIRECTORY>
#source $gip_root/sys/gipenv.csh

#use tcsh to run gipsy


