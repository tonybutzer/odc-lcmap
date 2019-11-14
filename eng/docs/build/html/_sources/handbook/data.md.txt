# Data

## Metadata

### Maps

### Google Data Layer

[google data layer](https://developers.google.com/maps/documentation/javascript/datalayer)


[earth quakes example](https://google-developers.appspot.com/maps/documentation/javascript/earthquakes)

### Geojson

[geojson.io](http://geojson.io/#map=2/20.0/0.0)

[What is GeoJSON and why should you care about it?](https://www.youtube.com/watch?v=8RPfrhzRw2s)

- GeoJSON
    - spec for storing geographic data in JSON form.
    - Vector data -- Points, Lines and polygons
    - Attributes

- JSON
    - JavaScript Object Notation
    - Text from of JavaScript Objects
    - Text can be 
        - Stored in text files
        - Easily sent accross the internet to be uses in a web application
        - Stored in a database field


### STAC -- SpatioTemporal Asset Catalog 

[announcing-the-spatiotemporal-asset-catalog-stac-specification-](https://medium.com/radiant-earth-insights/announcing-the-spatiotemporal-asset-catalog-stac-specification-1db58820b9cf)


[radiantearth/stac-spec ](https://github.com/radiantearth/stac-spec)

**Overview Outline**

- 14 organizations
    - increase interoperability
    - ease search of satellite imagery
    - support single search
    - STAC aims to make that easier
- Common Metadata
- API
- Tools?
    - Browser

- Core
    - **Solid**
    - **small**
    - flexible
- wide variety of information
    - derived data
    - point clouds
    - hyperspectral

- __Item__
    - GeoJSON Feature
    - links to its corresponding 'assets'
        - downloaded  (can be)
        - streamed (can be)

- Global Index
    - all imagery
        - satellite
        - aerial
        - drone
    - derived data products
    - alternate geospatial captures
        - LiDAR
        - SAR
        - Full Motion Video
        - Hyperspectral

- Standard
    - organizations expose their data in a persistent and reliable way
    - crawled (traversed) not scraped

- Not a single catalog
    - encourage a basic unit of information
- The actual geospatial asset
    - a geotiff
    - should be a **COG**
- a JSON description of the core fields 
- This mirrors the world wide web as a whole
- geospatial search is left as an exercise for the students
    - good students like Google, Amazon, Bing


#### Specification Overview Outline

- A STAC Item is the core of any implementing Catalog
    - is defined by a json specification.


**power of STAC posts**

[the-potential-of-spatiotemporal-asset](https://medium.com/radiant-earth-insights/the-potential-of-spatiotemporal-asset-catalogs-a9323927dc8a)
[static-spatiotemporal-asset-catalogs-in-depth](https://medium.com/radiant-earth-insights/static-spatiotemporal-asset-catalogs-in-depth-710530934a84)
