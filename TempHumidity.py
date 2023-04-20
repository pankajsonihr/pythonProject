import time
import board
import adafruit_dht  # Adafruit DHT library for sensor
import psutil
import pyttsx3
import main as m
import TempConvert as convert
import sys

# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

# Initialize the DHT sensor
sensor = adafruit_dht.DHT11(board.D17)  # GPIO pin 17 on raspberry pi.

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
sensor = adafruit_dht.DHT11(board.D17, use_pulseio=False)

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def house_temperature():
    while True:
        try:
            speak("Would you like to know temperature in Celcius or Fahrenheit")
            print("Would you like to know temperature in Celcius or Fahrenheit")
            query = m.parseCommand().lower()
            if "celcius" in query:
                temp = sensor.temperature  # Read temperature from DHT11 sensor
                humidity = sensor.humidity  # Read humidity from DHT11 sensor
                status = "Temperature: {}*C   Humidity: {}% ".format(temp, humidity)
                print(status)  # Print the status
                speak(status)
            elif "fahrenheit" in query:
                convert.temp_f()

        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            break

        except Exception as error:
            sensor.exit()
            raise error
            break
        time.sleep(2.0)


