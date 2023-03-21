import time
import board
import adafruit_dht		        # Adafruit DHT library for sensor
import psutil
import sys
from twython import Twython	    # Twython package to send tweets
from auth import (		        # Importing keys and token from auth.py file
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = adafruit_dht.DHT11(board.D23)	#GPIO pin 23 on raspberry pi.

while True:
    try:
        read = input("Would you like to send tweets read from sensors or type personal message? \n 1 :> Read Sensor \t 2 :> Type Message")
        choice = int(read)

        if choice == 1:
            temp = sensor.temperature	#Read temperature from DHT11 sensor
            humidity = sensor.humidity	#Read humidity from DHT11 sensor
            status = "Temperature: {}*C   Humidity: {}% ".format(temp, humidity)
            print(status)			#Print the status
            twitter.update_status(status = status)	#Send/update tweets on twitter
        else:
            tweet = input("Enter tweet: ")
            twitter.update_status(status = tweet)
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)
