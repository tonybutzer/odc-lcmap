
#

'''

NOTES:

conus_ulX = -2565585 # - longitude
conus_ulY = 3314805

conus_lrX = 2384415
conus_lrY = 14805 #  - latitude

# geog_lon, geog_lat = p(longitude,latitude,inverse=True)

'''


from pyproj import Proj
from noteLib import *


def return_map_useful_extent(ulX, ulY, lrX, lrY):
    """ this function returns the maximum span in lat long - 
        needed by the folio epsg 4326 to draw the correct red ~rectangle
    """
# Create projection transformation object

    p = Proj(init='epsg:5072') # EPSG code AEA
    
    t = ulY
    l = ulX
    b = lrY
    r = lrX
    
    urX = r
    urY = t
    
    llX = l
    llY = b
    
    gulX, gulY = p(ulX, ulY, inverse=True)
    glrX, glrY = p(lrX, lrY, inverse=True)
    gurX, gurY = p(urX, urY, inverse=True)
    gllX, gllY = p(llX, llY, inverse=True)
    
    xmin = min(gulX,glrX,gurX,gllX)
    xmax = max(gulX,glrX,gurX,gllX)
    
    # print(xmin,xmax)
    
    ymin = min(gulY,glrY,gurY,gllY)
    ymax = max(gulY,glrY,gurY,gllY)
    
    # print(ymin,ymax)
    
    return (xmin,xmax,ymin,ymax)
    


def return_tile_corners(h,v):
    """ returns ul and lr for the tile in meters AEA"""
    
    conus_ulX = -2565585 # - longitude
    conus_ulY = 3314805
    
    span = 5000 * 30
    
    c_ulX = conus_ulX + (h * span)
    c_ulY = conus_ulY - (v * span)
    
    c_lrX = c_ulX + span
    c_lrY = c_ulY - span
    
    return (c_ulX, c_ulY, c_lrX, c_lrY)


def return_chip_corners(o_ulX, o_ulY, ch, cv):
    """ returns ul and lr for the chip in meters AEA"""
    
    origin_ulX = o_ulX # - longitude
    origin_ulY = o_ulY
    
    span = 100 * 30
    
    c_ulX = origin_ulX + (ch * span)
    c_ulY = origin_ulY - (cv * span)
    
    c_lrX = c_ulX + span
    c_lrY = c_ulY - span
    
    return (c_ulX, c_ulY, c_lrX, c_lrY)



def display_tile(h,v):
    """ this does not quite work - almost! """
  
    c_ulX, c_ulY, c_lrX, c_lrY = return_tile_corners(h,v)

    # print (c_ulX, c_ulY)

    xmin,xmax,ymin,ymax = return_map_useful_extent(c_ulX, c_ulY, c_lrX, c_lrY)

    lat_ext = (ymin,ymax)
    lon_ext = (xmin,xmax)
    
    return (display_map(latitude = lat_ext, longitude = lon_ext))

def aea_display_tile(h,v):
  
    c_ulX, c_ulY, c_lrX, c_lrY = return_tile_corners(h,v)

    # print (c_ulX, c_ulY)

    my_map = aea_base_map(c_ulX, c_ulY, c_lrX, c_lrY)
    my_map = aea_display_map(my_map, c_ulX, c_ulY, c_lrX, c_lrY)

    return my_map


def display_tile_chip(h, v, ch, cv):
    """ displays the chip of a 50 x 50 grid for a given tile"""
    from pyproj import Proj

    p = Proj(init='epsg:5072') # EPSG code AEA

    
    # print (h, v, ch, cv)
    t_ulX, t_ulY, t_lrX, t_lrY = return_tile_corners(h,v)
    
    # print(t_ulX, t_ulY, t_lrX, t_lrY)
    
    c_ulX, c_ulY, c_lrX, c_lrY = return_chip_corners(t_ulX, t_ulY, ch, cv)
    
    # print(c_ulX, c_ulY, c_lrX, c_lrY)
    
    my_map = aea_base_map(c_ulX, c_ulY, c_lrX, c_lrY)
    my_map = aea_display_map(my_map, c_ulX, c_ulY, c_lrX, c_lrY)


    return (my_map)


def add_display_tile_chip(m, h, v, ch, cv):
    """ displays the chip of a 50 x 50 grid for a given tile"""
    # print (h, v, ch, cv)
    t_ulX, t_ulY, t_lrX, t_lrY = return_tile_corners(h,v)
    
    # print(t_ulX, t_ulY, t_lrX, t_lrY)
    
    c_ulX, c_ulY, c_lrX, c_lrY = return_chip_corners(t_ulX, t_ulY, ch, cv)
    
    # print(c_ulX, c_ulY, c_lrX, c_lrY)
    my_map = aea_display_map(m, c_ulX, c_ulY, c_lrX, c_lrY)
    
    return (my_map)

