import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import urllib.parse
import re
import time
import threading

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # slower and natural
newsapi_key = "6b444347cf7546afa955f8ab678495d8"

# Thread-safe speak function
def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    t = threading.Thread(target=run)
    t.start()
    t.join()  # wait until speaking finishes before moving on

def play_youtube(song_name):
    query = urllib.parse.quote(song_name)
    url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(url)
    if response.status_code == 200:
        video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
        if video_ids:
            video_url = f"https://www.youtube.com/watch?v={video_ids[0]}"
            webbrowser.open(video_url)
            speak(f"Playing {song_name} on YouTube")
        else:
            speak("Could not find the song on YouTube.")
    else:
        speak("Unable to access YouTube at the moment.")

def processCommand(c):
    c_lower = c.lower()
    if "open google" in c_lower:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif "open facebook" in c_lower:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")
    elif "open instagram" in c_lower:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram.")
    elif "open linkedin" in c_lower:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn.")
    elif c_lower.startswith("play"):
        song = c_lower.replace("play ", "").strip()
        if song:
            play_youtube(song)
        else:
            speak("Please tell me the song name.")
    elif "news" in c_lower:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi_key}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])[:5]
                if articles:
                    speak("Here are the top headlines for today.")
                    for article in articles:
                        title = article["title"]
                        print(title)
                        for part in re.split(r'[.,;:]', title):
                            part = part.strip()
                            if part:
                                speak(part)
                                time.sleep(0.3)
                else:
                    speak("No news found.")
            else:
                speak("Unable to fetch news at the moment.")
        except Exception as e:
            print("Error fetching news:", e)
            speak("Sorry, I cannot fetch news right now.")

def listen(timeout=10, phrase_time_limit=7, prompt=None):
    """Listen and return recognized text"""
    if prompt:
        speak(prompt)
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            return ""
    try:
        text = recognizer.recognize_google(audio)
        print(f"Heard: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Recognition error: {e}")
        return ""

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        word = listen(timeout=15, phrase_time_limit=10)
        if "jarvis" in word:
            # Using thread-safe speak now
            speak("Ya")
            command = listen(prompt="I am listening...", timeout=15, phrase_time_limit=15)
            if command:
                processCommand(command)
