from datetime import datetime,timedelta
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API = {"apikey": "AOuLwHb0S5EICLLmlg50mjrsVdxJgUak"}

class FlightData:
    def get_flight_price(self, iata_code):
        tomorrows_date = datetime.now().strftime("%d/%m/%Y") + timedelta(days = 1)
        up_to = datetime.now().strftime("%d/%m/%Y") + timedelta(months = 6)

        params = {
            "fly_from": "LON",
            "fly_to": iata_code,
            "date_from": tomorrows_date,
            "date_to": up_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0
        }

        response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=TEQUILA_API)
        results = response.json()
        return results


