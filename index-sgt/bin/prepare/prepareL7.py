
"""
USARD Prepare Script - WIP!

https://landsat.usgs.gov/ard
"""
# coding: utf-8
from pathlib import Path
import os
from xml.etree import ElementTree
from osgeo import osr
import dateutil
from dateutil import parser
from datetime import timedelta
import uuid
import logging
import re
import boto3
import datacube
from datacube.scripts.dataset import create_dataset, parse_match_rules_options
from datacube.utils import changes

MTL_PAIRS_RE = re.compile(r'(\w+)\s=\s(.*)')

bands_ls7_usard = [('1', 'blue'),
             ('2', 'green'),
             ('3', 'red'),
             ('4', 'nir'),
             ('5', 'swir1'),
             ('6', 'swir2'),
             ('7', 'therm'),
             ('8', 'pixel_qa')]

band_file_map = {
                  'blue' : 'sr_band1',
                  'green' : 'sr_band2',
                  'red' : 'sr_band3',
                  'nir' : 'sr_band4',
                  'swir1' : 'sr_band5',
                  'swir2' : 'sr_band7',
                  'therm' : 'bt_band6',
                  'pixel_qa' : 'pixel_qa',
                }

def _parse_value(s):
    s = s.strip('"')
    for parser in [int, float]:
        try:
            return parser(s)
        except ValueError:
            pass
    return s


def _parse_group(lines):
    tree = {}
    for line in lines:
        match = MTL_PAIRS_RE.findall(line)
        if match:
            key, value = match[0]
            if key == 'GROUP':
                tree[value] = _parse_group(lines)
            elif key == 'END_GROUP':
                break
            else:
                tree[key] = _parse_value(value)
    return tree


def get_geo_ref_points(info):
    return {
        'ul': {'x': info['CORNER_UL_PROJECTION_X_PRODUCT'], 'y': info['CORNER_UL_PROJECTION_Y_PRODUCT']},
        'ur': {'x': info['CORNER_UR_PROJECTION_X_PRODUCT'], 'y': info['CORNER_UR_PROJECTION_Y_PRODUCT']},
        'll': {'x': info['CORNER_LL_PROJECTION_X_PRODUCT'], 'y': info['CORNER_LL_PROJECTION_Y_PRODUCT']},
        'lr': {'x': info['CORNER_LR_PROJECTION_X_PRODUCT'], 'y': info['CORNER_LR_PROJECTION_Y_PRODUCT']},
    }


def get_coords(geo_ref_points, spatial_ref):
    t = osr.CoordinateTransformation(spatial_ref, spatial_ref.CloneGeogCS())

    def transform(p):
        lon, lat, z = t.TransformPoint(p['x'], p['y'])
        return {'lon': lon, 'lat': lat}

    return {key: transform(p) for key, p in geo_ref_points.items()}


def satellite_ref(sat):
    """
    To load the band_names for referencing either LANDSAT8  USARD
    """
    if sat == 'LANDSAT_8' or sat == 'LANDSAT_7' or sat == 'LANDSAT_5':
        sat_img = bands_ls7_usard
        prod_type = 'USARD'
    else:
        raise ValueError('Satellite data Not Supported')
    return sat_img, prod_type


def format_obj_key(obj_key):
    obj_key = '/'.join(obj_key.split("/")[:-1])
    return obj_key


def get_s3_url(bucket_name, obj_key):
    return 's3://{bucket_name}/{obj_key}'.format(
        bucket_name=bucket_name, obj_key=obj_key)


def absolutify_paths(doc, bucket_name, obj_key):
    objt_key = format_obj_key(obj_key)
    for band in doc['image']['bands'].values():
        band['path'] = get_s3_url(bucket_name, objt_key + '/'+band['path'])
    return doc

def get_band_filenames(xmldoc):
    band_dict = {}
    # print(type(xmldoc))
    bands = xmldoc.find('.//bands')
    for bandxml in bands:
        band_name = (bandxml.get('name'))
        print(band_name)
        file = bandxml.find('.//file_name')
        band_file_name = file.text
        band_file_name = band_file_name.replace("tif", "TIF")
        band_file_name = band_file_name.replace("L1TP", "L2SP")
        print("BANDFILE =", band_file_name)
        band_dict[band_name] = band_file_name
    return (band_dict)

def make_xml_doc(xmlstring, bucket_name, object_key):

    xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)
    doc = ElementTree.fromstring(xmlstring)

    satellite = doc.find('.//satellite').text

    instrument = doc.find('.//instrument').text
    # hardcode for now - the util changes routine is very unkind, unforgiving
    ## instrument = 'OLI_TIRS'
    ## instrument = 'TM'

    print("TONY")
    print(satellite, instrument)

    # add cloud cover and fill parameters to metadata_doc
    # cloud_cover = doc.find('.//cloud_cover').text
    # fill = doc.find('.//fill').text

    # other params like cloud_shadow, snow_ice, tile_grid, orientation_angle are also available

    acquisition_date = doc.find('.//acquisition_date').text
    scene_center_time = doc.find('.//scene_center_time').text
    center_dt = acquisition_date + " " + scene_center_time
    level = doc.find('.//product_id').text.split('_')[1]
    lpgs_metadata_file = doc.find('.//lpgs_metadata_file').text
    start_time = center_dt
    end_time = center_dt
    images, product_type = satellite_ref(satellite)
    image_path = doc.find('.//product_id').text
    # print(image_path)
    # hardcode the cs_code from esri since gdalinfo just gave the name
    """
	should this not be in the gdalinfo spatial data?
	and/or in the xml file
    """
    # cs_code = '102008'
    cs_code = '5072'
    label = 'USARD_SCENE_ID_TONY_TBD'
    # spatial_ref = 'EPSG:' + cs_code
    # spatial_ref = 'esri:' + cs_code
    spatial_ref = 'epsg:' + cs_code
    # spatial_ref = osr.SpatialReference()
    # spatial_ref.ImportFromEPSG(cs_code)
    west = doc.find('.//bounding_coordinates/west').text
    east = doc.find('.//bounding_coordinates/east').text
    north = doc.find('.//bounding_coordinates/north').text
    south = doc.find('.//bounding_coordinates/south').text

    coord = {
          'ul':
             {'lon': west,
              'lat': north},
          'ur':
             {'lon': east,
              'lat': north},
          'lr':
             {'lon': east,
              'lat': south},
          'll':
             {'lon': west,
              'lat': south}}
    # print(coord)
    # print(west,north)
    # print(east,south)

    projection_parameters = doc.find('.//projection_information')
    for corner_point in projection_parameters.findall('corner_point'):
        if corner_point.attrib['location'] in 'UL':
           # print(corner_point.attrib['location'])
           # print(corner_point.attrib['y'])
           # print(corner_point.attrib['x'])
           westx = corner_point.attrib['x']
           northy = corner_point.attrib['y']
        if corner_point.attrib['location'] in 'LR':
           # print(corner_point.attrib['location'])
           # print(corner_point.attrib['y'])
           # print(corner_point.attrib['x'])
           eastx = corner_point.attrib['x']
           southy = corner_point.attrib['y']

    deltax = float(westx) - float(eastx)
    deltay = float(northy) - float(southy)

    dpx = deltax / 30
    dpy = deltay / 30

    westxf = float(westx) * 1.0
    eastxf = float(eastx) * 1.0
    northyf = float(northy) * 1.0
    southyf = float(southy) * 1.0

    # print(deltax, dpx, deltay, dpy)
    geo_ref_points = {
          'ul':
             {'x': westxf,
              'y': northyf},
          'ur':
             {'x': eastxf,
              'y': northyf},
          'lr':
             {'x': eastxf,
              'y': southyf},
          'll':
             {'x': westxf,
              'y': southyf}}
        
    print(images)
    band_dict =  get_band_filenames(doc)
    print(band_dict)
    for i in images:
        print("TONY i = ", i[1])
        print("band map = ", band_file_map[i[1]])
    docdict = {
        'id': str(uuid.uuid4()),
        # 'cloud_cover': cloud_cover,
        # 'fill': fill,
        'processing_level': str(level),
        'product_type': product_type,
        'creation_dt': acquisition_date,
        'platform': {'code': satellite},
        'instrument': {'name': instrument},
        'extent': {
            'from_dt': str(start_time),
            'to_dt': str(end_time),
            'center_dt': str(center_dt),
            'coord': coord,
        },
        'format': {'name': 'GeoTiff'},
        'grid_spatial': {
            'projection': {
                'geo_ref_points': geo_ref_points,
                'spatial_reference': spatial_ref,
            }
        },
        'image': {
            'bands': {
                image[1]: {
                    'path': band_dict[band_file_map[image[1]]],
                    'layer': 1,
                } for image in images
            }
        },

        'lineage': {'source_datasets': {}}
    }

    print (docdict)
    print("TONY make xml")
    docdict = absolutify_paths(docdict, bucket_name, object_key)
    # print (docdict)
    # print("TONY")
    return docdict



def get_metadata_docs(bucket_name, prefix):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    logging.info("Bucket : %s", bucket_name)
    for obj in bucket.objects.filter(Prefix=prefix):
        if obj.key.endswith('.xml'):
            obj_key = obj.key
            logging.info("Processing %s", obj_key)
            raw_string = obj.get()['Body'].read().decode('utf8')
            # print(raw_string)
            metadata_doc = make_xml_doc(raw_string,bucket_name, obj_key)
            # print(metadata_doc)
            # TONY
            yield obj_key, metadata_doc


def make_rules(index, product):
    # all_product_names = [prod.name for prod in index.products.get_all()]
    # rules = parse_match_rules_options(index, None, all_product_names, True)

    # all_product_names = ['ls8_level1']

    #all_product_names = ['landsat_5_USARD']

    all_product_names = [product]
    rules = parse_match_rules_options(index, None, all_product_names,True)
    return rules


def add_dataset(doc, uri, rules, index):
    dataset = create_dataset(doc, uri, rules)

    try:
        index.datasets.add(dataset, sources_policy='skip')
    except changes.DocumentMismatchError as e:
        index.datasets.update(dataset, {tuple(): changes.allow_any})
    return uri

def determine_product_from_prefix(prefix):

    product = 'l5_kline'

    if 'L05' in prefix:
        product = 'l5_kline'
    if 'L07' in prefix:
        product = 'l7_kline'
    if 'L5' in prefix:
        product = 'l5_kline'
    if 'L7' in prefix:
        product = 'l7_kline'

    print("DETERMINE product = ", product)
    return(product)

def add_datacube_dataset(bucket_name, config, prefix):
    dc = datacube.Datacube(config=config)
    index = dc.index
    product = determine_product_from_prefix(prefix)
    rules = make_rules(index, product)
    # print(type(rules))
    # print(rules)
    for metadata_path, metadata_doc in get_metadata_docs(bucket_name, prefix):
        uri = get_s3_url(bucket_name, metadata_path)
        add_dataset(metadata_doc, uri, rules, index)
        logging.info("Indexing %s", metadata_path)



