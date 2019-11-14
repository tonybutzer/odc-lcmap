#! /bin/bash

datacube product add ../product_definition/l7_kline.yaml  ## L5

datacube product list

echo "Now run the prepare script you have\'nt written yet"

# python3 ../bin/prepare_L7.py lsaa-test-cog --prefix=L7   # L7
python3 ../bin/prepare_L7.py lsaa-staging-cog --prefix=L07   # L7

datacube dataset search product ='l7_kline' |grep id |wc -l

datacube dataset search product ='l7_kline' |grep s3

datacube product list



