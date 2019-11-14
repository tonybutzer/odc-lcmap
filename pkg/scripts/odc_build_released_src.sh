#! /bin/bash -x

cd /opt
# git clone https://github.com/opendatacube/datacube-core.git

mkdir EasterBilby
cd EasterBilby
wget https://github.com/opendatacube/datacube-core/archive/datacube-1.6rc1.tar.gz
tar xvfz datacube-1.6rc1.tar.gz
cd datacube-core-datacube-1.6rc1/
sudo pip3 install -e .
# sudo pip3 install -U .

