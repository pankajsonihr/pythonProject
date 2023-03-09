import pywhatkit as kit
import pyttsx3 as tts
from Speak import speak
from selenium import webdriver
def play_on_youtube(song_name):
    In = song_name
    v= tts.init()
    kit.playonyt(In)
    speak(f"Playing {In} On youtube")

#def close_song():
    #no code for now.





# this code is for raspberrypi to stop the browser
#import psutil

# find all Chromium processes
#for process in psutil.process_iter():
#    try:
#        # get process details as a named tuple
#        process_info = process.as_dict(attrs=['pid', 'name'])
#
#        # check if the process is a Chromium process
#        if 'chromium' in process_info['name']:
#            # terminate the process
#            process.terminate()
#    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#        pass