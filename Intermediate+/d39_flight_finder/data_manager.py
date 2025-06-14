import os
import requests
from requests.auth import HTTPBasicAuth

SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.user = os.environ.get("SHEETY_USRERNAME")
        self.password = os.environ.get("SHEETY_PASSWORD")
        self.authorization = HTTPBasicAuth(self.user, self.password)
        self.dest_data = {}

    def get_dest_data(self):        
        dest_response = requests.get(url=SHEETY_ENDPOINT)
        dest_response.raise_for_status()
        data = dest_response.json()
        self.dest_data = data["prices"] 
        return self.dest_data
    
    def update_dest_code(self):
        for city in self.dest_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            update_response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            update_response.raise_for_status() 