from weather import Weather
from alert import Alert
import config

def main():
    weather = Weather(config.WEATHER_API_KEY)
    alert = Alert()

    temperature = weather.get_current_temperature(config.LOCATION)

    if temperature > config.HEAT_WAVE_THRESHOLD:
        alert.send_alert(temperature)

if __name__ == "__main__":
    main()
