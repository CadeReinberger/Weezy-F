from gtts import gTTS, gTTSError
from playsound import playsound
import time
from configs import (try_online_first, num_wifi_retries, online_giveup_retries,
                     question_answer_time)
import pyttsx3
import os

#this is a somewhat crappy way of getting enum-style syntax
class speak_modes:
    online = 'online'
    offline = 'offline'
    
global engine, tot_num_retries, speak_mode
    
engine = None
tot_num_retries = 0

engine = pyttsx3.init()
speak_mode = speak_modes.online if try_online_first else speak_modes.offline
    
def online_speak(words):
    try:
        tts = gTTS(text=words, lang='en')
        if os.path.exists('cur.mp3'):
            os.remove('cur.mp3')
            tts.save('cur.mp3')
    except gTTSError:
        return False
    playsound('cur.mp3')
    return True

def offline_speak(words):
    engine.say(words)
    engine.runAndWait()

def speak(words):
    global engine, tot_num_retries, speak_mode
    if speak_mode == speak_modes.online:
        retries = 0
        while not online_speak(words):
            retries += 1
            tot_num_retries += 1
            if tot_num_retries > online_giveup_retries:
                speak_mode = speak_modes.offline
                offline_speak(words)
                break
            if retries > num_wifi_retries:
                offline_speak(words)
                break
        return
    offline_speak(words)
    
def speak_question(q):
    speak(q.q)
    time.sleep(question_answer_time)
    speak(q.a)
    