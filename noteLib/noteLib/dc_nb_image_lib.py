## Image Display RGB Utils

import folium
import json
from rasterio.plot import show_hist
from matplotlib import pyplot
from datacube.storage import masking
from datacube import Datacube
from datetime import datetime
from skimage import exposure
import numpy as np
import osr
import ogr

def threeBandImage(ds, bands, time = 0, figsize = [10,10], projection = 'projected'):
    '''
    threeBandImage takes three spectral bands and plots them on the RGB bands of an image. 
    
    Inputs: 
    ds -   Dataset containing the bands to be plotted
    bands - list of three bands to be plotted
    
    Optional:
    time - Index value of the time dimension of ds to be plotted
    figsize - dimensions for the output figure
    projection - options are 'projected' or 'geographic'. To determine if the image is in degrees or northings
    '''
    t, y, x = ds[bands[0]].shape
    rawimg = np.zeros((y,x,3), dtype = np.float32)
    for i, colour in enumerate(bands):
        rawimg[:,:,i] = ds[colour][time].values
    rawimg[rawimg == -9999] = np.nan
    img_toshow = exposure.equalize_hist(rawimg, mask = np.isfinite(rawimg))

    return img_toshow

def loadConfigExtent():
    config = json.load(open('/opt/odc/data/extents.txt'))
    lon_min, lon_max, lat_min, lat_max = config['extent']
    #centre = [(lat_min+ lat_max)/2,(lon_min + lon_max)/2]
    rectangle =  [[lat_max,lon_min],[lat_max,lon_max], [lat_min,lon_max],[lat_min,lon_min],[lat_max,lon_min]]
    return [[lon_min, lon_max, lat_min, lat_max], rectangle]

 
def transformToWGS(getLong, getLat, EPSGa):
    source = osr.SpatialReference()
    source.ImportFromEPSG(EPSGa)

    target = osr.SpatialReference()
    target.ImportFromEPSG(4326)

    transform = osr.CoordinateTransformation(source, target)

    point = ogr.CreateGeometryFromWkt("POINT (" + str(getLong[0]) + " " + str(getLat[0]) + ")")
    point.Transform(transform)
    return [point.GetX(), point.GetY()]

def plot_labeled_rgb(ds, time, count=1, figsize = [8,8]):
    """
        plot_labeled_rgb 
        1. ds = dataset (from a datacube xarray)
        2. time is the obeservation acq date to select the observation to be plotted
        3. count is an integer to display , not that important
    """
    
    img_toshow = threeBandImage(ds,bands = ['red', 'green', 'blue'], figsize=figsize, time = time)
    fig = pyplot.figure(figsize = figsize)
    pyplot.imshow(img_toshow)
    ax = pyplot.gca()
    title_string = "IMG " + str(count)
    title_string = title_string + " --> " + str(ds.time[time].values).split('T')[0]
    ax.set_title(title_string, fontweight = 'bold', fontsize = 16)
    #ax.set_xticklabels(ds.x.values)
    #ax.set_yticklabels(ds.y.values)
    #ax.set_xlabel('Easting', fontweight = 'bold')
    #ax.set_ylabel('Northing', fontweight = 'bold')
    return True

def plot_labeled_rgb_tick(ds, time, count=1, figsize = [8,8]):
    """
        plot_labeled_rgb 
        1. ds = dataset (from a datacube xarray)
        2. time is the obeservation acq date to select the observation to be plotted
        3. count is an integer to display , not that important
    """
    
    img_toshow = threeBandImage(ds,bands = ['red', 'green', 'blue'], figsize=figsize, time = time)
    fig = pyplot.figure(figsize = figsize)
    pyplot.imshow(img_toshow)
    ax = pyplot.gca()
    title_string = "IMG " + str(count)
    title_string = title_string + " --> " + str(ds.time[time].values).split('T')[0]
    ax.set_title(title_string, fontweight = 'bold', fontsize = 16)
    ax.set_xticklabels(ds.x.values)
    ax.set_yticklabels(ds.y.values)
    ax.set_xlabel('Easting', fontweight = 'bold')
    ax.set_ylabel('Northing', fontweight = 'bold')
    return True

