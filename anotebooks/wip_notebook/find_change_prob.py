from datetime import datetime

from noteLib import *

import numpy
import logging

def _return_change_array(the_xarray):
    width = 100
    height = 100
    change_array = numpy.zeros(shape = (width, height))
    for x in range(0,width):
        for y in range(0,height):
            mo = get_color_params(the_xarray,y,x) # (note the y,x for numpy array filling axis sanity
            # print(mo)
            for mod in mo['change_models']:
                change_array[x,y] = mod['change_probability']
                prob = change_array[x,y]
                if (prob > 0):
                    print(x,y,"change_prob",change_array[x,y])
                    logging.info("prob = %f" % prob)
                else:
                    print (x,y, end="")
        print("")
        
    return change_array


def _build_change_array(ch, cv):
    """ builds an change_probabilty array"""

    ### load the data ###

    date_range = (
        datetime(2013,1,1),
        # datetime(2016,7,1),
        datetime(2018,9,30))

    clear_list = dc_find_datasets(date_range=date_range)

    
    measurements = ['red', 'green', 'blue', 'nir', 'swir1', 'swir2', 'pixel_qa']

    h=3
    v=3

    dc_xarray = dc_load_tile_chip(h,v,ch,cv,datasets=clear_list,measurements=measurements)

    print(dc_xarray)
    _return_change_array(dc_xarray)



def Main():
    log_file = "./changeProb.log"
    my_level = logging.INFO
    logging.basicConfig(filename=log_file, level=my_level,
                    format='%(levelname)s,%(name)s,%(asctime)s,%(message)s,')
    logging.info("Start Main Logging")

    cv = 1
    for ch in range(7,50):
        logging.info("Main ch=%s,cv=%s" % (ch,cv))
        _build_change_array(ch, cv)


Main()
