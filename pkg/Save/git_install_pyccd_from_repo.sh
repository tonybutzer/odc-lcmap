#! /bin/bash

cd /opt
git clone https://github.com/USGS-EROS/lcmap-pyccd.git

cd lcmap-pyccd

pip3 install -e .
