import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
NUTRIURL = os.environ.get("APP_URL")
GENDER = "male"
AGE = 35
WEIGHT = 83
HEIGHT = 175.26
SHEETYAUTH = "os.environ.get("SHEETY_KEY")

sheety_endpoint = os.environ.get("SHEETY_URL")
exercise_text = input("Tell me which exercises you did: ")

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}

nutri_user_params = {
    "query": exercise_text,
    "gender" : GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=NUTRIURL, json=nutri_user_params, headers=nutri_headers)
result = response.json()
print(result)

sheety_headers = {
    "Authorization": SHEETYAUTH
}

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result ["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_headers)

    print(sheet_response.text)