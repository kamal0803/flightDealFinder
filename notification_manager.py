from twilio.rest import Client
import datetime

TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

class NotificationManager:

    def date_conversion(self, date_str):
        return (datetime.datetime.fromisoformat(date_str.replace('Z', '+00:00'))).date()

    def send_sms(self, x, destination_code, lowest_price):

        global min_date, max_date, t, flag

        tomorrow = datetime.datetime.now() + datetime.timedelta(days=2)
        max_date = tomorrow.date()
        min_date = (tomorrow + datetime.timedelta(days=6 * 30)).date()
        flag = 0

        for z in range(len(x['data'])):

            departure_date = self.date_conversion(x['data'][z]['local_departure'])

            if x['data'][0]['price'] <= lowest_price:

                t = x['data'][0]['price']
                if departure_date < min_date:
                    min_date = departure_date

                if departure_date > max_date:
                    max_date = departure_date

                flag = 1

            else:
                break

        if flag == 1:
            body = f"Low price alert! Only {t}£ to fly from LON to {destination_code}, from {min_date} to {max_date}"
            message = client.messages.create(
                from_='',
                body=body,
                to=''
            )


