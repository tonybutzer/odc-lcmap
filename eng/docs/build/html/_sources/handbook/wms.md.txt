# WMS

## ODC and WMS plus WMTS and sometimes WCS

### Docker

1. Start the instance 
2. Run the Docker



```bash
docker run \
	 --rm \
    opendatacube/wms \
    gunicorn -b '0.0.0.0:8000' -w 5 --timeout 300 datacube_wms:wms
```

### Error 

```bash
Warning: missing DB_DATABASE environment variable
 File "/usr/local/lib/python3.6/dist-packages/gunicorn/arbiter.py", line 528, in reap_workers
    raise HaltServer(reason, self.APP_LOAD_ERROR)
gunicorn.errors.HaltServer: <HaltServer 'App failed to load.' 4>
```

### Now What?

### WBS

1. read the docs; limited; DONE!
2. play with the parts
	- cube-in-a-box; cloud-sanity?
	- flask
	- gunicorn
3. save to git and publish the docs
	- odc-modis
	- odc-lcmap; sleepy
		- publish



[https://github.com/opendatacube/datacube-ows](https://github.com/opendatacube/datacube-ows)

[https://datacube-ows.readthedocs.io](https://datacube-ows.readthedocs.io).

![WMTSpyramid](assets/WMTSpyramid.png)


![WMTSarchitecture](assets/WMTSarchitecture.png)

OGC WMS



## Layers



#### USGS



[https://viewer.nationalmap.gov/services/](https://viewer.nationalmap.gov/services/)





## Clients

[http://www.arcgis.com/home/webmap/viewer.html](http://www.arcgis.com/home/webmap/viewer.html)

[http://www.arcgis.com/home/webmap/viewer.html](http://www.arcgis.com/home/webmap/viewer.html)

## Servers

## Open Data Cube

[https://github.com/opendatacube/datacube-ows](https://github.com/opendatacube/datacube-ows)

## Tutorial WMS

#### Searching the Geoportal

[http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0q.cgi?SERVICE=WMS&REQUEST=GetCapabilities](http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0q.cgi?SERVICE=WMS&REQUEST=GetCapabilities)

#### Build a weather map

1. start web client [http://www.arcgis.com/home/webmap/viewer.html](http://www.arcgis.com/home/webmap/viewer.html)
2. add geonames layer
   1. Modify Map - ADD+ (layer from web) **WFS**
   2. https://services.nationalmap.gov/arcgis/services/WFS/geonames/MapServer/WFSServer?request=GetCapabilities&service=WFS
   3. ADD layer
   4. Find address or place --> Sioux Falls
   5. Turn off geonames - structure - too busy
3. add water hydro info
   1. https://basemap.nationalmap.gov/arcgis/services/USGSHydroCached/MapServer/WMSServer?request=GetCapabilities&service=WMS
4. add radar weather
   1. http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0q.cgi?SERVICE=WMS&REQUEST=GetCapabilities
   2. zoom out - play with 45 minutes ago etc.
5. STRETCH GOAL - add flood water - hazards
   1. https://idpgis.ncep.noaa.gov/arcgis/services/NWS_Forecasts_Guidance_Warnings/sig_riv_fld_outlk/MapServer/WFSServer?request=GetCapabilities&service=WFS
   2. Change transparency to 50%
6. Flood Zones [https://msc.fema.gov/portal/search?AddressQuery=sioux%20falls#searchresultsanchor](https://msc.fema.gov/portal/search?AddressQuery=sioux%20falls#searchresultsanchor)
7. Ground Water etc - https://watersgeo.epa.gov/arcgis/services/OWPROGRAM/SDWIS_WMERC/MapServer/WMSServer?request=GetCapabilities&service=WMS
8. Real Time weather - cheat - [https://www.arcgis.com/home/item.html?id=bb37ceceeac14c829b2cf449ff0c14d8](https://www.arcgis.com/home/item.html?id=bb37ceceeac14c829b2cf449ff0c14d8)
9. Flood cheat - [http://www.arcgis.com/home/webmap/viewer.html?url=http%3A%2F%2Fidpgis.ncep.noaa.gov%2Farcgis%2Frest%2Fservices%2FNWS_Forecasts_Guidance_Warnings%2Fsig_riv_fld_outlk%2FMapServer&source=sd](http://www.arcgis.com/home/webmap/viewer.html?url=http%3A%2F%2Fidpgis.ncep.noaa.gov%2Farcgis%2Frest%2Fservices%2FNWS_Forecasts_Guidance_Warnings%2Fsig_riv_fld_outlk%2FMapServer&source=sd)

### Example Map 

![weather flood](./assets/weatherFloodMap.png)
