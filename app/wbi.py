import datetime
import json
import logging

from flask import Blueprint, jsonify, request
import ee

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

wbi_bp = Blueprint('wbi', __name__)

# Load private key JSON
with open('./private-key.json') as f:
    private_key = json.load(f)

# Initialize Earth Engine with the private key
def initialize_earth_engine():
    credentials = ee.ServiceAccountCredentials(private_key['client_email'], './private-key.json')
    ee.Initialize(credentials)

initialize_earth_engine()

def get_dates():
    """Get today's date and start date for the last year."""
    today = datetime.date.today()
    start_date = (today - datetime.timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')
    return start_date, end_date

def create_region(latitude, longitude, radius_km):
    """Create a region around the given latitude and longitude."""
    point = ee.Geometry.Point([longitude, latitude])
    return point.buffer(radius_km * 1000)  # Convert km to meters

def fetch_wbi_data(region, start_date, end_date):
    """Fetch WBI data using Earth Engine."""
    ET = (ee.ImageCollection('MODIS/061/MOD16A2GF')
          .filterDate(start_date, end_date)
          .select('ET')
          .mean()
          .clip(region))

    precipitation = (ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY')
                     .filterDate(start_date, end_date)
                     .select('precipitation')
                     .mean()
                     .clip(region))

    return ET.subtract(precipitation).rename('WBI')

def get_mean_wbi(latitude, longitude, radius_km):

    start_date, end_date = get_dates()
    region = create_region(latitude, longitude, radius_km)
    
    water_balance_index = fetch_wbi_data(region, start_date, end_date)

    water_balance_index_mean = water_balance_index.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=region,
        scale=5566,
        maxPixels=1e9
    ).getInfo()

    # Print the value to the console
    logger.debug("Water Balance Index Mean: %s", water_balance_index_mean)

    # Include the mean value
    return water_balance_index_mean['WBI']

@wbi_bp.route('/water-balance-map-tile', methods=['GET'])
def get_wbi_url():
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)

    if latitude is None or longitude is None:
        return jsonify({"error": "Latitude and longitude must be provided"}), 400
    
    start_date, end_date = get_dates()
    region = create_region(latitude, longitude, radius_km=100)  # Using a fixed 100 km buffer for map tiles
    
    water_balance_index = fetch_wbi_data(region, start_date, end_date)

    water_balance_index_stats = water_balance_index.reduceRegion(
        reducer=ee.Reducer.percentile([2, 98]),
        geometry=region,
        scale=5566,
        maxPixels=1e9
    ).getInfo()

    vis_params = {
        'min': water_balance_index_stats['WBI_p2'],
        'max': water_balance_index_stats['WBI_p98'],
        'palette': ['red', 'white', 'blue']
    }

    map_id_object = water_balance_index.getMapId(vis_params)
    tile_url = map_id_object['tile_fetcher'].url_format

    return jsonify({'url': tile_url})
