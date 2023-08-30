#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

def main():
    spreadsheet_data = DataManager()
    flights_data = FlightSearch()
    notifictations = NotificationManager()

    cities_prices = spreadsheet_data.get_cities_prices()

    for (airport_code, existing_price, row_in_spreadsheet, city) in cities_prices:

        flight = flights_data.find_flight_with_cheapest_price(airport_code)
        print(f"{city}: {flight['price']}")
        if flight["availability"]["seats"] != None:
            new_price = flight["price"]
            
            if new_price < existing_price:
                spreadsheet_data.update_price(row_in_spreadsheet, new_price)

                date_departure = flight["route"][0]["local_departure"].split("T")[0]
                date_comeback = flight["route"][-1]["local_departure"].split("T")[0]
                
                notifictations.notificate_me(new_price, city, date_departure, date_comeback)


if __name__ == "__main__":
    main()