import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pyautogui
import pyjokes

engine = pyttsx3.init()

def speak (audio):

    engine.say(audio)
    engine.runAndWait()

def time():
    speak("the current time is")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    speak("the current date is")
    year = int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome Back Pratik Bhai!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12 :
        speak("Good Morning Bhai")
    elif hour >= 12 and hour <18 :
        speak("Good Afternoon Bhai")
    elif hour >= 18 and hour <24 :
        speak("Good Evening Bhai")

    else:
        speak("Good night Bhai")

    speak("Jarvis at your service, Kya Help Karu Pratik Bhai?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ruk...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Ruk ja....")
            query = r.recognize_google(audio, language='en-in')
            print(query)

        except Exception as e:
            print(e)
            speak("Ye kya bol raha hai bhai")

            return "None"

        return query


def screenshot():
    img = pyautogui.screenshot()
    img.save("Z:\\ss\\ss2.png")

def joke():
    speak(pyjokes.get_joke())

if __name__== "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Ruk ja...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'search in Chrome' in query:
            speak("What Should I search?")

            chromepath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s'

            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'Shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play song' in query:
            songs_dir = 'Z:\music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'remember me' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that"+remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'tell me a joke' in query:
            joke()
