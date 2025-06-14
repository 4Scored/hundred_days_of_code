import os
import requests
from datetime import datetime

APP_ID = os.environ.get("NX_APP_ID")
API_KEY = os.environ.get("NX_API_KEY")
SHEETY_ID = os.environ.get("SHEETY_ID")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

WEIGHT_KG = 70 # ex. vars
HEIGHT_CM = 175
AGE = 20

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": input,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM ,
    "age": AGE,
}

exercise_response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=headers)
exercise_response.raise_for_status()
exercise_call = exercise_response.json()
# print(exercise_call)

today_date = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

sheety_headers = {
    "Authorization": f"Basic {SHEETY_TOKEN}"
}

for exercise in exercise_call["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
sheet_response.raise_for_status()
# print(sheet_response.text)

# important sources
    # https://docx.syndigo.com/developers/docs/natural-language-for-exercise