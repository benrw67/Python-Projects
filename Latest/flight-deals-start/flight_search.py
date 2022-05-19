import requests
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query?"
KIWI_API = "AOuLwHb0S5EICLLmlg50mjrsVdxJgUak"
KIWI_HEADER = "AOuLwHb0S5EICLLmlg50mjrsVdxJgUak"

class FlightSearch:
    def __init__(self):
        self.destination_data = {}

    def get_destination_code(self, city_name):
        params = {

        }

        code = "Testing"
        return code