import os
import requests
import datetime
import smtplib
from typing import List, Tuple
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_news_articles():
    news_api_key = os.environ.get("NEWS_API_KEY")
    news_api_endpoint = "https://newsapi.org/v2/everything"
    date = str(datetime.date.today() - datetime.timedelta(days=2))
    news_params = {
        "q": COMPANY_NAME, 
        "from": date,
        "sortBy":"publishedAt",
        "apiKey": news_api_key
    }
    news_request = requests.get(news_api_endpoint, params=news_params)

    return [(article["title"].encode('utf-8')[2:], article["description"].encode('utf-8')) for article in news_request.json()["articles"][:3]]

def send_email(articles: List[Tuple], prcnt: float):
    sender_password = os.environ.get("GMAIL_PASSWORD")
    sender_user = "maksim0dubrovin0@gmail.com"

    for (title, description) in articles:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sender_user, password=sender_password)
            connection.sendmail(from_addr=sender_user, to_addrs="maximus27rus@gmail.com", msg=f"Subject: {title}\n\n{description}")

def send_sms(articles: List[Tuple], prcnt: float):
    client = Client(os.environ.get("TWILIO_ACC_SID"), os.environ.get("TWILIO_AUTH_TOKEN")) 

    for (title, description) in articles:
        if prcnt < 0:
            body_msg = f"{STOCK}: 🔻{-prcnt}%\n"
        else: 
            body_msg = f"{STOCK}: 🔺{prcnt}%\n"
        body_msg += f"Headline: {title}\nBrief: {description}"
        message = client.messages.create(to=os.environ.get("MY_PHONE_NUMBER"), from_="+15736523525", body=body_msg)
        print(message.status)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api_key = os.environ.get("STOCK_API_KEY")
stock_api_endpoint = "https://www.alphavantage.co/query"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

stock_request = requests.get(stock_api_endpoint, params=stock_params)
stock_request.raise_for_status()
stock_data = stock_request.json()

today_date = str(datetime.date.today() - datetime.timedelta(days=4))
yesterday_date = str(datetime.date.today() - datetime.timedelta(days=5))

tsla_price_today = float(stock_data["Time Series (Daily)"][today_date]["4. close"])
tsla_price_yesterday = float(stock_data["Time Series (Daily)"][yesterday_date]["4. close"])

prcnt_of_change = 100 * (tsla_price_today - tsla_price_yesterday) / tsla_price_today
if prcnt_of_change > 1 or prcnt_of_change < -1:
    articles = get_news_articles()
    send_email(articles, prcnt_of_change)
    send_sms(articles, prcnt_of_change)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

