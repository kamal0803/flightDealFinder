import requests

sheety_url_endpoint = ""

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=sheety_url_endpoint).json()
        self.destination_data = sheet_response

        return self.destination_data

    def update_destination_code(self, i, new_data):
        requests.put(url=sheety_url_endpoint+f"/{i}", json=new_data)
