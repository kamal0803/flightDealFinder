import requests
import datetime

TEQUILA_ENDPOINT = ""
api_key = ""

tomorrow = datetime.datetime.now() + datetime.timedelta(days=2)

headers = {
    "accept": "application/json",
    "apikey": api_key
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def update_destination_data(self, city):

        params = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
        }

        flight_response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=headers)

        return flight_response

    def check_flights(self, destination_code):

        params = {
            "fly_from": "LON",
            "fly_to": destination_code,
            "date_from": tomorrow.strftime("%d/%m/%Y"),
            "date_to": (tomorrow + datetime.timedelta(days=6 * 30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "curr": "GBP",
            "max_stopovers": "0"
        }

        flight_response = requests.get(url=f"{TEQUILA_ENDPOINT}v2/search", params=params, headers=headers)
        x = flight_response.json()

        print(f"City: {destination_code}, Price: {x['data'][0]['price']}")

        return x

