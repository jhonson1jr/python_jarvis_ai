import requests
import wikipedia
import pywhatkit as kit

def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return ip_address['ip']

def search_on_wikipedia(query):
    resultado = wikipedia.summary(query, sentences = 2)
    return resultado

def search_on_google(query):
    kit.search(query)

def search_on_youtube(video):
    kit.playonyt(video)