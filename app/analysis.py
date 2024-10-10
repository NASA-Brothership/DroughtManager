from app.plants import get_plant_drought_risk
from app.wbi import get_mean_wbi, get_wbi_risk
from app.preciptation import get_precipitation_sum, get_preciptation_risk_score
from utils.enums import DroughtRisk, DroughtRiskValue, Recommendation, PlantingPeriod

from flask import jsonify

def get_mean_risk(plant_drought_risk: DroughtRiskValue,
                  ndmi_risk_score: DroughtRiskValue,
                  wbi_risk_score: DroughtRiskValue,
                  preciptation_risk_score: DroughtRiskValue) -> float:

    return 0.3 * plant_drought_risk.value + \
           0.25 * ndmi_risk_score.value + \
           0.25 * wbi_risk_score.value + \
           0.20 * preciptation_risk_score.value


def get_recommendation(mean_risk, is_irrigated, planting_period, existing_crops) -> Recommendation:
    if existing_crops == 'yes':
        if mean_risk <= 0.2:
            return Recommendation.VERY_LOW_RISK_WITH_CROPS
        elif mean_risk > 0.2 and mean_risk <= 0.4:
            return Recommendation.LOW_RISK_WITH_CROPS
        elif mean_risk > 0.4 and mean_risk <= 0.6:
            if is_irrigated == 'yes':
                return Recommendation.MEDIUM_RISK_WITH_CROPS_WITH_IRRIGATION
            else:
                return Recommendation.MEDIUM_RISK_WITH_CROPS_WITH_IRRIGATION
        elif mean_risk > 0.6 and mean_risk <= 0.8:
            if is_irrigated == 'yes':
                return Recommendation.HIGH_RISK_WITH_CROPS_WITH_IRRIGATION
            else:
                return Recommendation.HIGH_RISK_WITH_CROPS_WITHOUT_IRRIGATION
        elif mean_risk > 0.8:
            if is_irrigated == 'yes':
                return Recommendation.VERY_HIGH_RISK_WITH_CROPS_WITH_IRRIGATION
            else:
                return Recommendation.VERY_HIGH_RISK_WITH_CROPS_WITHOUT_IRRIGATION
    else:
        if is_irrigated == 'yes' and planting_period in (PlantingPeriod.BEFORE.value, PlantingPeriod.AFTER.value):
            if mean_risk <= 0.4:
                return Recommendation.LOW_RISK_WITHOUT_CROPS_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD
            if mean_risk > 0.4 and mean_risk <= 0.6:
                return Recommendation.MEDIUM_RISK_WITHOUT_CROPS_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD
            if mean_risk > 0.6:
                return Recommendation.HIGH_RISK_WITHOUT_CROPS_WITH_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD
        elif is_irrigated == 'yes' and planting_period == PlantingPeriod.DURING.value:
            if mean_risk <= 0.6:
                return Recommendation.LOW_RISK_WITHOUT_CROPS_WITH_IRRIGATION_DURING_PLANTING_PERIOD
            if mean_risk > 0.6:
                return Recommendation.HIGH_RISK_WITHOUT_CROPS_WITH_IRRIGATION_DURING_PLANTING_PERIOD
        if is_irrigated == "no" and planting_period in (PlantingPeriod.BEFORE.value, PlantingPeriod.AFTER.value):
            if mean_risk <= 0.4:
                return Recommendation.LOW_RISK_WITHOUT_CROPS_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD
            if mean_risk > 0.4 and mean_risk <= 0.6:
                return Recommendation.MEDIUM_RISK_WITHOUT_CROPS_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD
            if mean_risk > 0.6:
                return Recommendation.HIGH_RISK_WITHOUT_CROPS_WITHOUT_IRRIGATION_BEFORE_AFTER_PLANTING_PERIOD
        elif is_irrigated == "no" and planting_period == PlantingPeriod.DURING.value:
            if mean_risk <= 0.4:
                return Recommendation.LOW_RISK_WITHOUT_CROPS_WITHOUT_IRRIGATION_DURING_PLANTING_PERIOD
            if mean_risk > 0.4:
                return Recommendation.HIGH_RISK_WITHOUT_CROPS_WITHOUT_IRRIGATION_DURING_PLANTING_PERIOD


def get_drought_risk(mean_risk: float) -> DroughtRisk:
    if mean_risk <= 0.2:
        return DroughtRisk.VERY_LOW
    elif mean_risk <= 0.4:
        return DroughtRisk.LOW
    elif mean_risk <= 0.6:
        return DroughtRisk.MEDIUM
    elif mean_risk <= 0.8:
        return DroughtRisk.HIGH
    else:
        return DroughtRisk.VERY_HIGH


def analyze_drought(data_input:dict) -> DroughtRisk:
    crop_type = data_input.get('crop_type')
    latitude = data_input.get('latitude')
    longitude = data_input.get('longitude')
    radius_km = data_input.get('radius_km')
    is_irrigated = data_input.get('is_irrigated')
    planting_period = data_input.get('planting_period')
    existing_crops = data_input.get('existing_crops')

    # Call the function to get plant drought risk from plants.py
    plant_drought_risk_score = get_plant_drought_risk(crop_type)

    # Call the function to get mean ndmi data from satellite.py
    ndmi_risk_score = DroughtRiskValue.MEDIUM

    # Call the function to get water balance data from wbi.py
    mean_wbi = get_mean_wbi(latitude, longitude, radius_km)
    wbi_risk_score = get_wbi_risk(mean_wbi)

    # Call the function to get preciptation forecast data from preciptation.py
    precipitation_sum = get_precipitation_sum(latitude, longitude)
    preciptation_risk_score = get_preciptation_risk_score(precipitation_sum)

    mean_risk = get_mean_risk(plant_drought_risk_score,
                  ndmi_risk_score,
                  wbi_risk_score,
                  preciptation_risk_score)

    drought_risk = get_drought_risk(mean_risk)

    recommendation = get_recommendation(mean_risk, is_irrigated, planting_period, existing_crops)

    # Combine the results into a single output
    output = {
        "drought_risk": drought_risk.value,  # Drought risk for the crop
        "recommendation": recommendation.value
    }

    return jsonify(output)





