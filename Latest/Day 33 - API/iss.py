import requests
from datetime import datetime
import smtplib
from time import time, sleep

MY_LAT = 50.827990
MY_LONG = 0.245310
my_email="benw.python.test@gmail.com"
my_passw="Resco123!"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def iss_close():
    if MY_LAT-5 <= iss_latitude <=MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def is_it_dark():
    if time_now.hour >= sunset and time_now.hour <= sunrise:
        return True

while True:
    sleep(60 - time()% 60)
    if iss_close() is True and is_it_dark() is True:
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_passw)
            connection.sendmail(from_addr=my_email, to_addrs="benrwalker@icloud.com", msg=f"Subject:ISS is close! \n\n The ISS is close, go outside and look up!")




