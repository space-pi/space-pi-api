#!/usr/bin/python3
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    print(temperature)
    print(humidity)
#    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %' + format(temperature, humidity))