#! /bin/bash

# ' cp ../datacube.conf .

datacube --help

datacube --version

datacube system init

 echo hi

./dropDatabaseTables.sh 

datacube product add ../product_definition/wip-product_definition_USARD_L5.yaml  ## L5

datacube product list

echo "Now run the prepare script you have written!"

python3 ../bin/prepare_L7.py ga-odc-eros-ard-west --prefix=usard/LT05   # L5

datacube dataset search product ='landsat_5_USARD' |grep id |wc -l

datacube dataset search product ='landsat_5_USARD' 

datacube dataset search product ='landsat_5_USARD' |grep s3

## L7
datacube product add ../product_definition/wip-product_definition_USARD_L7.yaml  ## L7

python3 ../bin/prepare_L7.py ga-odc-eros-ard-west --prefix=usard/LE07   # L7


## L8
datacube product add ../product_definition/product_definition_USARD_L8_V2.yaml

python3 ../bin/prepare_L8.py ga-odc-eros-ard-west --prefix=usard/LC08




datacube product list




datacube dataset search product ='landsat_5_USARD' |grep id |wc -l
datacube dataset search product ='landsat_7_USARD' |grep id |wc -l
datacube dataset search product ='landsat_8_USARD' |grep id |wc -l


