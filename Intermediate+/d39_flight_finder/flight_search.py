import os
import requests

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        self.api_key = os.environ.get("AMADEUS_API_KEY")
        self.api_secret = os.environ.get("AMADEUS_SECRET")
        self.token = self.get_new_token()

    def get_new_token(self):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        token_params = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        token_response = requests.post(TOKEN_ENDPOINT, headers=headers, data=token_params)
        token_response.raise_for_status()
        return token_response.json()['access_token']
    
    def get_dest_code(self, city):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        query = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "Airport code not found."
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Airport code not found."
        return code
    
    def check_flights(self, city, origin_city, from_time, to_time, is_direct=True):
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        query = {
            "originLocationCode": origin_city,
            "destinationLocationCode": city,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": 10,
        }
        check_response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)

        if check_response.status_code != 200:
                print(f"check_flights() response code: {check_response.status_code}")
                print("There was a problem with the flight search.\n"
                    "For details on status codes, check the API documentation:\n"
                    "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference")
                print("Response body:", check_response.text)
                return None