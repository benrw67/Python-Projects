import requests
import os
import smtplib


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_key = "5UGEBDC4CUATIH6F"
NEWS_KEY = "744234747dce4c06b0635f4a715b343a"
auth_token = os.environ.get("AUTH_TOKEN")
Acc_sid = os.environ.get("ACC_SID")
my_email="benw.python.test@gmail.com"
my_passw="Resco123!"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
stock_params = {
    "apikey" : stock_key,
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "60min"
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = yesterdays_data["4. close"]
print(yesterdays_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = float(yesterdays_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterdays_closing_price)) * 100)
print(diff_percent)

if diff_percent > 5:
    print("Get News")

if abs(diff_percent) > 1:
    news_params = {
        "apikey": NEWS_KEY,
        "qInTitle":COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_passw)
        connection.sendmail(from_addr=my_email, to_addrs="benrwalker@icloud.com",
                            msg=f"Subject:Todays News \n\nHere are your news articles related to Tesla stocks: \n {three_articles}")
else:
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



    #Optional TODO: Format the message like this:
    """
    TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

