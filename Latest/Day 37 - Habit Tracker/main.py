import requests
from datetime import datetime
#https://pixe.la/v1/users/benrw67/graphs/graph1.html
USERNAME = "benrw67"
TOKEN = "chachacha"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_params = {
    "token": "chachacha",
    "username": "benrw67",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)

#print(response.text)

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Minutes",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()
#today.strftime("%Y%m%d")
pixel_data = {
    "date": "20220515",
    "quantity": "35",
}

#response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
requests.delete(url=f"{pixel_creation}/20220513", headers=headers)
#response = requests.delete(url=pixel_creation, json=pixel_data, headers=headers)
#print(response)