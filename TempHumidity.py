import time
import board
import adafruit_dht  # Adafruit DHT library for sensor
import psutil
import sys

# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()

# Initialize the DHT sensor
sensor = adafruit_dht.DHT11(board.D23)  # GPIO pin 23 on raspberry pi.

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
sensor = adafruit_dht.DHT11(board.D23, use_pulseio=False)
while True:
    try:
        temp = sensor.temperature  # Read temperature from DHT11 sensor
        humidity = sensor.humidity  # Read humidity from DHT11 sensor
        status = "Temperature: {}*C   Humidity: {}% ".format(temp, humidity)
        print(status)  # Print the status

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue

    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(2.0)


