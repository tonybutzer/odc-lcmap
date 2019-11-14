#! /bin/bash

datacube product add ../product_definition/l8_kline.yaml  ## L5

datacube product list

echo "Now run the prepare script you have\'nt written yet"

#python3 ../bin/prepare_L8.py lsaa-test-cog --prefix=L8   # L8

python3 ../bin/prepare_L8.py lsaa-staging-cog --prefix=L08   # L8

datacube dataset search product ='l8_kline' |grep id |wc -l

datacube dataset search product ='l8_kline' |grep s3

datacube product list
