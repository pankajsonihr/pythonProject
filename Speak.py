import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text, rate = 180):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()