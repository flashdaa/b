import RPi.GPIO as GPIO
import time
pir=11
led=13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
try:
    while True:
              
           if GPIO.input(pir):
              print("Motion")
              GPIO.output(led,GPIO.HIGH)
           else:
               print("No motion")
               GPIO.output(led,GPIO.LOW)
           time.sleep(2)
except KeyboardInterrupt:
      print("exit")
finally:
    GPIO.cleanup()
