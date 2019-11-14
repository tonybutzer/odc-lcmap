#! /bin/bash

# ' cp ../datacube.conf .

datacube --help

datacube --version

datacube system init

 echo hi



cd ../pkg; ./dropDatabaseTables.sh 

datacube product add ../product_definition/wip-product_definition_USARD_L5.yaml  ## L5

datacube product list

echo "Now run the prepare script you have\'nt written yet"


python3 ../bin/prepare_L7.py ga-odc-eros-ard-west --prefix=usard/LT05   # L5


datacube dataset search product ='landsat_5_USARD' |grep id |wc -l


datacube dataset search product ='landsat_5_USARD' 


datacube dataset search product ='landsat_5_USARD' |grep s3





datacube product list




datacube dataset search product ='landsat_5_USARD' |grep id |wc -l
datacube dataset search product ='landsat_7_USARD' |grep id |wc -l
datacube dataset search product ='landsat_8_USARD' |grep id |wc -l


