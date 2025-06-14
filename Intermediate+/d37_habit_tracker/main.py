import os
import requests
from datetime import datetime

user_token = os.environ.get("PIXELA_TOKEN")
user_username = os.environ.get("PIXELA_USERNAME")
graph_id = os.environ.get("PIXELA_GRAPH_ID")
today = datetime(year=2025,month=6,day=12) # or "today = datetime.now()"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{user_username}/graphs"
PIXEL_ON_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{user_username}/graphs/{graph_id}"
UPDATE_PIXEL_ON_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{user_username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"
DELETE_PIXEL_ON_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{user_username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"

headers = {
    "X-USER-TOKEN": user_token,
}

user_params = {
    "token": user_token,
    "username": user_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_params = {
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji",
}
# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(graph_response.text)

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "6.00",
}
# pixel_on_graph_response = requests.post(url=PIXEL_ON_GRAPH_ENDPOINT, json=pixel_params, headers=headers)
# print(pixel_on_graph_response)

new_pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "17.00",
}
# update_pixel_on_graph_response = requests.put(url=UPDATE_PIXEL_ON_GRAPH_ENDPOINT, json=new_pixel_params, headers=headers)
# print(update_pixel_on_graph_response)

# delete_pixel_on_graph_response = requests.delete(url=DELETE_PIXEL_ON_GRAPH_ENDPOINT, headers=headers)
# print(delete_pixel_on_graph_response)