#This class is responsible for talking to the Flight Search API.
import requests
from typing import List


class FlightSearch:
    def __init__(self) -> None:
        # self.endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.header = {
            "apikey": "yLumPs0BCkULV9QIjbJVIHJTjUgA0ZMf"
        }

    def find_flights(self):

        flight_info = {
            "fly_from": "PRG",
            "fly_to": ""
        }
        
        requests.get(url=self.endpoint, headers=self.header, params=flight_info)

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
