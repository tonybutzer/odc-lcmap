jupcloud:
	(export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml')

jup:
	(export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; jupyter notebook --allow-root --ip="*" --NotebookApp.token='yaml')

clear_db:
	(PGPASSWORD=localuser1234 psql -U dc_user datacube <dropTable.sql)

jup2:
	jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml'
jup3:
	(export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; jupyter notebook --allow-root --ip="0.0.0.0" --NotebookApp.token='yaml')

pandasfix:
	sudo pip3 install Cython 
	sudo apt-get update
	# sudo apt-get -y install gcc, g++
	sudo pip3 uninstall pandas
	sudo pip3 install pandas

netcdffix:
	sudo pip3 uninstall netCDF4
	sudo pip3 install netCDF4

numpyfix:
	sudo pip3 install --upgrade numpy

git:
	(cd /opt/odc-lcmap && make)

