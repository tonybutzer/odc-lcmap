#! /bin/bash 

echo "hello master!" >/tmp/mastergreeting.txt

sudo apt-get update
sudo apt-get install -y make


sudo mkdir /home/ubuntu/.aws
cp ./files/config /home/ubuntu/.aws
sudo chown -R ubuntu:ubuntu /home/ubuntu/.aws


# ./installPackages.sh > /tmp/install_log.txt

# ./installPython.sh >> /tmp/install_log.txt

# ./install_python_modules.sh >> /tmp/install_log.txt

#./createDatabase.sh > /tmp/createdb_log.txt

#./setupDatacube.sh >/tmp/datacube_log.txt
