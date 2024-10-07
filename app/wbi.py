from flask import Blueprint, jsonify, request
import ee
import json

wbi_bp = Blueprint('wbi', __name__)

# Load private key JSON
with open('./private-key.json') as f:
    private_key = json.load(f)

# Initialize Earth Engine with the private key
def initialize_earth_engine():
    credentials = ee.ServiceAccountCredentials(private_key['client_email'], './private-key.json')
    ee.Initialize(credentials)
    print('Authenticated with Earth Engine')

initialize_earth_engine()

# Endpoint to get water balance index data
@wbi_bp.route('/mean-water-balance', methods=['GET'])
def get_mean_wbi():
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)
    radius_km = request.args.get('radius_km', type=float)


@wbi_bp.route('/water-balance-map-tile', methods=['GET'])
def get_wbi_url():
    latitude = request.args.get('latitude', type=float)
    longitude = request.args.get('longitude', type=float)

    if latitude is None or longitude is None:
        return jsonify({"error": "Latitude and longitude must be provided"}), 400

    # Define a point around which to display the map (latitude, longitude)
    point = ee.Geometry.Point([longitude, latitude])

    # Create a region around the point (e.g., 100 km buffer)
    region = point.buffer(100000)  # 100 km buffer around the point

    start_date = '2023-10-03'
    end_date = '2024-10-03'

    # Fetch ET and precipitation data
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

    # Calculate the Water Balance Index (WBI)
    water_balance_index = ET.subtract(precipitation).rename('WBI')

    water_balance_index_stats = water_balance_index.reduceRegion(
        reducer=ee.Reducer.percentile([2, 98]),  # Calculate min and max
        geometry=region,
        scale=5566,  # Adjust scale as needed (in meters)
        maxPixels=1e9  # Increase if needed
    ).getInfo()

    vis_params = {
        'min': water_balance_index_stats['WBI_p2'],  # Minimum value of WBI (in mm/day)
        'max': water_balance_index_stats['WBI_p98'],  # Maximum value of WBI (in mm/day)
        'palette': ['red', 'white', 'blue']  # Palette for low to high WBI values
    }

    # Use getMapId to obtain mapId and token
    map_id_object = ET.getMapId(vis_params)
    tile_url = map_id_object['tile_fetcher'].url_format

    # Respond with the tile URL
    return jsonify({'url': tile_url})
