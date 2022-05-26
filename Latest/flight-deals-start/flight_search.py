import requests
from flight_data import FlightData
KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
KIWI_API = "AOuLwHb0S5EICLLmlg50mjrsVdxJgUak"
TEQUILA_API = {"apikey": "OvHs_VBwveW08-uwPkgdk_1uQGvaE2di"}
KIWI_HEADER = {"apikey": "AOuLwHb0S5EICLLmlg50mjrsVdxJgUak"}

class FlightSearch:

    def get_destination_code(self, city_name):
        endpoint = f"{KIWI_ENDPOINT}/locations/query"
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=endpoint, params=params, headers=KIWI_HEADER)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        endpoint = f"{KIWI_ENDPOINT}/v2/search"
        query = {
            "fly from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=endpoint, params=query, headers=TEQUILA_API)


        try:
            raw_data = response.json()["data"]
            if raw_data:
                data = raw_data[0]
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0]
                )
                print(f"{flight_data.destination_city}: ${flight_data.price}")
                return flight_data
            else:
                return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

