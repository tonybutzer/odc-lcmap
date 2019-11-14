all: cube pyccd noteLib util config testdatacube
python:
	sudo apt-get -y install python3-dev
	sudo apt-get -y install gfortran
	sudo apt-get -y install libopenblas-dev
	sudo apt-get -y install liblapack-dev
	sudo apt-get -y install graphviz
	sudo apt-get -y install python3-pip

URL='https://github.com/USGS-EROS/lcmap-pyccd.git'
FOLDER='/opt/lcmap-pyccd'

pyccd: python
	(cd /opt && if [ ! -d ${FOLDER} ]; then git clone ${URL}; fi)
	(cd /opt/lcmap-pyccd && pip3 install -e .)

noteLib:
	sudo pip3 install jupyter
	sudo pip3 install scikit-image
	sudo pip3 install matplotlib
	sudo pip3 install pyproj
	sudo pip3 install plotly
	(cd /opt/odc-lcmap/noteLib && pip3 install -e .)

db:
	./scripts/createDatabase.sh 

testdatacube:
	# sudo -H pip3 uninstall psycopg2-binary
	sudo -H pip3 uninstall psycopg2
	sudo -H pip3 install --no-binary psycopg2 psycopg2
	 (cd /opt/build/datacube-core-datacube-1.6rc1 \
	 && sudo pip3 install '.[test,analytics,celery,s3]' --upgrade)
	sudo -H pip3 install --no-binary psycopg2 psycopg2
	datacube system init
	python3 /opt/odc-lcmap/test/test_datacube_basic.py
buildcube: 
	# (cd /opt/build/datacube-core-datacube-1.6rc1 \
	# && sudo pip3 install -e  .)
	 (cd /opt/build/datacube-core-datacube-1.6rc1 \
	 && sudo pip3 install '.[test,analytics,celery,s3]' --upgrade)
	sudo -H pip3 install --no-binary psycopg2 psycopg2
	 # && sudo pip3 install ./tests/drivers/fail_drivers --no-deps --upgrade\
	 # && export LC_ALL=C.UTF-8 && sudo python3 setup.py develop)


cubestarter: first second
	sudo apt-get -y install python3-pip
	# sudo -H pip3 uninstall psycopg2-binary
	# sudo -H pip3 uninstall psycopg2
	# sudo -H pip3 install --no-binary psycopg2 psycopg2

	 # sudo -H pip3 install jsonschema
	 # (cd /opt/build/datacube-core-datacube-1.6rc1 && sudo python3 setup.py install)

getcube:
	mkdir -p /opt/build # EasterBilby here 
	(cd /opt/build && wget https://github.com/opendatacube/datacube-core/archive/datacube-1.6rc1.zip)
	(cd /opt/build && unzip datacube-1.6rc1.zip)

cube: cubestarter gdal getcube buildcube db
	echo "Download and build datacube - this is sort of painful!"
	echo "Lots of warnings - hope that's ok"
	echo "The build takes quite a while"

util:
	sudo pip3 install awscli # is it better to use sudo apt-get install awscli
	sudo apt-get -y install unzip

gdal:
	# sudo add-apt-repository -y ppa:ubuntugis/ppa
	sudo add-apt-repository ppa:nextgis/ppa
	sudo apt-get update && sudo apt-get install -y gdal-bin libgdal-dev libgdal20 libudunits2-0 \
	libudunits2-dev \
	python3 python3-gdal python3-setuptools python3-dev python3-numpy python3-netcdf4
	sudo apt-get -y install python3-pip
	pip3 install gdal



config: 
	cp ./files/datacube.conf ~/.datacube.conf


first:
	sudo apt-get update && sudo apt-get install -y software-properties-common 
	# sudo apt-get install -y python-software-properties

second:
	sudo apt-get update && sudo apt-get install -y wget unzip 

third:
	pip3 install gdal

numpy:
	sudo apt remove python3-numpy
	sudo -H pip3 install numpy

index:
	(cd /opt && git clone http://github.com/tonybutzer/index)
