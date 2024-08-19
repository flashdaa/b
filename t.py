import time
import adafruit_dht
import board

dht = adafruit_dht.DHT11(board.D4)  

while True:
    
        temperature = dht.temperature
        humidity = dht.humidity

        print(f'Temperature: {temperature:.1f}C')
        print(f'Humidity: {humidity:.1f}%')

         
    
        time.sleep(2)  
