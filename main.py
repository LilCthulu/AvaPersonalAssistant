import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import time
import warnings
import openai
import pyaudio
from tkinter import *

## Gui config
## window config
#window = Tk()
#window.title('Jarvis')
#window.geometry('400x500')
## gui elements
#main_menu = Menu(window)
#main_menu.add_command(label='Exit')
#window.config(menu=main_menu)
#window.mainloop()
## Jarvis config

# Initialize OpenAI API
openai.api_key = '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'

print('Ava initializing')

warnings.filterwarnings('ignore')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Functions


# Speak function custom made to say the str you pass to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Variable spoken greeting function based on time of day
def TimeGreet():
    hour = int(datetime.datetime.now().hour)

    if hour >= 4 and hour < 12:
        speak('Good morning Mister Carbis. How can I assist you.')
        print('Good morning Mister Carbis. How can I assist you.')

    elif hour >= 12 and hour < 18:
        speak('Good afternoon mister Carbis. How can I assist you.')
        print('Good afternoon Mr. Carbis. How can I assist you.')

    else:
        speak('Good Evening Mister Carbis. How can I assist you.')
        print('Good Evening Mister Carbis. How can I assist you.')

# Function for taking commands from user mic
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

    try:
        print('Thinking...')
        query = r.recognize_google(audio, language='en-us')
        print(f' {query}\n')

    except Exception as e:
        speak("I'm sorry i didn't quite catch that")
        print("I'm sorry i didn't quite catch that")
    return query


# Function for user recognition... kinda
def GetUser():
    speak('Hello... who are you?')
    print('Hello... who are you?')
    if 'Chaz' in TakeCommand():
        TimeGreet()

    else:
        speak('You are not my primary user. What was your name again?')
        print('You are not my primary user. What was your name again?')
        name = TakeCommand()
        speak(f'hello {name}. How can i assist you?')
        print(f'hello {name}. How can i assist you?')

# Function for getting date
def getDate():
    now = datetime.datetime.now()
    (datetime.datetime.today())
    monthNum = now.month
    dayNum = now.day

    # A list of months
    month_names = ['January', 'February', 'March', ' April', 'May', 'June', 'July', 'August', 'September', ' October',
    'November', 'December']

    # A list of ordinal Numbers
    ordinalNumbers = ['1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
    '14th', '15th', '16th','17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24rd', '25th', '26th', '27th', '28th',
    '29th', '30th', '31st']

    speak('Today is ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1])
    print('Today is ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1])


def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=1,
    )
    return response['choices'][0]['text']

# Main Program
# Jarvis 'brain'

speak('Ava Initializing...')
GetUser()

def main():
    query = TakeCommand()

    # Logic for handling queries
    if 'open youtube' in query.lower():
        webbrowser.open('www.youtube.com')
        speak('No problem')
        print('No problem')
    
    elif 'open my email' in query.lower():
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
        speak('No problem')
        print('No problem')

    elif 'listen to music' in query.lower():
        path = r'C:/Users/karat/AppData/Local/Microsoft/WindowsApps/Spotify.exe'
        os.system(path)
        speak('No problem')
        print('No problem')

    elif 'the time' in query.lower():
        time_now = datetime.datetime.now().strftime('%H:%M')
        (hour, minute) = time_now.split(':')
        if int(hour) > 12:
            hour = int(hour) - 12
            btrTime = str(hour) + ' ' + str(minute)
        speak(f'It is currently {btrTime}')
        print(f'It is currently {btrTime}')

    elif 'my projects' in query.lower():
        path = 'C:/Users/karat/Code'
        os.startfile(path)
        speak('No problem')
        print('No problem')

    elif 'the date' in query.lower():
        get_date = getDate()
        speak(get_date)
        print(get_date)

    else:
        response = generate_response(query)
        speak(response)
        print(response)

while True:
    main()
