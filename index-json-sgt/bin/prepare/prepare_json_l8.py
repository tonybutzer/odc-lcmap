
"""
USARD Prepare Script - WIP!

SGT Cloud staged data 

This script scrapes and AWS S3 Bucket and Prefix recursively and:

* 1. locates the json metadata
* 2. creates a json blob (binary) for each metadata file 
* 3. loads these into the postgresql database as a JSONB object

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

bands_ls8_usard = [('1', 'sr_band1'),
             ('2', 'blue'),
             ('3', 'green'),
             ('4', 'red'),
             ('5', 'nir'),
             ('6', 'swir1'),
             ('7', 'swir2'),
             ('8', 'therm'),
             ('9', 'pixel_qa')]

band_file_map = {
                  'sr_band1' : 'sr_band1',
                  'blue' : 'sr_band2',
                  'green' : 'sr_band3',
                  'red' : 'sr_band4',
                  'nir' : 'sr_band5',
                  'swir1' : 'sr_band6',
                  'swir2' : 'sr_band7',
                  'therm' : 'bt_band10',
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
    """ extracts the geo bounding box from the xml metadata and returns a dict {ul,ur,ll,lr} """
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
    load the band_names for referencing LANDSAT8  USARD
    """
    if sat == 'LANDSAT_8':
        sat_img = bands_ls8_usard
        prod_type = 'USARD'
    else:
        raise ValueError('Satellite data Not Supported')
    return sat_img, prod_type


def format_obj_key(obj_key):
    """ return a prefix sperated by / for use as an AWS prefix """
    obj_key = '/'.join(obj_key.split("/")[:-1])
    return obj_key


def get_s3_url(bucket_name, obj_key):
    """ return an S3 suitable url such as: s3://{bucket_name}/{obj_key} """
    return 's3://{bucket_name}/{obj_key}'.format(
        bucket_name=bucket_name, obj_key=obj_key)



def get_band_filenames(xmldoc):
    """ parse the xml metadata and return the band names in a dict """
    band_dict = {}
    # print(type(xmldoc))
    bands = xmldoc.find('.//bands')
    for bandxml in bands:
        band_name = (bandxml.get('name'))
        # print(band_name)
        file = bandxml.find('.//file_name')
        band_file_name = file.text
        band_file_name = band_file_name.replace("tif", "TIF")
        band_file_name = band_file_name.replace("L1TP", "L2SP")
        # print(band_file_name)
        band_dict[band_name] = band_file_name
    return (band_dict)


from prepare.json_meta_blob import MetaBlob
def make_doc_from_json(raw_json, bucket_name, object_key):
    """ creates a json blob called a doc for insetion into the database index

    Args:
        **raw_json**

        **bucket_name**

        **object_key** (str): AWS S3 key to the json file name

    """

    # print(object_key)

    s3prefix = '/'.join(object_key.split("/")[:-1])
    s3path = 's3://{bucket_name}/{s3prefix}'.format(
        bucket_name=bucket_name, s3prefix=s3prefix)

    # print(s3path)

    meta_blob = MetaBlob(raw_json)

    level = meta_blob.product_id.split('_')[1]
    images, product_type = satellite_ref(meta_blob.satellite)
    center_dt = meta_blob.acquisition_date + " " + meta_blob.scene_center_time
    start_time = center_dt
    end_time = center_dt

    # HARDCODE - please fix this Tony
    cs_code = '5072'
    spatial_ref = 'epsg:' + cs_code

    
    westxf = float(meta_blob.westx) * 1.0
    eastxf = float(meta_blob.eastx) * 1.0
    northyf = float(meta_blob.northy) * 1.0
    southyf = float(meta_blob.southy) * 1.0

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
        
    docdict = {
        'id': str(uuid.uuid4()),
        'processing_level': str(level),
        'product_type': product_type,
        'creation_dt': meta_blob.acquisition_date,
        'platform': {'code': meta_blob.satellite},
        'instrument': {'name': meta_blob.instrument},
        'extent': {
            'from_dt': str(start_time),
            'to_dt': str(end_time),
            'center_dt': str(center_dt),
            'coord': meta_blob.coord,
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
                    'path': s3path + '/' + meta_blob.file_dict[band_file_map[image[1]]],
                    'layer': 1,
                } for image in images
            }
        },

        'lineage': {'source_datasets': {}}
    }
    # print (docdict)
    # print("TONY make xml")
    # docdict = absolutify_paths(docdict, bucket_name, object_key)
    # print (docdict)
    # print("TONY")
    return docdict


    exit()

    pass

def make_xml_doc(xmlstring, bucket_name, object_key):
    """ principle function to convert xml metadata into a JSON doc 

        need to document each section here:
    """

    xmlstring = re.sub(r'\sxmlns="[^"]+"', '', xmlstring, count=1)
    doc = ElementTree.fromstring(xmlstring)

    satellite = doc.find('.//satellite').text

    # instrument = doc.find('.//instrument').text
    # hardcode for now - the util changes routine is very unkind, unforgiving
    instrument = 'OLI_TIRS'

    # print("TONY")
    # print(satellite, instrument)

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
        
    # print(images)
    band_dict =  get_band_filenames(doc)
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
                    'path': s3path + '/' + meta_blob.band_dict[band_file_map[image[1]]],
                    'layer': 1,
                } for image in images
            }
        },

        'lineage': {'source_datasets': {}}
    }
    # print (docdict)
    # print("TONY make xml")
    docdict = absolutify_paths(docdict, bucket_name, object_key)
    # print (docdict)
    # print("TONY")
    return docdict



def get_metadata_docs_json(bucket_name, prefix):
    """ GENERATOR: recursively find the metadata for each scene/tile

    Args:
        **bucket_name** (str): AWS S3 Bucket Name - example lsaa-staging-cog

        **prefix** (str): AWS prefix within the bucket to start the recursive search for .json file = example L8
    """

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    logging.info("Bucket : %s", bucket_name)
    for obj in bucket.objects.filter(Prefix=prefix):
        if obj.key.endswith('.json') and not "ANG" in obj.key and not "MTL" in obj.key:
            obj_key = obj.key
            logging.info("Processing %s", obj_key)
            raw_string = obj.get()['Body'].read().decode('utf8')
            metadata_doc = make_doc_from_json(raw_string, bucket_name, obj_key)

            yield obj_key, metadata_doc


def make_rules(index):
    """ I have never understood what this function does and it may have been axed by ODC developers """
    # all_product_names = [prod.name for prod in index.products.get_all()]
    # rules = parse_match_rules_options(index, None, all_product_names, True)

    # all_product_names = ['ls8_level1']

    all_product_names = ['l8_kline']
    rules = parse_match_rules_options(index, None, all_product_names,True)
    return rules


def add_dataset(doc, uri, rules, index):
    """ add a single dataset to the postgresql index 

        1. call create_dataset(datacube) to build the dataset object with the newly created json doc
        2. call index.datasets.add with the dataset document object to populate the DB

    """

    dataset = create_dataset(doc, uri, rules)

    try:
        index.datasets.add(dataset, sources_policy='skip')
    except changes.DocumentMismatchError as e:
        index.datasets.update(dataset, {tuple(): changes.allow_any})
    return uri


def add_datacube_dataset(bucket_name, config, prefix):
    """ Main loop function to traverse the bucket-->prefix tree and index each dataset

    for each .json metadata file:

    * extract the metadata and 
    * create a doc (dict json blob for the postgresql database)

    Args:
        **bucket_name** (str): AWS S3 Bucket Name - example lsaa-staging-cog

        config (str): A datacube config file to over-ride the one in your home directory

        **prefix** (str): AWS prefix within the bucket to start the recursive search for .json file = example L8

    Returns:
        ABSOLUTELY_NOTHING

    """

    dc = datacube.Datacube(config=config)
    index = dc.index
    rules = make_rules(index)
    # print(type(rules))
    # print(rules)
    for metadata_path, metadata_doc in get_metadata_docs_json(bucket_name, prefix):
        uri = get_s3_url(bucket_name, metadata_path)
        add_dataset(metadata_doc, uri, rules, index)
        logging.info("Indexing %s", metadata_path)



