import requests
from datetime import datetime
import time
import smtplib

def is_iss_near(iss_lat: float, iss_lng: float) -> bool:
    return MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5

#setting constants
MY_LAT = 49.195061
MY_LNG = 16.606836

target_user = "maximus27rus@gmail.com"
user = "maksim0dubrovin0@gmail.com"
with open("password.txt", mode="r") as file:
    password = file.read()

date_parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}
#/setting constants


# Getting current location sunset and sunrise data
date_response = requests.get("https://api.sunrise-sunset.org/json", params=date_parameters)
date_response.raise_for_status()
date_data = date_response.json()

sunrise_hour = int(date_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(date_data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()
#/Getting current location sunset and sunrise data

#Getting iss position
iss_position_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_position_response.raise_for_status()
iss_position = iss_position_response.json()
iss_lng = float(iss_position["iss_position"]["longitude"])
iss_lat = float(iss_position["iss_position"]["latitude"])
#/Getting iss position

#if now is dark and iss is visible send email
while True:
    time.sleep(60)
    if (time_now.hour < sunrise_hour or time_now.hour > sunset_hour) and is_iss_near(iss_lat, iss_lng):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user, to_addrs="maximus27rus@gmail.com", msg="Subject:ISS\n\nYou can see ISS right now!!!")