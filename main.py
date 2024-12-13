import pyttsx3
import speech_recognition as sr
import keyboard
import os
import subprocess as sp

from datetime import datetime
from decouple import config
from random import choice
from conv import random_text

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 225)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 1 é a voz feminina

USER     = config('USER')
HOSTNAME = config('BOT')

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

def greet_me():
    hora = datetime.now().hour
    if (hora>=6) and (hora <= 12):
        falar(f"Good morning {USER}")
    elif (hora>=12) and (hora <= 16):
        falar(f"Good afternoon {USER}")
    elif (hora>=16):
        falar(f"Good evening {USER}")
    falar(f"I am {HOSTNAME}. How may I assist you {USER}?")

listening = True
def start_listening():
    global listening
    listening = True
    print('Started listening')

def pause_listening():
    global listening
    listening = False
    print('Stopped listening')

keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(query)
        if not "stop" in query or "exit" in query:
            falar(choice(random_text))
        else:
            hora = datetime.now().hour
            if hora >= 21 and hora < 6:
                falar("Good night Sir, take care.")
            else:
                falar("Have a good day Sir.")
            exit()
    except Exception:
        falar("Sorry I could not understand. Can you repeat that using different words?")
        query = 'None'
    return query

greet_me()
while True:
    if listening:
        query = take_command().lower()
        if "how are you" in query:
            falar("I am absolutely fine Sir. What about you?")
        elif "open command prompt" in query:
            falar("Opening command prompt...")
            os.system('start cmd')
        elif "open camera" in query:
            falar("Opening camera...")
            sp.run('start microsoft.windows.camera:', shell=True)
        elif "open discord" in query:
            falar("Opening Discord...")
            discord_path = "C:\\Users\\Jhon\\AppData\\Local\\Discord\\app-1.0.9174\\Discord.exe"
            os.startfile(discord_path)

