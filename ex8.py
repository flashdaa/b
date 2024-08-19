import RPi.GPIO as GPIO
import requests
import time

api_key = " "
channel_id = 

LDR_PIN = 7
LED_PIN = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        ldr_value = GPIO.input(LDR_PIN)
        GPIO.output(LED_PIN, ldr_value)
        params = {'api_key': api_key, 'field1': ldr_value}
        try:
            response = requests.get(f"https://api.thingspeak.com/update", params=params)
            print(f"LDR Value: {ldr_value}, LED State: {'ON' if ldr_value else 'OFF'}, Response: {response.text}")
        except Exception as e:
            print("Failed to update ThingSpeak:", e)
        time.sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
finally:
    GPIO.cleanup()
