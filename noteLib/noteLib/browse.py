""" Create cogs from tif gdal """
import sys
import os
import time
import subprocess
from osgeo import gdal


def delete(path):
    """Delete a file.

    Args:
        path (str): Full path to file

    Returns:
        bool: True if the file was deleted, False if not (with message logged)
    """

    try:
        os.remove(path)
    except FileNotFoundError:
        pass
    except Exception as e:
        logger.error("Exception deleting file:{}".format(path))
        logger.error(e)
        return False
    return True


def exists(path):
    """Determine if a file exists.

    Args:
        path (str): Full path to file

    Returns:
        bool: True if the file exists, False if not
    """

    return os.path.exists(path) and os.path.isfile(path)



def run_command(cmd, verbose=False):
    if verbose:
        print(cmd)
    result = os.system(cmd)
    if result != 0:
        raise Exception('command "%s" failed with code %d.' % (cmd, result))



def get_min_max(raster):
# open raster and choose band to find min, max
# raster = r'C:\path\to\your\geotiff.tif'
    gtif = gdal.Open(raster)
    srcband = gtif.GetRasterBand(1)

    # Get raster statistics
    stats = srcband.GetStatistics(True, True)

    # Print the min, max, mean, stdev based on stats index
    print ("[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % (
        stats[0], stats[1], stats[2], stats[3]))
    return stats[0],stats[1]



def build_browse(rgb_files, out_file):
    """
        builds a browse file
    """

    red_amplify = 210
    green_amplify = 200
    blue_amplify = 140
    
    browse = rgb_files[0][0:-13] + '_browse.png'
    rgb_wrk=[]
    garbage = []
    for the_file in rgb_files:
        print(the_file)
        wrk_file = the_file.rsplit('.', 1)[0] + '_wrk.tif'
        garbage.append(wrk_file)
        browse_file = the_file.rsplit('.', 1)[0] + '_browse.jpg'
        tmp_file = the_file.rsplit('.', 1)[0] + '_wrk.IMD'
        # garbage.append(tmp_file)
        rgb_file = the_file.rsplit('.', 1)[0] + '_wrkrgb.tif'
        prgb_file = the_file.rsplit('.', 1)[0] + '_wrkprgb.tif'
        print(wrk_file)
        rgb_wrk.append(wrk_file)
        run_command(
            'gdal_translate %s %s -of Gtiff -outsize 10% 10% -scale ' % (
            the_file,
            wrk_file))
        min,max = get_min_max(wrk_file)

        run_command(
            'gdal_translate %s %s -of Gtiff -scale %s %s 0 65535 -exponent 0.5' % 
            (wrk_file, tmp_file, min, max))

        run_command('mv %s %s' % (tmp_file, wrk_file))

        print("hello THERE")

    
    run_command(
        'gdal_merge.py -o %s -separate %s %s %s -co PHOTOMETRIC=RGB -co COMPRESS=DEFLATE' %
        (rgb_file, rgb_wrk[0], rgb_wrk[1], rgb_wrk[2]))

    run_command(
        'gdalwarp -of GTiff -t_srs EPSG:4326 %s %s' %
        (rgb_file, prgb_file))

    run_command(
        'convert -modulate %s,%s,%s -transparent black %s %s' %
         (red_amplify, green_amplify, blue_amplify, prgb_file, out_file))

    run_command(
        'cp  %s %s' %
         (out_file, browse))

    if exists(prgb_file):
        delete(prgb_file)
    if exists(rgb_file):
        delete(rgb_file)

    for fid in garbage:
        delete(fid)
            
    for fid in rgb_wrk:
        delete(fid)

    return browse

