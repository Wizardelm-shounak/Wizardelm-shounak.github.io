from winreg import QueryInfoKey
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
import sys


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.setProperty('rate',190)

def voiceChange():
    eng = pyttsx3.init() #initialize an instance
    voice = eng.getProperty('voices') #get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    eng.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
    eng.say("This is a demonstration of how to convert index of voice using pyttsx3 library in python.") #say method for passing text to be spoken
    eng.runAndWait() #run and process the voice command


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)


    if hour>=0 and hour<12:
        speak("Good Morning sir!")


    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")


    else:
        speak("Good Evening sir!")
    speak("All system for you will be prepared in a few minutes, for now , you feel free to grab a cup of coffee , and have  a good day")       


def takeCommand():
    r = sr.Recognizer()
    
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, )
    
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    
    except Exception as e:
        print("Say that again please...")  
        return "None"
    
    
    return query.lower()


# Define a dictionary with example questions and answers
stringVar = { "what" and "name": "ma name is joe ",
    
     
    "what is your name": "My name is Jarvis",

    "what's your name": "My name is Jarvis",

    "can I have your name": "My name is Jarvis",

    "what would your name be": "My name is Jarvis",

    "what can I call you": "you can call me Jarvis",

    "what do you call yourself": "Jarvis , I am jarvis",
    
    
    "who created you": "I was created by Mr. Krishna",
    
    
    "what can you do": "I can perform tasks like searching on Wikipedia, opening websites like Google and YouTube, and playing videos on YouTube",
    
    
    "what time is it": "It is currently " + datetime.datetime.now().strftime("%I:%M %p"),
    
    
    "tell me more about you": "Hello, I'm Jarvis, My code was made by Parikshit Raj Karn, my body and appearence was managed by Krishna Panjrekar, Though, I got no soul but I got emotions, Thank you",
    
    
    "thank you jarvis": "You're welcome"
}

def jarvisResponse(query):
    
    
    if query in stringVar:
        speak(stringVar[query])
    
    
    elif 'wikipedia' in query:
        speak('Searching...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    
    elif 'open google' in query:
        webbrowser.open("google.com")
    
    
    elif 'play a song' in query:
        webbrowser.open("https://www.youtube.com/watch?v=kt14c7sYTFA")

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

        
    elif 'jarvis please leave' in query or 'bye' in query:
        speak("GoodBye! See you later, it was nice time with you")
        sys.exit()

    
    elif 'google search' in query:
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        result = webbrowser.open("https://www.google.com/search?q=" + query)
        speak("")

    
     
    else:
        speak("I'm sorry, I didn't quite catch that. Could you please repeat?")

    
    
if _name_ == "_main_":
    wishMe()
    while True:
        query = takeCommand()
        if query == "none":
            continue
        else: 
            query is not None
            jarvisResponse(query)