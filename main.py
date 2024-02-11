import tkinter as tk
from function.online_file import (
    find_my_api, search_on_google, search_on_wikipedia,
    play_on_youtube, get_weather_report, get_latest_news,
    get_random_advice, get_random_jock
    )
from function.os_file import open_calculator, open_camera, open_cmd
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime 
from random import choice
import threading
from utils import opening_text 
from pprint import pprint
import requests


USERNAME = config("USER")
BOTNAME = config("BOTNAME")


class Assistant:

    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.engine.setProperty('rate', 190)
        self.engine.setProperty('volume', 1.0)

        # set Voice (Female)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.root = tk.Tk()
        self.root.title('Voice Assistant')
        self.label = tk.Label(text="🤖", font=("Aerial", 120, "bold"))
        self.label.pack()
        
        threading.Thread(target=self.run_assistant).start()

        self.root.geometry("400x300")
        self.root.mainloop()

    def talk(self, audio):
        """Used to speak, the text is passed it."""
        self.engine.say(audio)
        self.engine.runAndWait()

    def greeting_user(self):
        """"Greeting the user accoriding to the hours."""
        hour = datetime.now().hour
        if 6 <= hour < 11 :
            self.talk(f"Good Morinig {USERNAME}")
        elif 11 <=hour < 17:
            self.talk(f"Good Afternoon {USERNAME}")
        elif 17 <= hour < 21:
            self.talk(f"Good Evening {USERNAME}")
        self.talk(f"I am {BOTNAME}.  How may I assist you.")

    # Take input from the user
    def run_assistant(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1 
            """Records a single phrase from source (an AudioSource instance) into an 
               AudioData instance, which it returns."""
            audio = r.listen(source)

        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language = "en-US")
            print(f"User said: {query}\n")
            if not 'exit' in query or 'stop' in query:
                self.talk(choice(opening_text))
            else:
                hour = datetime.now().hour
                if 21 <= hour or hour < 6:
                    self.talk("Good Night sir, Have a nice dream!")
                else:
                    self.talk('Have a good day sir!')
                exit()

        except Exception as e:
            print("Sorry, Unable to Recognize your sound. Could you please say that again?.", e)
            return "None"
        
        return query
    def process_query(self, query):
        if 'open command prompt' in query or 'open cmd' in query:
            open_cmd()
        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_api()
            self.talk(f"Your IP address is {ip_address}")

        elif 'wikipedia' in query:
            self.talk('What do you want to search on wikipedia, sir?')
            search_query = self.run_assistant().lower()
            results = search_on_wikipedia(search_query)
            self.talk(f"According to wikipedia, {results}")
            self.talk(f"For your comfort, I am priniting it on the screen sir.")
            pprint(results)

        elif 'youtube' in query:
            self.talk('What do you want on youtube to play, sir?')
            video = self.run_assistant().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            self.talk('What do you want to serach on google, sir?')
            query = self.run_assistant().lower()
            search_on_google(query)

        elif 'joke' in query:
            self.talk(f"I hope, you like this one, sir.")
            joke = get_random_jock()
            self.talk(joke)
            self.talk('For your comfort, I am priniting on the screen sir.')
            pprint(joke)

        elif "advice" in query:
            self.talk(f"Here's an advice for you, sir")
            advice = get_random_advice()
            self.talk(advice)
            self.talk("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

if __name__ == '__main__':
    assistant = Assistant()
    assistant.greeting_user()
    query = assistant.run_assistant().lower()
    assistant.process_query(query)
