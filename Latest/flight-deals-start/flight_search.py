import requests
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query?"
KIWI_API = "AOuLwHb0S5EICLLmlg50mjrsVdxJgUak"
KIWI_HEADER = {"apikey": "AOuLwHb0S5EICLLmlg50mjrsVdxJgUak"}

class FlightSearch:

    def get_destination_code(self, city_name):
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=KIWI_ENDPOINT, params=params, headers=KIWI_HEADER)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code