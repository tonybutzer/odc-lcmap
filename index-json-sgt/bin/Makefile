testl8:
	python3 ./prepare_L8.py lsaa-staging-cog --prefix L08

count:
	datacube dataset search product ='l8_kline' |grep s3


cleardb:
	(cd /opt/odc-lcmap/index-json-sgt/script ; ./dropDatabaseTables.sh)
	datacube product add ../product_definition/l8_kline.yaml
	datacube product list
