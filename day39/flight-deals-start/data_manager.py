#This class is responsible for talking to the Google Sheet.
import requests
import os
from typing import List

SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")


class DataManager:

    def __init__(self):
        self.endpoint = "https://api.sheety.co/bd229125e44ca58de9a047a04a1b3d2d/flightDeals/deals"
        self.headers = {
            "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
            "Content-Type": "application/json"
        }

    def change_name(self):
        params = {
            "deal": {
                "city": "moscow",
                "iataCode": "PAR",
                "lowestPrice": 2000
            }
        }

        response = requests.put(url=self.endpoint, json=params, headers=self.headers)
        print(response.text)

    def get_cities(self) -> List[str]:
        response = requests.get(url=self.endpoint, headers=self.headers)
        deals = response.json()['deals']
        return [deal['city'] for deal in deals]
        