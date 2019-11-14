
first:
	sudo apt-get update && sudo apt-get install -y software-properties-common python-software-properties
	sudo add-apt-repository ppa:nextgis/ppa


second:
	sudo apt-get update && sudo apt-get install -y \
	wget unzip \
	gdal-bin libgdal-dev libgdal20 libudunits2-0 \
	python3 python3-gdal python3-setuptools python3-dev python3-numpy python3-netcdf4

third:
	pip3 install gdal

numpy:
	sudo apt remove python3-numpy
	sudo -H pip3 install numpy
