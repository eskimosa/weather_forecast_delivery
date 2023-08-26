Intro
--

Stay up-to-date with the weather forecast using these Python scripts! Each script scrapes weather information from AccuWeather and sends notifications using different methods - choose the one that suits you better!

Scripts at Your Service - Choose the desired script to run based on the notification method you prefer.
--

1. weather_forecast_api:
This script fetches the weather forecast for the desired city using the AccuWeather API. Simply provide the name of the city when prompted, and the script will use the AccuWeather API to fetch the latest weather data. It then processes this data to extract temperature and forecast information, and sends the processed information to a Slack channel using a webhook. 

2. weather_forecast_twilio:
Ready for action-packed weather updates? This script swoops in, scrapes the desired city weather forecast, and sends a fast SMS using the incredible Twilio service. If the web service you would like to use doesn't provide API then this script should be your choice! With help of BeautifulSoup library you'll be armed with accurate weather info straight to your phone. To customize the city, you can modify the URL in the script to point to your desired location's forecast on the AccuWeather website.

Requirements
--

```shell
$ cat requirements.txt
beautifulsoup4==4.12.2
requests==2.31.0
twilio==8.5.0
typer==0.9.0
```

Setup
--

1. Create '.env' file in the same directory as your scripts.
2. Depending on the script you want to run, add the following environment variables to the '.env' file:
```shell
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_NUMBER = 'your_twilio_number'
TARGET_NUMBER = 'your_twilio_target_number'
ACCU_API = 'your_accuweather_api_key'
SLACK_WEBHOOK = 'your_slack_webhook_url'
```
3. Install the required packages:
```shell
$ virtualenv venv
$ venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Running the Scripts
--
```shell
$ python3 main.py sms # To receive weather forecast via SMS
$ python3 main.py slack # To receive weather forecast in Slack
```

Before running any of the scripts, ensure you configure the necessary credentials and API keys as required.
Please adjust any paths or formatting to match your actual file structure and preferences.

Author
--

[eskimosa](https://github.com/eskimosa/)
