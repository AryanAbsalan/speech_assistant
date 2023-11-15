import speech_recognition as speech_rec 
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

from gtts import gTTS 
import yfinance as yf 

import random
import os 
from time import ctime 
import time
import webbrowser 

class person:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

recognizer = speech_rec.Recognizer() # initialise a recogniser

# listen for audio and convert it to text:
def record_audio(ask=False):
    with speech_rec.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = recognizer.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            # convert audio to text
            voice_data = recognizer.recognize_google(audio, language="en-US") 
        except speech_rec.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except speech_rec.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(f"User: {voice_data.lower()}") # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    random_num = random.randint(1,20000000)
    audio_file_name = 'audio' + str(random_num) + '.mp3'
    tts.save(audio_file_name) # save as mp3
    # Get the current working directory
    current_directory = os.getcwd()
    # Construct the full path to the audio file
    audio_file_path = os.path.join(current_directory, audio_file_name)
    # Play the audio file using playsound
    playsound(audio_file_path)

    # # Load the MP3 file using pydub
    # audio_segment = AudioSegment.from_mp3(audio_file_path)

    # # Play the MP3 file
    # play(audio_segment)

    print(f"GTTS: {audio_string}") # print what app said
    os.remove(audio_file_path) # remove audio file

def respond(voice_data):
    # 1: greeting
    if there_exists(['hey','hi','hello']):
        greetings = [f"hey, how can I help you {person.name}", 
                     f"hey, what's up? {person.name}", 
                     f"I'm listening {person.name}", 
                     f"how can I help you? {person.name}", 
                     f"hello {person.name}, how can I help you?",
                     f"hello {person.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    if there_exists(["what is your name","what's your name","tell me your name"]):
        if person.name:
            speak("my name is GTTS")
        else:
            speak("my name is GTTS. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person.setName(person_name) # remember name in person object

    # 3: greeting
    if there_exists(["how are you","how are you doing"]):
        speak(f"I'm very well, thanks for asking {person.name}")

    # 4: time
    if there_exists(["what's the time","tell me the time","what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    # 7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.lower().split(" of ")[-1].strip() #strip removes whitespace after/before a term in string
        stocks = {
            "apple":"APPL",
            "microsoft":"MSFT",
            "facebook":"FB",
            "tesla":"TSLA",
            "bitcoin":"BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]

            speak(f'price of {search_term} is {price} {stock.info["currency"]} {person.name}')
        except:
            speak('oops, something went wrong')

    # 8: search google Image
    if there_exists(["find image"]):
        search_term = voice_data.split("for")[-1]
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 9: search google location
    if there_exists(["find location"]):
        location = voice_data.split("for")[-1]
        url = f"https://www.google.com/maps/dir/{location}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {location} on google')

    # 9: search google location
    if there_exists(["wikipedia"]):
        word = voice_data.split("wikipedia")[-1]
        url = f"https://en.wikipedia.org/wiki/{word}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {word} on wikipedia')

    # 10: search google location
    if there_exists(["bing"]):
        word = voice_data.split("bing")[-1]
        url = f"https://www.bing.com/search?q={word}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {word} on bing')

    if there_exists(["exit", "quit", "goodbye"]):
        speak("going offline")
        exit()

time.sleep(1)

person = person()
while True:
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond


