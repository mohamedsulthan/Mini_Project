import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import datetime
import wolframalpha
import os
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# pyttsx3,Text to speech conversion module
# usage of pyttsx3 (belove are deafult code to set it)
"""engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()"""

engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[len(voices) - 1].id)  # changing index, changes voices. o for male,1 for female

"""Wolfram Alpha is an API which can compute expert-level answers using Wolfram's algorithms, knowledgebase and AI technology"""
client = wolframalpha.Client('GTE8EA-7AX8EQT7JH')  # my own login ID in wolfarmalpha website


def speak(audio):
    print('Regi:' + audio)
    engine.say(audio)
    engine.runAndWait()


# speak("General MS")
speak('I am your assistant Regi,How may I help you?')
# speak('Do you want to play Multi player Game,tic tac toe? then say \'open it\' ')
speak('say something, sir')


# obtain audio from the microphone
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        # if there any error use below code
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 0.5

    try:
        speech1 = r.recognize_google(audio).lower()
        print('User: ' + speech1 + '\n')

    except sr.UnknownValueError:
        speak('Sorry sir! TRY Writing your command Sir')
        speech1 = input('Command: ')

    return speech1


def random_music():
    lst = os.listdir("C:\\Users\MSP\\Music")
    folder = "C:\\Users\\MSP\\Music\\"
    random_music = (folder + random.choice(lst[1:]))
    os.system(random_music)


def music():
    speak("select song, sir")
    lst = os.listdir("C:\\Users\MSP\\Music")
    for i in lst:
        print(i)
    s = input("song name:")
    # playsound("C:\\Users\\MSP\\Music\\" + s)
    folder = "C:\\Users\\MSP\\Music\\"
    os.system(folder + s)


if __name__ == '__main__':

    while True:

        speech1 = speech()
        speech1 = speech1.lower()

        if 'help' in speech1 or 'basic commands' in speech1:
            speak("Listing basic commands sir")
            print("open youtube")
            print("open google")
            print("open gmail")
            print('open whatsapp')
            print("quotes")
            print('what time is it')
            print("what\'s up")
            print('take notes')
            print("play_music")
            print("'random song','random music','play some song regi'")
            print("'play a song regi','play this song',")
            print('send a mail')

        elif 'open youtube' in speech1:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in speech1:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'open gmail' in speech1:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif 'open it' in speech1:
            os.system('python D:\\Mini_Project\\X_O.py')
        elif 'quotes' in speech1:
            speak("General your favourite quote,once her love ruled my heart now her memories ruling my mind")
        elif "what\'s up" in speech1 or 'how are you' in speech1:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif 'nothing' in speech1 or 'exit' in speech1 or 'bye' in speech1:
            speak("Thank you, Have a nice day sir, bye")
            sys.exit()
        elif 'what time is it' in speech1 or 'what is the time regi' in speech1 or 'what time is it' in speech1 or 'time' in speech1 or 'current time' in speech1:
            speak('The current time is ' + (str(datetime.datetime.now().strftime('%H:%M:%S'))))
        elif 'what date is it' in speech1 or 'what is the date skava' in speech1 or 'what date is it' in speech1 or 'date' in speech1 or 'current date' in speech1:
            speak('The current time is ' + (str(datetime.datetime.now().strftime('%H:%M:%S'))))
        elif 'hello' in speech1 or 'hi' in speech1:
            speak('Hello General')
        elif 'take notes' in speech1:
            os.system('python D:\\Mini_Project\\notes.py')
        elif 'open whatsapp' in speech1:
            os.system("C:\\Users\\MSP\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

        elif 'random song' in speech1 or 'random music' in speech1 or 'play some song regi' in speech1 or 'play some song' in speech1:
            random_music()
        elif 'my choice' in speech1 or 'play this song' in speech1 or 'play a song regi' in speech1 or 'play a song' in speech1 or 'play song' in speech1:
            music()
        elif 'send a mail' in speech1 or 'mail' in speech1 or 'email' in speech1:
            speak("please type the receiver's email id,sir")
            receiver = input("receiver email:")
            from_address = 'edit here'
            to_address = receiver  # REPLACE with the to addresses you wish to send
            message = MIMEMultipart()
            message['From'] = from_address
            message['To'] = " ,".join(to_address)
            speak("Your Message, sir")
            message['subject'] = speech()
            speak("please tell the body of the email sir")
            body = speech()
            message.attach(MIMEText(body, 'plain'))
            email = 'edit here'
            password = 'edit here'
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(email, password)
            text = message.as_string()
            mail.sendmail(from_address, to_address, text)
            mail.quit()
            print("mail successfully send")
            speak("mail successfully send")

        else:
            text1 = speech1
            speak('Searching...')
            try:
                res = client.query(text1)
                results = next(res.results).text
                speak('getting results from google')
                speak('Got it.')
                speak(results)
            except:
                webbrowser.open('www.google.com')
        speak('any Command! Sir!')
