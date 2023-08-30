#This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
MY_PHONE_NUMBER = os.environ['MY_PHONE_NUMBER']

class NotificationManager:
    def __init__(self) -> None:
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def notificate_me(self, price, dst, date_departure, date_arrival):
        message = self.client.messages.create(
                     body=f"LOW PRICE ALERT! Only {price}CZK to fly from Prague to {dst}, from {date_departure} to {date_arrival}",
                     from_='+15736523525',
                     to=MY_PHONE_NUMBER
                 )
        print(message.sid)