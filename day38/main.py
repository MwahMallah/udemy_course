import os
import requests
import datetime
from requests.auth import HTTPBasicAuth

NUTRITION_API_KEY = os.environ.get("NUTRITION_API_KEY")
NUTRITION_APP_ID = os.environ.get("NUTRITION_APP_ID")
PASSWORD = os.environ.get("PASSWORD")
USERNAME = os.environ.get("USERNAME")

headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
    "x-remote-user-id": "0",
    "Content-Type": "application/json"
}

exercise_text = input("Which exercises did you do?:")
date_col = datetime.datetime.now().strftime("%d/%m/%Y")
time_col = datetime.datetime.now().strftime("%H:%M:%S")

params = {
    "query": exercise_text,
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=params)

exercises = response.json()["exercises"]

params = {
    "workout" : {
        "date": date_col,
        "time": time_col,
        "exercise": None,
        "duration": None,
        "calories": None,
    }
}

for exercise in exercises:
    params["workout"]["exercise"] = exercise["name"]
    params["workout"]["duration"] = exercise["duration_min"]
    params["workout"]["calories"] = exercise["nf_calories"]
    
    basic_auth = HTTPBasicAuth(username=USERNAME, password=PASSWORD)

    resp = requests.post(url="https://api.sheety.co/bd229125e44ca58de9a047a04a1b3d2d/workouts/workouts", json=params, auth=basic_auth)
    print(resp.text)

