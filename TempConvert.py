import time
import board
import adafruit_dht  # Adafruit DHT library for sensor
import psutil
import pyttsx3
import sys

# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

# Initialize the DHT sensor
sensor = adafruit_dht.DHT11(board.D17)  # GPIO pin 17 on raspberry pi.

sensor = adafruit_dht.DHT11(board.D17, use_pulseio=False)

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def temp_f():
        while True:
                try:
                        temp = sensor.temperature  # Read temperature from DHT11 sensor
                        temp_f = (temp * 9 / 5) + 32  # convert Celsius to Fahrenheit
                        humidity = sensor.humidity  # Read humidity from DHT11 sensor
                        status = "Temperature: {}*C   {}*F   Humidity: {}% ".format(temp, temp_f,
                                                                    humidity)  # print both temperatures in Celsius and Fahrenheit
                        print(status)
                        speak(status)

                except RuntimeError as error:
                        print(error.args[0])
                        time.sleep(2.0)
                        break

                except Exception as error:
                        sensor.exit()
                        raise error
                        break
                time.sleep(2.0)


