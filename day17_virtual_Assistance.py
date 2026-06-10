import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
name = input("Enter your name :")
engine = pyttsx3.init()

def speak(text):
    engine.say("charan haleluya")
    engine.runAndWait()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
       print("Recognizing...")
       command = recognizer.recognize_google(audio)
       print("You said:", command)
       return command.lower()
    except Exception:
        print("Sorry, Plese say that again")
        return ""
def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak(f"Good Morning{name}\nIam your virtual assistance")
        
    elif hour < 18:
        speak(f"Good Afternoon{name}\nIam your virtual assistance")

    else:
        speak(f"Good Evening{name}\nIam your virtual assistance")


wish_user()

while True:
    command = take_command()
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "open youtube" in command:
        webbrowser.open("http://www.youtube.com")

    elif "open google" in command:
        webbrowser.open("http://www.google.com")
    elif "open instagram" in command:
        webbrowser.open("http://www.instagram.com")

    elif "who is" in command:
        person = command.replace("who is ","")
        info = wikipedia.summary(person, 2)
        print(info)
        speak(info)

    elif "exit" in command:
        speak("Goodbye")
        break

gana()
while True:
    com = take_command()
    hour = datetime.datetime.now().hour
    if hour <12 and com == "good afternoon" or "good evening":
        print("it is morning now")
        break




















