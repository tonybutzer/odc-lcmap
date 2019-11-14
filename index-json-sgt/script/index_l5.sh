#! /bin/bash

# ' cp ../datacube.conf .

datacube --help

datacube --version

datacube system init

 echo hi



cd ../pkg; ./dropDatabaseTables.sh 

datacube product add ../product_definition/l5_kline.yaml  ## L5

datacube product list

echo "Now run the prepare script you have\'nt written yet"

# python3 ../bin/prepare_L7.py lsaa-test-cog --prefix=L5   # L5

python3 ../bin/prepare_L7.py lsaa-staging-cog --prefix=L05   # L5

datacube dataset search product ='l5_kline' |grep id |wc -l

# datacube dataset search product ='landsat_5_USARD' 

datacube dataset search product ='l5_kline' |grep s3


datacube product list


datacube dataset search product ='l5_kline' |grep id |wc -l


