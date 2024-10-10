import base64
import datetime
import os

import requests


class MeteomaticsInterface:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.token_url = 'https://login.meteomatics.com/api/v1/token'
        self.api_url = 'https://api.meteomatics.com'
        self.token = None

    def _get_token(self):
        credentials = f"{self.username}:{self.password}".encode("utf-8")
        auth_header = base64.b64encode(credentials).decode("utf-8")

        response = requests.get(
            self.token_url,
            headers={
                'Authorization': f'Basic {auth_header}'
            }
        )

        if response.status_code == 200:
            self.token = response.json().get('access_token')
        else:
            raise Exception(f'Error while requesting token: {response.status_code} - {response.text}')

    def get_precipitation(self, latitude: float, longitude: float, start_datetime: datetime.datetime,  end_datetime: datetime.datetime):
        if not self.token:
            self._get_token()

        start_datetime = start_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_datetime = end_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
        url = f"{self.api_url}/{start_datetime}--{end_datetime}:P1D/precip_24h:mm/{latitude},{longitude}/json?model=mix"

        # Requests preciptation data
        response = requests.get(
            url,
            headers={
                'Authorization': f'Bearer {self.token}'
            }
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error while requesting preciptation data: {response.status_code} - {response.text}")

    def get_precipitation_sum(self, data):
        # Extract coordinate list
        coordinates = data['data'][0]['coordinates'][0]['dates']
        
        # Extract preciptation values
        preciptation_values = [item['value'] for item in coordinates]
        
        return sum(preciptation_values)
