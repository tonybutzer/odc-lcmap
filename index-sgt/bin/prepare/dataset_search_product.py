
import datacube

from datetime import datetime

from datacube.index import index_connect

local_config = "/opt/index/anotebooks/datacube.conf"
# index = index_connect(local_config, "me_app" )
index = index_connect()

expressions = {'product': 'landsat_USARD'}

limit=1000
datasets = index.datasets.search(limit=limit, **expressions)

# for dataset in datasets:
    #print(dataset)


dc = datacube.Datacube()


date_range = (
        datetime(2013,6,1),
        datetime(2013,6,15))
dss = dc.find_datasets(product='landsat_USARD', time=date_range, measurements=['red',])

for item in dss:
    print(item)
    # print(dir(item))
    print(item.uris)
    # print(item.local_path)
    print(item.measurements['red'])
