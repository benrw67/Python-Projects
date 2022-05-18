import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ffe13bf6e799248d3e25498f46d8bdde/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_headers = {
            "Authorization": "Bearer goingoneholidayw00w00"
        }
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data