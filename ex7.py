import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText
import time

EMAIL_ADDRESS = ' '  
EMAIL_PASSWORD = ' '  
TO_EMAIL = ' '    

SENSOR_PIN = 11  
BUZ_PIN = 13     

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.setup(BUZ_PIN, GPIO.OUT)

def send_email():
    msg = MIMEText('Rain/Water detected!')
    msg['Subject'] = 'Alert: Rain/Water Detected'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

try:
    print("Rain/Water Sensor Test")
    time.sleep(2)  
    print("Ready")

    while True:
        if not GPIO.input(SENSOR_PIN):  
            print("Rain/Water detected!")
            GPIO.output(BUZ_PIN, GPIO.HIGH) 
            send_email()
            time.sleep(5)  
        else:
            GPIO.output(BUZ_PIN, GPIO.LOW)  

except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup() 
