import time
import adafruit_dht
import board
import requests

dht = adafruit_dht.DHT11(board.D4)
api_key = " "

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity

        if temperature is not None and humidity is not None:
            print(f'Temperature: {temperature:.1f}C')
            print(f'Humidity: {humidity:.1f}%')

            params = {
                'api_key': api_key,
                'field1': temperature,
                'field2': humidity
            }

            requests.get("https://api.thingspeak.com/update", params=params)

    except RuntimeError as error:
        print('error')

    time.sleep(2)
