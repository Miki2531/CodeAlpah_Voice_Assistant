import requests
import wikipedia
import pywhatkit as kit
from decouple import config

NEW_API_KEY = config("NEWS_API_KEY")
OPENWEATHER_API_KEY = config("OPENWEATHER_APP_ID")
CITY = config("CITY")

def find_my_api():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, senteces=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)


def get_latest_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={NEW_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

def get_weather_report(city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHER_API_KEY}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

def get_random_jock():
    headers = {
        'Accept': 'applicatiion/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']