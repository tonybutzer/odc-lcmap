#! /bin/bash

# ' cp ../datacube.conf .


./index_l5.sh
./index_l7.sh
./index_l8.sh




datacube product list




datacube dataset search product ='l5_kline' |grep id |wc -l
datacube dataset search product ='l7_kline' |grep id |wc -l
datacube dataset search product ='l8_kline' |grep id |wc -l


