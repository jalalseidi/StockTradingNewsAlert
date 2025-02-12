import requests
import os
import smtplib

my_email = "matildaseidi@gmail.com"
my_password = os.environ.get("EMAIL_PASS")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_KEY = os.environ.get("ALPHA_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

ALPHA_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_KEY}"
NEWS_URL = "https://newsapi.org/v2/everything"

# Step 1: Fetch stock data
response = requests.get(url=ALPHA_URL)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

# Ensure we get the latest trading days in order
sorted_dates = sorted(data.keys(), reverse=True)
yesterdays_data = data[sorted_dates[0]]
yesterdays_closing_price = float(yesterdays_data["4. close"])

day_before_yesterdays_data = data[sorted_dates[1]]
day_before_yesterdays_closing_price = float(day_before_yesterdays_data["4. close"])

# Calculate percentage change
difference = ((yesterdays_closing_price - day_before_yesterdays_closing_price) / day_before_yesterdays_closing_price) * 100
abs_difference = abs(difference)

# Step 2: Fetch news if stock moved 5%+
if abs_difference > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(url=NEWS_URL, params=news_params)
    news_response.raise_for_status()
    data = news_response.json()
    articles = data["articles"][:3]  # Get top 3 articles

    # Format articles for email
    formatted_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in articles]

    # Step 3: Send a single email with all news
    full_message = f"Subject: Tesla Stock Alert!\n\nTSLA: {'🔺' if difference > 0 else '🔻'}{abs_difference}%\n\n" + "\n\n".join(formatted_articles)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=full_message.encode("utf-8"))
