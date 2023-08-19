#This class is responsible for talking to the Flight Search API.
import requests
from typing import List, Dict
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self) -> None:
        self.endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.header = {
            "apikey": "yLumPs0BCkULV9QIjbJVIHJTjUgA0ZMf"
        }
        self.date_from = datetime.now()
        self.date_to = self.date_from + timedelta(days=182)

    def find_flight_with_cheapest_price(self, airport_code) -> Dict:

        flight_info = {
            "fly_from": "PRG",
            "fly_to": airport_code,
            "date_from": self.date_from.strftime("%d/%m/%Y"),
            "date_to": self.date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 4,
            "sort": "price",
            "limit": 1,
            "curr": "CZK"
        }
        
        response = requests.get(url=self.endpoint, headers=self.header, params=flight_info)

        return response.json()["data"][0]


    def get_airports(self, cities: List[str]):

        for city in cities: 
            airport_info = {
                "term": city
            }

            response = requests.get(url=self.endpoint, headers=self.header, params=airport_info)

            print(response.json())

        city = cities[0]
        airport_info = {
                "term": city
            }

        response = requests.get(url=self.endpoint, headers=self.header, params=airport_info)

        print(response.json())
