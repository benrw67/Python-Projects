import smtplib
import datetime as dt
import random

my_email="benw.python.test@gmail.com"
my_passw="Resco123!"
#with smtplib.SMTP(host="smtp.gmail.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=my_passw)
#    connection.sendmail(from_addr=my_email, to_addrs="benw.pythontest@yahoo.com", msg="Subject:Hi! \n\nHello, this is an email from Python code.")

#now = dt.datetime.now()
#year = now.year
#month = now.month
#day = now.day
#print(f"{day} - {month} - {year}")

#date_of_birth = dt.datetime(year=1986, month=4, day=16)
#print(date_of_birth)

with open("quotes.txt", "r") as quotes_raw:
    quotes_data = quotes_raw.read()
    quotes_list = quotes_data.replace('\n', ' ').split(".")

print(random.choice(quotes_list))

now = dt.datetime.now()
day = now.weekday()

if day == 3:
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_passw)
        connection.sendmail(from_addr=my_email, to_addrs="clairenwalker@icloud.com, benrwalker@icloud.com", msg=f"Subject:Todays Quote \n\nHere is your inspirational quote of the week: \n {random.choice(quotes_list)}")
else:
    pass