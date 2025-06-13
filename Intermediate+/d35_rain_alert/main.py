# import os # automation
import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient # automation

# proxy_client = TwilioHttpClient() # automation
# proxy_client.session.proxies = {"https": os.environ['https_proxy']} # automation

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

API_KEY = "xyz" # os.environ.get("OWM_API_KEY") # automation
ACC_SID = "xyz" # os.environ.get("ACC_SID")
AUTH_TOKEN = "xyz" # os.environ.get("AUTH_TOKEN")

MY_LAT = 35.250778 # ex. lat and lon
MY_LONG = -91.736343
COUNT = 4 # 1 count for 3 hrs
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "cnt": COUNT
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
# print(data)

def bring_umbrella():
    for hr in data["list"]:
        weather_id = hr["weather"][0]["id"]
        # print(weather_id) # check
        if int(weather_id) < 700:
            return True
    return False

# Whatsapp functionality
TWILIO_NUM = "whatsapp:+xyz"
MY_NUM = "whatsapp:+xyz"
if bring_umbrella():
    client = Client(ACC_SID, AUTH_TOKEN) # for automation, do "client = Client(ACC_SID, AUTH_TOKEN, http_client=proxy_client)"
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_=TWILIO_NUM, # twilio whatsapp number
        to=MY_NUM # your whatsapp number
    )
    print(message.status)

