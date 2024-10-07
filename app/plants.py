from flask import Blueprint, jsonify
from crops.code_enums import DroughtRisk
import crops.plants as plants

plants_bp = Blueprint('plants', __name__)

@plants_bp.route('/plants', methods=['GET'])
def get_plants():
    return jsonify(list(plants.all_plants))

# Function to get drought risk category for a crop
def get_plant_drought_risk(crop: str) -> DroughtRisk:
    # Check for crop in each drought risk category
    print(crop)
    if crop in plants.very_low_drought_risk:
        return DroughtRisk.VERY_LOW
    elif crop in plants.low_drought_risk:
        return DroughtRisk.LOW
    elif crop in plants.medium_drought_risk:
        return DroughtRisk.MEDIUM
    elif crop in plants.high_drought_risk:
        return DroughtRisk.HIGH
    elif crop in plants.very_high_drought_risk:
        return DroughtRisk.VERY_HIGH