import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO pin

while True:
    humidity, temperature = Adafruit_DHT.read(sensor, pin)

    if humidity is not None and temperature is not None:
        print(f"Temp={temperature}°C  Humidity={humidity}%")
    else:
        print("Sensor error")

    time.sleep(2)
