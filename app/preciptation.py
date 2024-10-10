import os
import datetime
from utils.meteomatics_interface import MeteomaticsInterface
from utils.enums import DroughtRiskValue


def get_precipitation_sum(latitude: float, longitude: float, days_ahead=14) -> float:

    username = os.getenv('METEOMATICS_USERNAME')
    password = os.getenv('METEOMATICS_PASSWORD')

    start = datetime.datetime.now()
    end = start + datetime.timedelta(days=days_ahead)

    meteomatics_api = MeteomaticsInterface(username, password)

    weather_data = meteomatics_api.get_precipitation(latitude, longitude, start, end)
    precipitation_sum = meteomatics_api.get_precipitation_sum(weather_data)

    return precipitation_sum


# Preciptation related risks
def get_preciptation_risk_score(precipitation_sum: float) -> DroughtRiskValue:
    if precipitation_sum <= 10:
        preciptation_risk_score = DroughtRiskValue.VERY_HIGH
    elif 10 < precipitation_sum < 30:
        preciptation_risk_score = DroughtRiskValue.HIGH
    elif 30 < precipitation_sum < 60:
        preciptation_risk_score = DroughtRiskValue.HIGH
    elif 60 < precipitation_sum < 90:
        preciptation_risk_score = DroughtRiskValue.LOW
    elif precipitation_sum > 90:
        preciptation_risk_score = DroughtRiskValue.VERY_LOW

    return preciptation_risk_score
