import typer
import weather_forecast_api
import weather_forecast_twilio

start = typer.Typer()


@start.command()
def sms():
    weather_forecast_twilio.main()


@start.command()
def slack():
    weather_forecast_api.main()


if __name__ == '__main__':
    start()
