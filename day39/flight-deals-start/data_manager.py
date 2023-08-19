#This class is responsible for talking to the Google Sheet.
import requests
import os
from typing import List, Tuple

SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")


class DataManager:

    def __init__(self):
        self.endpoint = "https://api.sheety.co/bd229125e44ca58de9a047a04a1b3d2d/flightDeals/deals"
        self.headers = {
            "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
            "Content-Type": "application/json"
        }
    
    def get_cities_prices(self) -> List[Tuple]:
        response = requests.get(url=self.endpoint, headers=self.headers)
        deals = response.json()['deals']

        return [(deal['iataCode'], deal['lowestPrice'], deal['id'], deal['city']) for deal in deals]
    
    def update_price(self, row_in_spreadsheet: int, new_price: int):
        endpoint = f"{self.endpoint}/{row_in_spreadsheet}"
        body = {
            "deal":{
                "lowestPrice": new_price
            }
        }

        response = requests.put(url=endpoint, json=body, headers=self.headers)
        print(response.text)