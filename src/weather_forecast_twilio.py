import datetime
from dotenv import load_dotenv
from twilio.rest import Client
import os
from bs4 import BeautifulSoup
import requests


load_dotenv()


def today_date():
    current_date = datetime.datetime.now()
    current_date_formatted = current_date.strftime('%-m/%d')
    return current_date_formatted


def scrape_web(web, c_date):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    html_text = requests.get(web, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    date = soup.find('span', class_='module-header sub date').text
    forecast = soup.find('div', class_='phrase').text.lower()
    if c_date == date:
        if 'showers' in forecast or 'shower' in forecast or 'rain' in forecast:
            return f'Don\'t forget your umbrella! Look at the forecast for today: {forecast}'
        elif 'sunshine' in forecast or 'sunny' in forecast or 'sun' in forecast:
            return f'Don\'t forget your SPF cream! Look at the forecast for today: {forecast}'
        else:
            return f'Here is you forecast for today: {forecast}'


def send_sms(text):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_number = os.getenv('TWILIO_NUMBER')
    target_number = os.getenv('TARGET_NUMBER')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=text,
        from_=twilio_number,
        to=target_number
    )
    print(message.body)


def main():
    url = 'https://www.accuweather.com/en/es/barcelona/307297/daily-weather-forecast/307297'
    fetch_data = scrape_web(url, today_date())
    send_sms(fetch_data)


if __name__ == '__main__':
    main()
