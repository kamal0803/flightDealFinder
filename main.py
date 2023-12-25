from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

data_mngr = DataManager()
sheet_response = data_mngr.get_destination_data()
notification_manager = NotificationManager()

flight_srch = FlightSearch()

for i in sheet_response['prices']:

    flight_data = flight_srch.check_flights(i['iataCode'])
    lowest_price = i['lowestPrice']

    notification_manager.send_sms(flight_data, i['iataCode'], lowest_price)

