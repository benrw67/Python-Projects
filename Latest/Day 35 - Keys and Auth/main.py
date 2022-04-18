import requests
import os
KEY = os.environ.get("OWM_API_KEY")
LAT = "45.713840"
LON = "24.151320"
API = "https://api.openweathermap.org/data/2.5/onecall"

from twilio.rest import Client 
 
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token) 


#Param example: lat={lat}&lon={lon}&exclude={part}&appid={API key}

parameters = {
    "lat" : LAT,
    "lon" : LON, 
    "appid" : KEY,
    "exclude" : "current,minutely,daily"
}

response = requests.get(url=API, params=parameters)
data = response.json()
hourly_data = data["hourly"][:12]

response.raise_for_status()

will_rain = False

for hour in hourly_data:
    condition_code = (hour["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        body="It's going to rain today. Take an umbrella!",
        messaging_service_sid='MGbd36c7db3620fb21cf4a2ab3c2eb382d', 
        to="+447725613499"

        )
else:
        message = client.messages.create(
        body="No rain forecast!",
        messaging_service_sid='MGbd36c7db3620fb21cf4a2ab3c2eb382d', 
        to="+447725613499"
        ) 
 
print(message.status)