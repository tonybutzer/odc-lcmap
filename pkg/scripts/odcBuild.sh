
# THIS WAS modeled after the Docker file from here alexgleith/docker-opendatacube
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal


# First add the NextGIS repo
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
   software-properties-common python-software-properties make
sudo add-apt-repository ppa:nextgis/ppa
sudo rm -rf /var/lib/apt/lists/*


# And now install apt dependencies, including a few of the heavy Python projects
sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    wget unzip \
    gdal-bin libgdal-dev libgdal20 libudunits2-0 \
    python3 python3-gdal python3-setuptools python3-dev python3-numpy python3-netcdf4
sudo apt-get install -y python3-pip
sudo rm -rf /var/lib/apt/lists/*


# Install the dependencies
# Install psychopg2 as a special case, to quiet the warning message 
sudo pip3 install --no-cache --no-binary :all: psycopg2
./gdalInstall.sh


# Get the code, and put it in /opt
cd /opt
sudo wget "https://github.com/opendatacube/datacube-core/archive/develop.zip" -O /tmp/odc.zip
sudo unzip /tmp/odc.zip
sudo mv /opt/datacube-core-develop /opt/opendatacube


# ENV LC_ALL C.UTF-8

cd /opt/opendatacube
sudo pip3 install '.[test,analytics,celery,s3]' --upgrade
# don't need to test fail drivers - i have enuf errors - tony
# I don't understand the relation between fail_drivers and s3aio_index
sudo pip3 install ./tests/drivers/fail_drivers --no-deps --upgrade

sudo python3 setup.py develop

datacube --help
datacube --help
datacube --help

sudo pip3 install awscli
sudo pip3 install folium
sudo pip3 install scikit-image


sudo chown ubuntu:ubuntu -R /opt
