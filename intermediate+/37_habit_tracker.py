import requests
import datetime as dt

USER_NAME = "alicebui1301"
TOKEN = "gsdfk@3549034kfdj&"

# Create User
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# Create Graph
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Habit Tracker",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Create Pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
today = dt.datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)