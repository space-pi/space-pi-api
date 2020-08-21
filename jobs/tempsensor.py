#!/usr/bin/python3
import sys
import Adafruit_DHT
import time
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="django",
  password="django",
  database="space_pi"
)

mycursor = mydb.cursor()
jobstarttime = time.time()

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    sql = """INSERT INTO space_pi_api_temphistory (reading, datetime, sensor) values (%s, now(), 1)"""
    val = (temperature,)
    mycursor.execute(sql,val)
    mydb.commit()
    sql = """INSERT INTO space_pi_api_humidityhistory (reading, datetime, sensor) values (%s, now(), 1)"""
    val = (humidity,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(temperature)
    print(humidity)
    time.sleep(60.0 - ((time.time() - jobstarttime) % 60.0))
#    print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %' + format(temperature, humidity))
