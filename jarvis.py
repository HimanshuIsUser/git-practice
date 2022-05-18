import winsound
import sounddevice as noise
from scipy.io.wavfile import write
import smtplib
import os
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3
# speak function
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[0].id)
engine.setProperty('voices',voice[0].id)

# sound recorder function
def soundrecoder(durt):
    freq = 44100
    duration = int(durt)
    recording = noise.rec(int(duration*freq),
                          samplerate=freq,channels=2)
    noise.wait()
    file_name = input("enter the your file name : ")
    write(file_name,freq,recording)
#play any sound by there name :
def playsound(name):
    winsound.PlaySound(name,winsound.SND_FILENAME)

# send email function

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('himanshubansal9818812568@gmail.com','@HIMANSHU98188')
    server.sendmail('himanshubansal9818812568@gmail.com ',to,content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif(hour>=12 and hour<18):
        speak("good afternoon")
    else:
        speak("good evening")
    speak(" jarvis here..")
def takecommand():
    # help to convert input of oral words to string
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("jarvis...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f'user said: {query}\n')
    except Exception as e:
        print(e)
        print("say that again")
        return "none"
    return query
if __name__ == '__main__':
    speak("welcome to the jarvis world")
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching... wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif ('open youtube' in query):
            webbrowser.open("youtube.com")
        elif ('open google' in query):
            webbrowser.open("google.com")
        elif ('open github' in query):
            webbrowser.open("git hub.com")
        elif ('play music') in query:
            music_dr = 'D:\\music'
            song = os.listdir(music_dr)
            print(song)
            os.startfile(os.path.join(music_dr, song[0]))
        elif ('email') in query:
            try:
                speak("what should i say?")
                conttent = takecommand()
                to = "himanshub166@gmail.com"
                sendEmail(to, conttent)
                speak("email has been send")
            except Exception as e:
                print(e)
                print("ERROR! check your less secure app should be ON")
        elif ('take your break') in query:
            print("thank you sir")
            speak("thank you sir")
            break
        elif('play sound') in query:
            try:
                name = input("enter the your file name : ")
                speak("enter the your file name")
                playsound(name)
            except Exception as e:
                print(e)
                print("check your file name")
        elif('start recording')in query:
            try:
                durt = input("enter the duration of your recording : ")
                soundrecoder(durt)
            except Exception as e:
                print(e)
        else:
            continue