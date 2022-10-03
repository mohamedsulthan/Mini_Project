import sys
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')  # getting details of current voice
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def file(fi, t):
    d = ".txt"
    ext=['.pdf','.txt','.py']
    f = open(fi+d, "a")
    f.write(t)
    f.close()


def crf():
    speak("output file name sir")
    speech2 = speech_()
    f = open(speech2, "a")
    return speech2
    f.close


def speech_():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        # if there any error use below code
        """#r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source, duration=1)

        #r.pause_threshold = 0.5"""

    try:
        speech2 = r.recognize_google(audio).lower()
        print('User: ' + speech2 + '\n')

    except sr.UnknownValueError:
        print('Sorry sir! TRY Writing your command Sir')
        speech2 = input('Command: ')

    return speech2


if __name__ == '__main__':

    speak("Enter the file name to save your text:")
    fi = input("Enter the file name to save:")
    while True:
        speech2 = speech_()
        speech2 = speech2.lower()
        if 'exit' in speech2:
            #sys.exit()
            sys.exit()
        else:
            file(fi, speech2)
