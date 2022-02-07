import requests
from twilio.rest import Client
STOCK_NAME = "QCOM"
COMPANY_NAME = "QUALCOMM"

STOCK_NAME = "QCOM"
COMPANY_NAME = "QUALCOMM"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "<Your Stock API Key>"
NEWS_API_KEY = "<Your News API Key>"
TWILIO_SID = "<Your TWILIO SID >"
TWILIO_TOKEN = "<Your TWILIO Authorisation Token>"

# TODO 1 : Get yesterday's closing stock price
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
# print(data)
# converting the json data to a list
data_list = [value for (key, value) in data.items()]
print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)
# json data is a dictionary with the key as date
# print(response.json())

## ALTERNATE WAY IS TO JUST PASS THE PARAMETERS IN
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'

# TODO 2 - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# TODO 3 - Find the positive difference between 1 and 2 . eg 40 - 20 = -20

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(difference)

# TODO 4 - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday
diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)
# TODO 5 - If TODO4 percentage is greater than 5 then print("Get News")
# if diff_percent > 1:
#     print("Get News")

# TODO 6 - Use the NEWS API to get news instead of just printing it
if abs(diff_percent) > 0:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title"

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    print(news_response.json())
    print(articles)

# TODO 7 : Use python slice operator tp list first three articls\
    first_three_article = articles[:3]
    print(first_three_article)

#   TODO 8 - Create a new list of the first three articles headline and description using list comprehenision
# "Headline: {article title}, \nBrief: {article description}"
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}, \nBrief: {article['description']}" for article in first_three_article]
  # TODO 9 - Send each article as a seperate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="<Your Twilio Phone number>",
            to="<Your Phone number>"
        )
