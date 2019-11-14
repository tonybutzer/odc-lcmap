
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
# sudo pip3 install psycopg2-binary
sudo pip3 install boto3
sudo pip3 install scikit-image
sudo pip3 install folium
./gdalInstall.sh

# gdal hell
gdal-config --datadir

sudo updatedb

sudo locate gcs.csv

# !sudo rmdir /usr/share/gdal/2.3
sudo mkdir -p /usr/share/gdal
sudo rm /usr/share/gdal/2.3
# !sudo ln -s /usr/local/lib/python3.5/dist-packages/rasterio/gdal_data /usr/share/gdal/2.3

sudo ls -lR /usr/share/gdal/2.3

sudo ls -lR /usr/local/lib/python3.5/dist-packages/rasterio/gdal_data

sudo ln -s /usr/local/lib/python3.5/dist-packages/rasterio-1.0a12-py3.5-linux-x86_64.egg/rasterio/gdal_data /usr/share/gdal/2.3


sudo chown ubuntu:ubuntu -R /opt
