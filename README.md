# Tesla Stock Alert Project

## 📌 Overview
This Python script monitors Tesla's stock price and sends an email notification if the stock price changes by more than **5%** between two consecutive trading days. If the threshold is met, the script fetches the latest news about Tesla and includes them in the email notification.

## 🚀 Features
- Fetches Tesla's daily stock prices using the **Alpha Vantage API**.
- Calculates the percentage change between the last two trading days.
- Retrieves the latest Tesla news from the **News API** if the stock price change exceeds 5%.
- Sends an email notification containing:
  - The percentage change (🔺 or 🔻)
  - The top 3 latest news headlines and brief descriptions.

## 🛠️ Technologies Used
- **Python**
- **Requests** (for API calls)
- **SMTP** (for sending emails)
- **Alpha Vantage API** (for stock data)
- **News API** (for fetching Tesla-related news)

## 📜 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/tesla-stock-alert.git
cd tesla-stock-alert
```

### 2️⃣ Install Required Dependencies
Make sure you have Python installed. Then, install dependencies:
```bash
pip install requests
```

### 3️⃣ Set Up Environment Variables
Create an `.env` file or set environment variables in your system:
```
ALPHA_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key
EMAIL_PASS=your_email_password
```
Alternatively, you can set them in your script:
```python
import os
os.environ["ALPHA_KEY"] = "your_alpha_vantage_api_key"
os.environ["NEWS_API_KEY"] = "your_news_api_key"
os.environ["EMAIL_PASS"] = "your_email_password"
```

### 4️⃣ Run the Script
```bash
python stock_alert.py
```

## 🔔 Automate Execution
To run this script automatically every day:
- **Linux/macOS**: Use `cron`
- **Windows**: Use Task Scheduler

## 📧 Example Email Format
```
Subject: Tesla Stock Alert!

TSLA: 🔻6.3%

Headline: Tesla's Stock Drops Amid Market Uncertainty
Brief: Tesla's stock saw a sharp decline due to...

Headline: Elon Musk Announces New Product
Brief: The new Tesla product is set to revolutionize...
```

## 📝 To-Do List
- [ ] Add support for more stocks
- [ ] Implement Twilio for SMS alerts
- [ ] Create a web dashboard for stock tracking

## 🏆 Credits
- Developed by [Your Name]
- API Services: Alpha Vantage, News API

## 📄 License
This project is licensed under the MIT License.

