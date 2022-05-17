import smtplib
import os
import webbrowser
import wikipedia
import datetime
import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[0].id)
engine.setProperty('voices',voice[0].id)
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourname@gmail.com','your-password here')
    server.sendmail('youremail@gmail.com',to,content)
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
    speak(" I am manish sir.")
def takecommand():
    # help to convert input of oral words to string
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("listening..")
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
    speak("harry is a good boy")
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("searching... wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif('open youtube' in query):
            webbrowser.open("youtube.com")
        elif('open google'in query):
            webbrowser.open("google.com")
        elif('open github'in query):
            webbrowser.open("git hub.com")
        elif('play music') in query:
            music_dr = 'D:\\music'
            song = os.listdir(music_dr)
            print(song)
            os.startfile(os.path.join(music_dr,song[0]))
        elif('email')in query:
            try:
                speak("what should i say?")
                conttent = takecommand()
                to = "himanshub166@gmail.com"
                sendEmail(to,conttent)
                speak("email has been send")
            except Exception as e:
                print(e)
                print("sorry yr i am not able to send email")

