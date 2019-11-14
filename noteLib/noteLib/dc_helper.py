import datacube
import time

from datetime import datetime

def dc_find_datasets(date_range, product='landsat_8_USARD', cloud_threshold = 20, fill_threshold = 30 ):


    dc = datacube.Datacube(app = 'my_app', config = '../datacube.conf')

    dss = dc.find_datasets(product=product, time=date_range, measurements=['red',])

    clear_datasets = []
    for item in dss:
        if float(item.metadata_doc['cloud_cover']) < cloud_threshold:
            if float(item.metadata_doc['fill']) < fill_threshold:
                clear_datasets.append(item)
            
    print("Number of Pretty Scenes", len(clear_datasets))
    return clear_datasets

def compute_tile_chip_span(h,v,ch,cv,datasets):
    
    citem = datasets[0]
    citem.bounds

    l = citem.bounds.left

    b = citem.bounds.bottom

    r = citem.bounds.right
    
    t = citem.bounds.top

    x1 = l + (ch * 100) * 30
    x2 = l + ((ch + 1) * 100 - 1) * 30
    y1 = t - (cv * 100) * 30
    y2 = t - ((cv + 1) * 100 - 1) * 30
    return x1,x2,y1,y2

def dc_load_tile_chip(h,v,ch,cv,datasets,measurements,product='landsat_8_USARD'):

    x1,x2,y1,y2 = compute_tile_chip_span(h,v,ch,cv,datasets)
    dc = datacube.Datacube(app = 'dc_helper', config = '../datacube.conf')
    ds2 = dc.load(product=product, datasets=datasets, measurements=measurements,
                  x=(x1,x2),y=(y1,y2), crs='epsg:5072',
                  output_crs = 'epsg:5072',
                  resolution = (-30,30))
    return (ds2)

