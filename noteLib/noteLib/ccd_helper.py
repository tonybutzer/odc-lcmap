
import ccd
import pandas as pd
import numpy as np
from datetime import datetime


def get_color_params(ds, inx, iny):
   
    landsat_dataset = ds
    myx = inx
    myy = iny

    myred = landsat_dataset.red[:, myy, myx].values

    myblue = landsat_dataset.blue[:, myy, myx].values

    mygreen = landsat_dataset.green[:, myy, myx].values
    mynir = landsat_dataset.nir[:, myy, myx].values
    myswir1 = landsat_dataset.swir1[:, myy, myx].values
    myswir2 = landsat_dataset.swir2[:, myy, myx].values
    mypixel_qa = landsat_dataset.pixel_qa[:, myy, myx].values

    dts = landsat_dataset.time.values
    scene_count = len(dts)
    mythermals = np.ones(scene_count) * (273.15) * 10
    
    ordinal_dates = []
    for mydate in dts:
        dval = datetime.utcfromtimestamp(mydate.tolist()/1e9)
        ordinal_dates.append(dval.toordinal())
        
        
    params = (ordinal_dates, myblue, mygreen, myred, mynir, myswir1, myswir2, mythermals, mypixel_qa)

    mystery_object = ccd.detect(*params)

    return mystery_object


def l7_get_color_params(ds, inx, iny):
   
    landsat_dataset = ds
    myx = inx
    myy = iny

    myred = landsat_dataset.red[:, myy, myx].values

    myblue = landsat_dataset.blue[:, myy, myx].values

    mygreen = landsat_dataset.green[:, myy, myx].values
    mynir = landsat_dataset.nir[:, myy, myx].values
    myswir1 = landsat_dataset.swir1[:, myy, myx].values
    myswir2 = landsat_dataset.swir2[:, myy, myx].values
    mypixel_qa = landsat_dataset.pixel_qa[:, myy, myx].values
    # mythermals = landsat_dataset.therm[:, myy, myx].values

    dts = landsat_dataset.time.values
    scene_count = len(dts)
    mythermals = np.ones(scene_count) * (273.15) * 10
    
    ordinal_dates = []
    for mydate in dts:
        dval = datetime.utcfromtimestamp(mydate.tolist()/1e9)
        ordinal_dates.append(dval.toordinal())
        
        
    qa_bit_params = {'QA_BITPACKED': False,
              'QA_FILL': 255,
              'QA_CLEAR': 0,
              'QA_WATER': 1,
              'QA_SHADOW': 2,
              'QA_SNOW': 3,
              'QA_CLOUD': 4}

    bparams = (ordinal_dates, myblue, mygreen, myred, mynir, myswir1, myswir2, mythermals, mypixel_qa)

    mystery_object = ccd.detect(*bparams, params = qa_bit_params)

    return mystery_object


def get_prob_array(the_xarray, prob_type='water_prob'):
    width = 100
    height = 100
    prob_array = np.zeros(shape = (width, height))
    for x in range(0,width):
        for y in range(0,height):
            mo = get_color_params(the_xarray,y,x) # (note the y,x for numpy array filling axis sanity)
            #print("MO=",mo)
            print(x,y,prob_type,"prob",mo[prob_type])
        
            prob_array[x,y] = mo[prob_type]

    return prob_array


def l7_get_prob_array(the_xarray, prob_type='water_prob'):
    width = 100
    height = 100
    prob_array = np.zeros(shape = (width, height))
    for x in range(0,width):
        for y in range(0,height):
            mo = l7_get_color_params(the_xarray,y,x) # (note the y,x for numpy array filling axis sanity)
            #print("MO=",mo)
            print(x,y,prob_type,"prob",mo[prob_type])
        
            prob_array[x,y] = mo[prob_type]

    return prob_array
