#! /bin/bash

# ' cp ../datacube.conf .

datacube --help

datacube --version

datacube system init

 echo hi

./dropDatabaseTables.sh 

## L7
datacube product add ../product_definition/wip-product_definition_USARD_L7.yaml  ## L7

datacube product list

echo "Now run the prepare script you have written!"

python3 ../bin/prepare_L7.py ga-odc-eros-ard-west --prefix=usard/LE07   # L7

 datacube dataset search product ='landsat_7_USARD' |grep id |wc -l

# datacube dataset search product ='landsat_7_USARD' 

# datacube dataset search product ='landsat_7_USARD' |grep s3

