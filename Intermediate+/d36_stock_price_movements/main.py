import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWSAPI_KEY")

TWILIO_AUTH = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_NUM = f"whatsapp:+{os.environ.get('TWILIO_NUM')}"
MY_NUM = f"whatsapp:+{os.environ.get('MY_NUM')}"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": STOCK_API_KEY,
}
news_params = {
    "q": COMPANY_NAME,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY,
}

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_close = float(stock_data_list[0]["4. close"])
day_before_yesterday_close = float(stock_data_list[1]["4. close"])
stock_diff = abs(day_before_yesterday_close - yesterday_close) / abs(day_before_yesterday_close)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
if stock_diff > 0.05: # can switch the percent if needed
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_articles = news_response.json()["articles"][:3]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.        
    for article in news_articles:        
        client = Client(TWILIO_SID, TWILIO_AUTH)    
        percent_change = round((day_before_yesterday_close - yesterday_close) / (day_before_yesterday_close), 2) * 100
        percent_movement = ""
        if percent_change > 0:
            percent_movement = "🔺"
        else:
            percent_movement = "🔻"
        formatted_body = f"{STOCK}: {percent_movement}{f'{abs(percent_change)}'}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        message = client.messages.create(
            body=formatted_body,
            from_=TWILIO_NUM, # twilio whatsapp number
            to=MY_NUM # your whatsapp number
        )    


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

