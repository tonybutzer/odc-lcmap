#! /bin/bash

datacube dataset search product ='l5_kline' |grep id |wc -l
datacube dataset search product ='l7_kline' |grep id |wc -l
datacube dataset search product ='l8_kline' |grep id |wc -l

