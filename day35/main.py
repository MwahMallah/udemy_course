import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
weather_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
params = {
    "appid":api_key,
    "lat":49.848171,
    "lon":3.288170,
    "units":"metric",
    "exclude":"current,minutely,daily"
}

accound_sid = "ACca28382aac15d0dae2f45cb03013796e"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
phone_number = "+15736523525"


response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=params)
response.raise_for_status()
weather_data = response.json()
weather_data = weather_data["hourly"][:12]

for hour_data in weather_data:
    if int(hour_data['weather'][0]["id"]) < 700:
        client = Client(accound_sid, auth_token)
        message = client.messages.create(body="Bring the umbrella", from_=phone_number, to=os.environ.get("MY_PHONE_NUMBER"))
        print(message.status)
        break
