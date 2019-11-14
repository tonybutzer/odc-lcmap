#! /bin/bash

## postgreql

sudo apt-get update
sudo apt-get install -y postgresql-doc-9.5
sudo apt-get install -y postgresql
sudo apt-get install -y pgadmin3

# sudo sed -i 's/peer/md5/g' /etc/postgresql/9.5/main/pg_hba.conf
## sudo vi /etc/postgresql/9.5/main/pg_hba.conf
# sudo cp ./files/pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf
sudo cp ./files/pg_hba.conf /etc/postgresql/10/main/pg_hba.conf
sudo systemctl restart postgresql

sudo -u postgres createuser --superuser dc_user
sudo -u postgres psql -c "ALTER USER dc_user WITH PASSWORD 'localuser1234';"
echo HEY localuser1234
sudo createdb -U dc_user datacube

sudo cp ./files/datacube.conf /home/ubuntu
sudo chown ubuntu:ubuntu /home/ubuntu/datacube.conf
# sudo cp ./files/datacube.conf /home/tony
# sudo chown tony:tony /home/tony/datacube.conf

