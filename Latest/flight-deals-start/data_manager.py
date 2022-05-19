import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ffe13bf6e799248d3e25498f46d8bdde/flightDeals/prices"
SHEETY_HEADERS = {
    "Authorization": "Bearer goingoneholidayw00w00"
}
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes (self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=SHEETY_HEADERS)
            print(response.text)