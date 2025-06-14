#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "LON"
email_list = [] # fill out

data_manager = DataManager()
sheet_data = data_manager.get_dest_data()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_dest_code(row["city"])        
        time.sleep(1)

data_manager.dest_data = sheet_data
data_manager.update_dest_code()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
for destination in sheet_data:    
    flights = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"], from_time=tomorrow, to_time=six_month_from_today)
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:    
        message_body=f"Low price alert! Only £{cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        notification_manager.send_msg(message_body)
        notification_manager.send_emails(email_list=email_list, email_body=message_body)