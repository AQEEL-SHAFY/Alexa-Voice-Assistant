import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit

# To recognize the voice
listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')  # To change the voice of alexa
engine.setProperty('voice', voice[1].id)
engine.say('Hello I am your Alexa')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        # source of the audio
        with sr.Microphone() as source:
            print('Alexa Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # print(command) # if needed to repeat the same thing
                print(command)


    except:
        pass

    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        print('Alexa Playing Song')
        talk('Alexa Playing' + song)
        pywhatkit.playonyt(song)  # play songs from YouTube

    elif 'hello' in command:
        print('Hello')
        talk('Hello How Can I Help You')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    else:
        talk('Please Say it again')


while True:
    run_alexa()
