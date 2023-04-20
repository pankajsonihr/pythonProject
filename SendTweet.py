import time
import board
import adafruit_dht		        # Adafruit DHT library for sensor
import psutil
import sys
import speech_recognition as sr
from Speak import speak
import main as m
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

def listener():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""

def send_tweet():
    while True:
        try:
            print("Would you like to speak or type your tweet?")
            speak("Would you like to speak or type your tweet?")
            query = m.paseCommand()
            if "speak" in query:
                status = listener()
                speak(status)
                print(status)			#Print the status
                twitter.update_status(status = status)	#Send/update tweets on twitter
            elif "type" in query:
                tweet = input("Enter tweet: ")
                twitter.update_status(status = tweet)
                break
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            break

        except Exception as error:
            sensor.exit()
            raise error
            break
        time.sleep(2.0)
