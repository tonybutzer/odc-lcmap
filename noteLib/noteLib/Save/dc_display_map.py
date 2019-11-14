import folium
import itertools    
import math
import numpy as np  
from pyproj import Proj


def _degree_to_zoom_level(l1, l2, margin = 0.0):
    
    degree = abs(l1 - l2) * (1 + margin)
    zoom_level_int = 0
    if degree != 0:
        zoom_level_float = math.log(360/degree)/math.log(2)
        zoom_level_int = int(zoom_level_float)
    else:
        zoom_level_int = 18
    return zoom_level_int


def _aea_return_zoom():
    return 8


def aea_display_map(ulX, ulY, lrX, lrY, resolution = None):
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
    

    ###### ###### ######   CALC ZOOM LEVEL     ###### ###### ######

    # margin = -0.5
    # zoom_bias = 0
    
    # lat_zoom_level = _degree_to_zoom_level(margin = margin, *latitude ) + zoom_bias
    # lon_zoom_level = _degree_to_zoom_level(margin = margin, *longitude) + zoom_bias
    # zoom_level = min(lat_zoom_level, lon_zoom_level) 

    ## FIX THIS hard code for now

    zoom_level = _aea_return_zoom()



    ###### ###### ######   GENERATE ALL CORNERS FROM ul and lr       ###### ###### ######

    urX = lrX
    urY = ulY

    llX = ulX
    llY = lrY

    aea_corners = (ulX,ulY, urX, urY, lrX, lrY, llX, llY)
    print("aea_corners", aea_corners)


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

    ###### ###### ######   CREATE MAP         ###### ###### ######
    
    map_hybrid = folium.Map(
        location=center,
        zoom_start=zoom_level, 
        tiles=" http://mt1.google.com/vt/lyrs=y&z={z}&x={x}&y={y}",
        attr="Google"
    )
    
    
    ###### ###### ######     BOUNDING BOX     ###### ###### ######
    
    line_segments = [(gulY,gulX),
                     (gurY,gurX),
                     (glrY,glrX),
                     (gllY,gllX),
                     (gulY,gulX)
                    ]

    print("line_segments", line_segments)

    
    map_hybrid.add_child(
        folium.features.PolyLine(
            locations=line_segments,
            color='red',
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


