import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import pywhatkit
import pyjokes
import sys
import os
from requests import get

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
listener = sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("I am Jarvis. Please tell me how may I help you?")

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print("Recognizing...")
                print(f"User said: {command}\n")    

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return command


if __name__=="__main__" :
    greetings()
    while True:
    
        command = takeCommand().lower()

        if 'wikipedia' in command:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open notepad' in command:
            speak("Opening Notepad...")
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)

        elif 'open youtube' in command:
            speak("opening youtube...")
            webbrowser.open("youtube.com")

        elif "open google" in command:
            speak("Sir, what should I search on google?")
            search = takeCommand().lower()
            webbrowser.open(f"{search}")

        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "ip address" in command:
            ip = get('https://api.ipify.org').text
            print("Your IP address is"+ip)
            speak(f"Sir, your IP address is {ip}")

        elif 'sleep' in command:
            print("Thank you for using me, sir. Have a nice day!")
            speak("Thank you for using me, sir. Have a nice day!")
            break 
        
        elif 'belong' in command:
            print("I belong to Lord Subhrajit")
            speak("I belong to Lord Subhrajit")     