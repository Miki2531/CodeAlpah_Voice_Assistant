import requests
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


USERNAME = config("USER")
BOTNAME = config("BOTNAME")


class Assistant:

    def __init__(self):
        self.engine = self.pyttsx3.init('sapi5')

        # set rate
        self.engine.setProperty('rate', 190)

        # set volume
        self.engine.setProperty('volume', 1.0)

        # set Voice (Female)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        self.root = tk.Tk()
        self.label = tk.Lable(text = "BOTNAME", font=("Aerial", 120, "bold"))
        self.label.pack()
        
        threading.Thread(target=self.run_assistant).start()


        self.root.mainloop()


    def run_assistant(self):
        pass