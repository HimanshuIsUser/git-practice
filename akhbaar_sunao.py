# from win32 import
# speak = dispatch("SAPI.Spvoice")
# speak.speak(Str)
# speak("mohan")
# import subprocess
# def execute_unix(inputcommand):
#     p = subprocess.Popen(inputcommand,stdout=subprocess.PIPE,shell=True)
#     (output,err) = p.communicate()
#     return output
# a = "hello"
# execute_unix(a)
# import pyttsx3
# speak = pyttsx3.init()
# t = input("WRITE SOME THING :-")
# speak.say(speak)
# speak.runAndWait()
# from gtts import gTTS
# import os
# s = input("write something")
# file = "file.mp3"
# tts = gTTS(s,'en')
# tts.save(file)
# os.system("mpg123"+file)
import requests
import json
def lou_d(str):
    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    request = requests.get('https://newsapi.org/v2/top-headlines?'
                           'pagesize=10&'
                           'country=in&'
                           'language=en&'
                           'apiKey=c33ff6b689b2420c8625a08f784306ef').text
    art = json.loads(request)
    # print(art['articles'])
    news = art['articles']
    for articles in news:
        i=1
        if i<=9:
            print(articles['title'])
            lou_d(articles['title'])
lou_d("thank you")