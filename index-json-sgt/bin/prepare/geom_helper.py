"""

MODULE: geom_helper
===================

1. Helps with geometry concepts and transforms

* Notably between Geographic (lat, lon) and Albers Equal Area (x,y)

more to come ...

"""

from pyproj import Proj

def ge_translate(lat,lon,epsg="epsg:5072"):
    """ converts lat lon to albers X and Y

        Returns: x, y
    """
    print(lat,lon)

    p = Proj(init=epsg) # EPSG code AEA

    
    x,y = p(lon,lat)

    print(x,y)
    return(x,y)


def ge_untranslate(x,y,epsg="epsg:5072"):
    """ converts albers X and Y to lat, lon

        Returns: lat, lon
    """
    print(x,y)

    p = Proj(init=epsg) # EPSG code AEA

    
    glon, glat = p(x, y, inverse=True)


    print(glat,glon)
    return(glat,glon)



