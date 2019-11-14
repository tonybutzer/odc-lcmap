import os
import folium
import itertools    
import math
import numpy as np  
from pyproj import Proj
from prepare import *
from .browse import build_browse


def _degree_to_zoom_level(l1, l2, margin = 0.0):
    
    degree = abs(l1 - l2) * (1 + margin)
    zoom_level_int = 0
    if degree != 0:
        zoom_level_float = math.log(360/degree)/math.log(2)
        zoom_level_int = int(zoom_level_float)
        zoom_level_int = zoom_level_int - 1
    else:
        zoom_level_int = 18
    return zoom_level_int


def _aea_return_zoom(ulX, ulY, lrX, lrY):

    ###### ###### ######   GENERATE ALL CORNERS FROM ul and lr       ###### ###### ######

    urX = lrX
    urY = ulY

    llX = ulX
    llY = lrY

    #######################    NOW Make the Geographic (Lat/Lon) CORNERS #######################

    p = Proj(init='epsg:5072') # EPSG code AEA

    gulX, gulY = p(ulX, ulY, inverse=True)
    gurX, gurY = p(urX, urY, inverse=True)

    glrX, glrY = p(lrX, lrY, inverse=True)
    gllX, gllY = p(llX, llY, inverse=True)


    return 8


def aea_base_map(ulX, ulY, lrX, lrY, resolution = None):
    """ Generates a folium map with a lat-lon bounded rectangle drawn on it. Folium maps can be 
    
    ul and lr are in crs -  EPSG:5072 -- usard uses this.
    
    Args:
        ul and lr are in AEA meters from the origin

    Returns:
        folium.Map: A map centered on the lat lon bounds. A rectangle is drawn on this map detailing the
        perimeter of the lat,lon bounds.  A zoom level is calculated such that the resulting viewport is the
        closest it can possibly get to the centered bounding rectangle without clipping it. An 
        optional grid can be overlaid with primitive interpolation.  

    .. _Folium
        https://github.com/python-visualization/folium

    """
    


    ###### ###### ######   GENERATE ALL CORNERS FROM ul and lr       ###### ###### ######

    urX = lrX
    urY = ulY

    llX = ulX
    llY = lrY

    aea_corners = (ulX,ulY, urX, urY, lrX, lrY, llX, llY)
    # print("aea_corners", aea_corners)


    #######################    NOW Make the Geographic (Lat/Lon) CORNERS #######################

    p = Proj(init='epsg:5072') # EPSG code AEA

    gulX, gulY = p(ulX, ulY, inverse=True)
    gurX, gurY = p(urX, urY, inverse=True)

    glrX, glrY = p(lrX, lrY, inverse=True)
    gllX, gllY = p(llX, llY, inverse=True)

    ###### ###### ######   CENTER POINT        ###### ###### ######
    
    center_aeaX, center_aeaY = [np.mean((ulX,urX)), np.mean((ulY, llY))]

    gcenterX, gcenterY = p(center_aeaX, center_aeaY, inverse=True)

    center = (gcenterY, gcenterX)

    ###### ###### ######   CALC ZOOM LEVEL     ###### ###### ######

    latitude = (gulY, gllY)
    longitude = (gulY, gllY)

    margin = -0.5
    zoom_bias = 0
    
    lat_zoom_level = _degree_to_zoom_level(margin = margin, *latitude ) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(margin = margin, *longitude) + zoom_bias
    zoom_level = min(lat_zoom_level, lon_zoom_level) 
    ###### ###### ######   CREATE MAP         ###### ###### ######
    
    map_hybrid = folium.Map(
        location=center,
        zoom_start=zoom_level, 
        tiles=" http://mt1.google.com/vt/lyrs=y&z={z}&x={x}&y={y}",
        attr="Google"
    )
    
    
    map_hybrid.add_child(folium.features.LatLngPopup())        

    return map_hybrid



def prj_base_map(ulX, ulY, lrX, lrY, resolution = None, epsg='epsg:32636'):
    """ Generates a folium map with a lat-lon bounded rectangle drawn on it. Folium maps can be 
    
    ul and lr are in crs -  ie EPSG:5072 -- usard uses this. but also others
    
    Args:
        ul and lr are in AEA meters from the origin

    Returns:
        folium.Map: A map centered on the lat lon bounds. A rectangle is drawn on this map detailing the
        perimeter of the lat,lon bounds.  A zoom level is calculated such that the resulting viewport is the
        closest it can possibly get to the centered bounding rectangle without clipping it. An 
        optional grid can be overlaid with primitive interpolation.  

    .. _Folium
        https://github.com/python-visualization/folium

    """
    


    ###### ###### ######   GENERATE ALL CORNERS FROM ul and lr       ###### ###### ######

    urX = lrX
    urY = ulY

    llX = ulX
    llY = lrY

    aea_corners = (ulX,ulY, urX, urY, lrX, lrY, llX, llY)
    # print("aea_corners", aea_corners)


    #######################    NOW Make the Geographic (Lat/Lon) CORNERS #######################
    

    p = Proj(init=epsg) # EPSG code AEA

    gulX, gulY = p(ulX, ulY, inverse=True)
    gurX, gurY = p(urX, urY, inverse=True)

    glrX, glrY = p(lrX, lrY, inverse=True)
    gllX, gllY = p(llX, llY, inverse=True)

    ###### ###### ######   CENTER POINT        ###### ###### ######
    
    center_aeaX, center_aeaY = [np.mean((ulX,urX)), np.mean((ulY, llY))]

    gcenterX, gcenterY = p(center_aeaX, center_aeaY, inverse=True)

    center = (gcenterY, gcenterX)

    ###### ###### ######   CALC ZOOM LEVEL     ###### ###### ######

    latitude = (gulY, gllY)
    longitude = (gulY, gllY)

    margin = -0.5
    zoom_bias = 0
    
    lat_zoom_level = _degree_to_zoom_level(margin = margin, *latitude ) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(margin = margin, *longitude) + zoom_bias
    zoom_level = min(lat_zoom_level, lon_zoom_level) 
    ###### ###### ######   CREATE MAP         ###### ###### ######
    
    map_hybrid = folium.Map(
        location=center,
        zoom_start=zoom_level, 
        tiles=" http://mt1.google.com/vt/lyrs=y&z={z}&x={x}&y={y}",
        attr="Google"
    )
    
    
    map_hybrid.add_child(folium.features.LatLngPopup())        

    return map_hybrid



def prj_display_map(m, ulX, ulY, lrX, lrY, resolution = None, color = 'red', epsg = 'epsg:5072'):
    """ Generates a folium map with a lat-lon bounded rectangle drawn on it. Folium maps can be 
    
    ul and lr are in crs -  EPSG:5072 -- usard uses this.
    
    Args:
        m = the map object/element creadet by aea_base_map
        ul and lr are in AEA meters from the origin

    Returns:
        folium.Map: A map centered on the lat lon bounds. A rectangle is drawn on this map detailing the
        perimeter of the lat,lon bounds.  A zoom level is calculated such that the resulting viewport is the
        closest it can possibly get to the centered bounding rectangle without clipping it. An 
        optional grid can be overlaid with primitive interpolation.  

    .. _Folium
        https://github.com/python-visualization/folium

    """
    


    ###### ###### ######   GENERATE ALL CORNERS FROM ul and lr       ###### ###### ######

    urX = lrX
    urY = ulY

    llX = ulX
    llY = lrY

    aea_corners = (ulX,ulY, urX, urY, lrX, lrY, llX, llY)
    # print("aea_corners", aea_corners)


    #######################    NOW Make the Geographic (Lat/Lon) CORNERS #######################

    p = Proj(init=epsg) # EPSG code AEA

    gulX, gulY = p(ulX, ulY, inverse=True)
    gurX, gurY = p(urX, urY, inverse=True)

    glrX, glrY = p(lrX, lrY, inverse=True)
    gllX, gllY = p(llX, llY, inverse=True)

    ###### ###### ######   CENTER POINT        ###### ###### ######
    
    center_aeaX, center_aeaY = [np.mean((ulX,urX)), np.mean((ulY, llY))]

    gcenterX, gcenterY = p(center_aeaX, center_aeaY, inverse=True)

    center = (gcenterY, gcenterX)

    ###### ###### ######   CALC ZOOM LEVEL     ###### ###### ######

    latitude = (gulY, gllY)
    longitude = (gulY, gllY)

    margin = -0.5
    zoom_bias = 0
    
    lat_zoom_level = _degree_to_zoom_level(margin = margin, *latitude ) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(margin = margin, *longitude) + zoom_bias
    zoom_level = min(lat_zoom_level, lon_zoom_level) 
    ###### ###### ######   CREATE MAP         ###### ###### ######
    
    map_hybrid = m
    
    
    ###### ###### ######     BOUNDING BOX     ###### ###### ######
    
    line_segments = [(gulY,gulX),
                     (gurY,gurX),
                     (glrY,glrX),
                     (gllY,gllX),
                     (gulY,gulX)
                    ]

    # print("line_segments", line_segments)



    
    map_hybrid.add_child(
        folium.features.PolyLine(
            locations=line_segments,
            color=color,
            # color='red',
            opacity=0.8)
    )

    map_hybrid.add_child(folium.features.LatLngPopup())        

    return map_hybrid

def geo_display_map(m, ul_lat, ul_lon, ur_lat, ur_lon, lr_lat, lr_lon,  ll_lat, ll_lon,
                    resolution = None, color = 'yellow'):
    """ Generates a folium map with a lat-lon bounded rectangle drawn on it. 
    
    ul ur, lr, and ll are in geograhic lat long - 
    
    Args:
        m = the map object/element creadet by aea_base_map
        ul and lr are in AEA meters from the origin

    Returns:
        folium.Map: A map centered on the lat lon bounds. A rectangle is drawn on this map detailing the
        perimeter of the lat,lon bounds.  A zoom level is calculated such that the resulting viewport is the
        closest it can possibly get to the centered bounding rectangle without clipping it. An 
        optional grid can be overlaid with primitive interpolation.  

    .. _Folium
        https://github.com/python-visualization/folium

    """
    


    ###### ###### ######   CENTER POINT        ###### ###### ######
    
    gcenterY = (ul_lat + lr_lat) / 2
    gcenterX = (ul_lon + lr_lon) / 2

    center = (gcenterY, gcenterX)

    ###### ###### ######   CALC ZOOM LEVEL     ###### ###### ######

    latitude = (ul_lat, ll_lat)
    longitude = (ul_lon, ll_lon)

    margin = -0.5
    zoom_bias = 0
    
    lat_zoom_level = _degree_to_zoom_level(margin = margin, *latitude ) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(margin = margin, *longitude) + zoom_bias
    zoom_level = min(lat_zoom_level, lon_zoom_level) 
    ###### ###### ######   CREATE MAP         ###### ###### ######
    
    map_hybrid = m
    
    
    ###### ###### ######     BOUNDING BOX     ###### ###### ######
    
    line_segments = [(ul_lat,ul_lon),
                     (ur_lat,ur_lon),
                     (lr_lat,lr_lon),
                     (ll_lat,ll_lon),
                     (ul_lat,ul_lon)
                    ]

    # print("line_segments", line_segments)



    
    map_hybrid.add_child(
        folium.features.PolyLine(
            locations=line_segments,
            color=color,
            opacity=0.8)
    )

    map_hybrid.add_child(folium.features.LatLngPopup())        

    return map_hybrid




def display_map(latitude = None, longitude = None, resolution = None):
    """ Generates a folium map with a lat-lon bounded rectangle drawn on it. Folium maps can be 
    
    Args:
        latitude   (float,float): a tuple of latitude bounds in (min,max) format
        longitude  ((float, float)): a tuple of longitude bounds in (min,max) format
        resolution ((float, float)): tuple in (lat,lon) format used to draw a grid on your map. Values denote   
                                     spacing of latitude and longitude lines.  Gridding starts at top left 
                                     corner. Default displays no grid at all.  

    Returns:
        folium.Map: A map centered on the lat lon bounds. A rectangle is drawn on this map detailing the
        perimeter of the lat,lon bounds.  A zoom level is calculated such that the resulting viewport is the
        closest it can possibly get to the centered bounding rectangle without clipping it. An 
        optional grid can be overlaid with primitive interpolation.  

    .. _Folium
        https://github.com/python-visualization/folium

    """
    
    assert latitude is not None
    assert longitude is not None

    ###### ###### ######   CALC ZOOM LEVEL     ###### ###### ######

    margin = -0.5
    zoom_bias = 0
    
    lat_zoom_level = _degree_to_zoom_level(margin = margin, *latitude ) + zoom_bias
    lon_zoom_level = _degree_to_zoom_level(margin = margin, *longitude) + zoom_bias
    zoom_level = min(lat_zoom_level, lon_zoom_level) 

    ###### ###### ######   CENTER POINT        ###### ###### ######
    
    center = [np.mean(latitude), np.mean(longitude)]

    ###### ###### ######   CREATE MAP         ###### ###### ######
    
    map_hybrid = folium.Map(
        location=center,
        zoom_start=zoom_level, 
        tiles=" http://mt1.google.com/vt/lyrs=y&z={z}&x={x}&y={y}",
        attr="Google"
    )
    
    ###### ###### ######   RESOLUTION GRID    ###### ###### ######
    
    if resolution is not None:
        res_lat, res_lon = resolution

        lats = np.arange(abs(res_lat), *latitude)
        lons = np.arange(abs(res_lon), *longitude)

        vertical_grid   = map(lambda x :([x[0][0],x[1]],[x[0][1],x[1]]),itertools.product([latitude],lons))
        horizontal_grid = map(lambda x :([x[1],x[0][0]],[x[1],x[0][1]]),itertools.product([longitude],lats))

        for segment in vertical_grid:
            folium.features.PolyLine(segment, color = 'white', opacity = 0.3).add_to(map_hybrid)    
        
        for segment in horizontal_grid:
            folium.features.PolyLine(segment, color = 'white', opacity = 0.3).add_to(map_hybrid)   
    
    ###### ###### ######     BOUNDING BOX     ###### ###### ######
    
    line_segments = [(latitude[0],longitude[0]),
                     (latitude[0],longitude[1]),
                     (latitude[1],longitude[1]),
                     (latitude[1],longitude[0]),
                     (latitude[0],longitude[0])
                    ]
    
    
    
    map_hybrid.add_child(
        folium.features.PolyLine(
            locations=line_segments,
            color='red',
            opacity=0.8)
    )

    map_hybrid.add_child(folium.features.LatLngPopup())        

    return map_hybrid


def add_display_map(map_hybrid, latitude = None, longitude = None):
    """ Generates a folium map with a lat-lon bounded rectangle drawn on it. Folium maps can be 
    
    Args:
        map_hybrid - existing map object
        latitude   (float,float): a tuple of latitude bounds in (min,max) format
        longitude  ((float, float)): a tuple of longitude bounds in (min,max) format

    Returns:
        folium.Map: A map centered on the lat lon bounds. A rectangle is drawn on this map detailing the
        perimeter of the lat,lon bounds.  A zoom level is calculated such that the resulting viewport is the
        closest it can possibly get to the centered bounding rectangle without clipping it. An 
        optional grid can be overlaid with primitive interpolation.  

    .. _Folium
        https://github.com/python-visualization/folium

    """
    
    assert latitude is not None
    assert longitude is not None


    ###### ###### ######   CENTER POINT        ###### ###### ######
    
    center = [np.mean(latitude), np.mean(longitude)]

    ###### ###### ######   CREATE MAP         ###### ###### ######
    
    
    ###### ###### ######     BOUNDING BOX     ###### ###### ######
    
    line_segments = [(latitude[0],longitude[0]),
                     (latitude[0],longitude[1]),
                     (latitude[1],longitude[1]),
                     (latitude[1],longitude[0]),
                     (latitude[0],longitude[0])
                    ]
    
    
    
    map_hybrid.add_child(
        folium.features.PolyLine(
            locations=line_segments,
            color='red',
            opacity=0.8)
    )

    map_hybrid.add_child(folium.features.LatLngPopup())        

    return map_hybrid


def display_browse(aoi, myds):
    """ display the browse image for this scene and the area of interest
        aoi is the area of interest in geographic (lat/long) coordinates

    """
    rgb = []
    rgb.append(myds.measurements['red']['path'])
    rgb.append(myds.measurements['green']['path'])
    rgb.append(myds.measurements['blue']['path'])

    print(rgb)
    ulX = myds.bounds.left
    ulY = myds.bounds.top

    lrX = myds.bounds.right
    lrY = myds.bounds.bottom

    ep = myds.crs

    gulx,guly = ge_untranslate(ulX,ulY,epsg=ep)

    glrx,glry = ge_untranslate(lrX,lrY,epsg=ep)

    my_ul = [gulx,guly]
    my_lr = [glrx,glry]

    out = 'dummy.png'
    the_browse = build_browse(rgb, out)

    merc = the_browse

# m = folium.Map([37, 0], zoom_start=1, tiles='stamentoner')

    m = prj_base_map(ulX,ulY,lrX,lrY,resolution=None, epsg=ep)
    m = prj_display_map(m,ulX,ulY,lrX,lrY, color='yellow', epsg=ep)

    ul_lon,ul_lat,lr_lon,lr_lat = aoi
    ulx,uly = ge_translate(ul_lat,ul_lon,epsg=ep)
    lrx,lry = ge_translate(lr_lat,lr_lon,epsg=ep)
    m = prj_display_map(m,ulx,uly,lrx,lry, color='red', epsg=ep)
    img = folium.raster_layers.ImageOverlay(
        name='Mercator projection SW',
        image=merc,
        bounds=[my_ul, my_lr],
        #
        opacity=0.8,
        interactive=True,
        cross_origin=False,
        zindex=1,
    )

    folium.Popup('I am an image').add_to(img)

    img.add_to(m)

    folium.LayerControl().add_to(m)
    return m
