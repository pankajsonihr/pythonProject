import random

import speech_recognition as sr
from datetime import datetime
import json

import SMS
import Wolframalpha as wf
import News as News
from Weather import *
import Bulb as sb
import randfacts
import Youtube as yt

import SendTweet as Tweet
import TempHumidity as hometemp
import TempConvert as fahren
from SMS import sendEmergencyText
from Speak import speak
import Recipe as Recipe

activationWord = 'hello buddy'  # single word

responses = json.loads(open('responses.json').read())


def parseCommand():
    # listener = sr.Recognizer()
    # print("Listening for a command")
    #
    # with sr.Microphone() as source:
    #     listener.energy_threshold = 10000  # it listen low voices as well
    #     listener.adjust_for_ambient_noise(source, 1.2)
    #     input_speech = listener.listen(source)

    try:
        print("Recognizing speech...")
        converted_text = input("What action would you like too take? ")
        # converted_text = listener.recognize_google(input_speech, language='en_gb')
        print(f"The input speech was: {converted_text}")
    except Exception as exception:
        print('I did not quite catch that')
        # speak('I did not quite catch that')
        print(exception)
        return "None"
    return converted_text


def get_response(input_text):
    for intent in responses['chat']:
        for pattern in intent['patterns']:
            if isinstance(pattern, list):
                for p in pattern:
                    if p.lower() in input_text.lower():
                        return random.choice(intent['responses'])
            else:
                if pattern.lower() in input_text.lower():
                    return random.choice(intent['responses'])
    return None


def conversation():
    print("Starting conversation mode")
    speak("Starting conversation mode")
    while True:
        input_text = parseCommand()
        if input_text is not None:
            response = get_response(input_text)
            if response is not None:
                speak(response)
                print(response)
            else:
                speak("I'm sorry, I didn't understand what you said")
                speak("Exiting conversation mode")
                break
        else:
            break


# Main Loop
if __name__ == '__main__':
    speak('Starting c p i n buddy')
    while True:
        # List Commands
        query = parseCommand().lower().split()
        if "hi" and "buddy" in query:
            speak('Hi how I can help you.')

            query = parseCommand().lower().split()

            if "who" and "are" and "you" in query:
                speak(get_response("What is your name"))

            elif "conversation" in query:
                conversation()

            elif "date" in query:
                speak(News.return_date())
            elif "current" and "time" in query:
                speak(News.return_date())
            elif "time" and "now" in query:
                speak(News.return_date())

            elif "say" and "hello" in query:
                speak(get_response("greetings"))

            # We have inserted stories in json file for now.
            elif "story" in query:
                speak("Seems like you want to listen a story")
                print("Seems like you want to listen a story\n")
                speak(get_response("tell me a story"))
                print(get_response("tell me a story"))

            # WolframAlpha this will compute math but not much effective in some cases. --Done
            elif query[0] == 'calculate' or query[0] == 'compute':
                query = ''.join(query[1:])
                speak('Computing')
                try:
                    result = wf.search_wolfram(query)
                    speak(result)
                except:
                    speak("Sorry I can't compute it.")

            # Will read top 3 news for user --Done
            elif 'news' in query:
                get_news = News.news()
                speak(get_news)

            # This will give random facts to user.  --Done
            elif "random" and "fact" in query:
                speak("Sure sir, I will find some interesting facts for you.")
                rngfacts = randfacts.get_fact()
                speak("Did you know that, " + rngfacts)
            # This will give random facts to user if he said facts instead of fact.  --Done
            elif "random" and "facts" in query:
                speak("Sure sir, I will find some interesting facts for you.")
                rngfacts = randfacts.get_fact()
                speak("Did you know that, " + rngfacts)
                print("Did you know that, " + rngfacts)

            # Weather info is working perfectly. --Done
            elif "weather" and "outside" in query:
                speak(f"current temperature in sudbury is " + str(temp()))
                print(f"current temperature in sudbury is " + str(temp()))

            # Bulb commands are working perfectly. --Done
            elif "activate" and "bulb" in query:
                if any(arg in ['on', 'off', 'red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'black', 'white'] for
                       arg in query):
                    sb.bulb_commands(query)
                else:
                    speak("I think we didn't got you.")
                    speak("say turn on to light the bulb, or say turn off to turn it off")
                    speak("to change color tell me the color name only")
                    query = parseCommand().lower().split()
                    sb.bulb_commands(query)
            # This location part is also working. --Done
            elif "location" in query:
                speak("Seems like you want to find a location please tell me the name of loction only.")
                SMS.sendLocationOnPhone(parseCommand().lower())
            # Emergency help perfectly working. --Done
            elif "emergency" and "help" in query:
                speak("Please tell me your emergency message. I will send that to emergency help.")
                text = parseCommand().lower()
                print(text)
                sendEmergencyText(text)

            # Finally we figure our recipe part now. --Done
            elif "recipe" in query:
                speak("which recipe you are looking for?")
                query = parseCommand().lower()
                speak(Recipe.search_recipes(query))
                print(Recipe.search_recipes(query))

            elif "youtube" in query:
                yt.play_on_youtube(query)
            # this will stop the code right now we don't close it now on windows
            elif "stop" and "music" in query:
                yt.close_song()

            elif "home" and "temperature" in query:
                speak("reading the temperature and humidity of the house")
                m = hometemp.house_temperature()
                print(m)

            elif "tweet" in query:
                speak("opening application for tweets. Please wait")
                query = parseCommand().lower()
                Tweet.send_tweet()

            elif "home" and "temp fahrenheit" in query:
                speak("reading temperature in fahrenheit")
                print("reading temperature in fahrenheit")
                fahren.temp_f()

