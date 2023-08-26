import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_location_key(accu_api_key, searched_city):
    url_loc_key = 'http://dataservice.accuweather.com/locations/v1/cities/search?apikey=%s&q=%s' % (accu_api_key, searched_city)
    web_response_location = requests.get(url_loc_key).json()
    location_key = web_response_location[0]['Key']
    return location_key


def fetch_weather_data(location_key, accu_api_key):
    url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/%s?apikey=%s' % (location_key, accu_api_key)
    web_response = requests.get(url).json()
    return web_response


def processing_response(web_data, searched_city):
    forecast = web_data['DailyForecasts'][0]['Day']['IconPhrase']
    temp = web_data['DailyForecasts'][0]['Temperature']['Maximum']['Value']
    temp_celsius = int((temp - 32) * 5 / 9)
    return f'{searched_city} today: {temp_celsius} degrees - {forecast}'


def send_slack_message(text, key):
    payload = '{"text": "%s"}' % text
    response = requests.post(key,
                             data=payload)
    print(response.text)


def main():
    api_key = os.getenv('ACCU_API')
    slack_webhook = os.getenv('SLACK_WEBHOOK')

    city = input('Please type the city you`d like to see the forecast for: ')
    location_key = get_location_key(api_key, city)
    web_response = fetch_weather_data(location_key, api_key)
    message = processing_response(web_response, city)
    send_slack_message(message, slack_webhook)


if __name__ == '__main__':
    main()
