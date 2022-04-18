##################### Hard Starting Project ######################

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import datetime as dt
import pandas
import random

my_email="benw.python.test@gmail.com"
my_passw="Resco123!"
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in  birthdays:
    birthday_person = birthdays[today_tuple]
    birthday_name = birthday_person["name"]
    file_path= f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        contents = letter_file.read()
        contents_new = contents.replace("[NAME]", birthday_name)
        
        print(contents_new)
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_passw)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday! \n\n{contents_new}")