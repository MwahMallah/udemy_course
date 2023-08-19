#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

def main():
    dm = DataManager()
    fs = FlightSearch()
    cities = dm.get_cities()
    fs.get_airports(cities)

if __name__ == "__main__":
    main()