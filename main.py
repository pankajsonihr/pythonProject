import random

import speech_recognition as sr
from datetime import datetime
import pyttsx3
import webbrowser
import json
import wikipedia
import Wolframalpha as wf
from News import *
from Weather import *
import Bulb as sb
import randfacts

engine = pyttsx3.init()
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
activationWord = 'hello buddy' #single word
responses = json.loads(open('responses.json').read())
def search_wikipedia(query):
    searchResults = wikipedia.search(query)
    if not searchResults:
        print('No wikipedia result')
        return 'No wikipedia result'
    try:
        wikiPage = wikipedia.search(query)
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary
def speak(text, rate = 180):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print("Listening for a command")

    with sr.Microphone() as source:
        listener.energy_threshold = 10000  # it listen low voices as well
        listener.adjust_for_ambient_noise(source,1.2)
        input_speech = listener.listen(source)

    try:
        print("Recognizing speech...")
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f"The input speech was: {query}")
    except Exception as exception:
        print('I did not quite catch that')
        #speak('I did not quite catch that')
        print(exception)
        return "None"
    return query


def json_response(tag):
    for item in responses["chat"]:
        if item["tag"] ==tag:
           return item["responses"]


#Main Loop
if __name__ == '__main__':
    speak('Starting c p i n buddy')
    while True:
        #List Commands
        query = parseCommand().lower().split()
        if "hi" and "buddy"in query:
            speak('Activated')
            query = parseCommand().lower().split()
            if "your" and "name" in query:
                speak(random.choice(json_response("name")))

            elif "say" and "hello" in query:
                speak(random.choice(json_response("greetings")))
            #Navigation to open web browser

            elif 'go' and 'to' in query:
                speak('Opening..')
                query = ''.join(query[2:])
                webbrowser.open_new(query)
            #wolframAlpha
            elif query[0] == 'calculate' or query[0] == 'compute':
                query = ''.join(query[1:])
                speak('Computing')
                try:
                    result = wf.search_wolfram(query)
                    speak(result)
                except:
                    speak("Sorry I can't compute it.")
            #will read some news for user
            elif 'news' in query:
                get_news= news()
                speak(get_news[random.randint(0,len(get_news))])
                speak(get_news[random.randint(0, len(get_news))])

            #this will give random facts to user
            elif "random" and "fact" in query:
                speak("Sure sir, I will find some interesting facts for you.")
                rngfacts =randfacts.get_fact()
                speak("Did you know that, "+rngfacts)

            #weather info
            elif "temperature" in query:
                speak(f"current temperature in sudbury is "+str(temp()))

            elif "activate" and "bulb" in query:
                if any(arg in ['on', 'off', 'red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'black', 'white'] for arg in query):
                    sb.bulb_commands(query)
                else:
                #if "on" in query or "off" in query or "red" in query or
                    speak("I think we didn't got you.")
                    speak("say turn on to light the bulb, or say turn off to turn it off" )
                    speak("to change color tell me the color name only")
                    query = parseCommand().lower().split()
                    sb.bulb_commands(query)
            #jokes
            #if "joke" or "jokes" in query:
            #    speak("Sure sir, get ready for some chukles")
            #    joke = joke()
            #    speak(joke[0])
            #    speak(joke[1])
            #speak("I am going to get some sleep, but don't worry, if you need something wake me, by saying hello buddy")

            #responses thanks responses press the button and say some one on the door check that if there is a person on the door
            # or there is any object in front of door and send email only if its a person.
            #call emergency means send a text or email to a specific person.
            #edit crontab to create an alarm at a specific time
                #https://www.geeksforgeeks.org/crontab-in-linux-with-examples/
                #https://crontab.guru/
                #cron tab for alarms in python
                #https://www.timeapi.io/swagger/index.html to check the current time or find something for free
                # curl -X 'GET' \
            #       'https://www.timeapi.io/api/Time/current/ip?ipAddress=54.39.163.38' \
            #       -H 'accept: application/json'
            #https://www.timeapi.io/api/Time/current/ip?ipAddress=54.39.163.38 to get the current time in weblink rather than curl

