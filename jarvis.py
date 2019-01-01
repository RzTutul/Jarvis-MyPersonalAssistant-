import ctypes
from gtts import gTTS
import pyttsx3

import os
import random
import webbrowser
import speech_recognition as sr
from playsound import playsound

speech = sr.Recognizer()

greeting_dict = {'hello': 'hello', 'hi': 'hi'}
open_lunch_dict = {'open': 'open', 'lunch': 'lunch'}
social_media_dict = {'facebook': 'https://www.facebook.com', 'twitter': 'https://www.twitter.com','youtube': 'https://www.youtube.com'}

open_play_dict = {'play': 'play', 'play': 'play'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which'}
google_searches_dict1 ={'search': 'search'}

mp3_greeting_list = ['mp3/voiceList/gretting1.mp3', 'mp3/voiceList/gretting1.mp3']
mp3_opening_list = ['mp3/voiceList/open_1.mp3', 'mp3/voiceList/open_1.mp3']
mp3_bye_list = ['mp3/voiceList/bye.mp3', 'mp3/voiceList/bye.mp3']
mp3_search_list = ['mp3/voiceList/search_1.mp3', 'mp3/voiceList/search_1.mp3']
mp3_listen_problem = ['mp3/voiceList/listening_problem_1.mp3', 'mp3/voiceList/listening_problem_2.mp3']
mp3_thank_you = ['mp3/voiceList/thankyou_1.mp3', 'mp3/voiceList/thankyou_2.mp3']




def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


def read_voice_cmd():

    voice_text = ''
    print('Listening...')



    try:

        with sr.Microphone() as source:
          audio = speech.listen(source=source, timeout=5, phrase_time_limit=6)
          voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        error_occer = 0
        if error_occer == 0:
            play_sound(mp3_listen_problem)
            error_occer+=1
        elif error_occer == 1:
            play_sound(mp3_listen_problem)

    except sr.RequestError as e:
        print('Network error.')

    except sr.WaitTimeoutError:
        pass
    return voice_text

def is_valid_google_search(phrase):
    if(google_searches_dict1.get(phrase.split(' ')[0])==phrase.split(' ')[0]):
        return True

def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():

        try:
            if value == voice_note.split(' ')[0]:
                return True

            elif key == voice_note.split(' ')[1]:
                return True

        except IndexError:
            pass

    return False



if __name__ == '__main__':

    #playsound('mp3/voiceList/hello_sir.mp3')

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    volume = engine.getProperty('volume')
    engine.setProperty('volume',  -0.25)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say("hey I'm Your personal Assistent how can help you!")
    engine.runAndWait()
    engine.stop()




    while True:
        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))

        if is_valid_note(greeting_dict, voice_note):
            print('In greeting...')
            play_sound(mp3_greeting_list)
            continue

        elif is_valid_note(open_lunch_dict, voice_note):
            print('opening...')
            play_sound(mp3_opening_list)
            if (is_valid_note(social_media_dict, voice_note)):
                # Launch Facebook
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('shutdown /s')
             #os.startfile('H:\\12.Strong.2018.1080p.BluRay.H264.AAC-RARBG')
             ##os.system('explorer C:\\"{}"'.format(voice_note.replace('open ','')))




            continue
        elif is_valid_google_search(voice_note):
            print('In google Searching...')
            play_sound(mp3_search_list)
            x = voice_note.split(' ', 1)
            x1 = x[1]

            webbrowser.open('https://www.google.com/search?q={}'.format(x1))
            continue

        elif is_valid_note(open_play_dict , voice_note):
            print('In google Searching...')
            play_sound(mp3_search_list)
            webbrowser.open('https://www.google.com/search?q={}'.format(voice_note))

        elif 'lock' in voice_note:
          for value in ['pc', 'system', 'windows']:
             ctypes.windll.user32.LockWorkStation()





        elif 'thank you' in voice_note:
            print('Thank you sir')
            play_sound(mp3_thank_you)

        elif 'by' in voice_note:
            play_sound(mp3_bye_list)
            exit()
        else:
            play_sound(mp3_listen_problem)
