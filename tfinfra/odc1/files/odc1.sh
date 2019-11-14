#! /bin/bash

# sudo apt-get upadte

echo "Hello Tony" > /tmp/hellotony.txt

# sudo hostname espa1
sudo mkdir -p /opt

(cd /opt; git clone http://github.com/tonybutzer/odc-lcmap)

sudo mkdir -p /data; sudo chown ubuntu /data

sudo chown -R ubuntu /opt

(cd /opt/odc-lcmap/pkg; ./setup_os.sh)
