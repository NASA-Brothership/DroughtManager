from flask import jsonify
from app.plants import get_plant_drought_risk
from app.wbi import get_mean_wbi

def analyze_drought(data_input):
    crop_type = data_input.get('crop_type')
    latitude = data_input.get('latitude')
    longitude = data_input.get('longitude')
    radius_km = data_input.get('radius_km')

    # Call the function to get drought risk from plants.py
    plant_drought_risk = get_plant_drought_risk(crop_type)

    # Call the function to get water balance data from wbi.py
    wbi_mean = get_mean_wbi(latitude, longitude, radius_km)

    # Combine the results into a single output
    output = {
        "drought_risk": plant_drought_risk.value,  # Drought risk rating for the crop
        "wbi_mean": wbi_mean  # Water Balance Index data
    }

    return jsonify(output)
