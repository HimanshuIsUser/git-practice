import datetime
from time import time
from pygame import mixer
def water():
    mixer.init()
    mixer.music.load('Pinjraa Punjabi Mp3 Song By Gurnazar.mp3')
    mixer.music.play()
    while True:
        with open("water data.text","a")as wd:
            data = datetime.datetime.now()
            wd.write(str(data) + ' :- ')
            wd.write(input("enter drunk to stop the alert\n")+"\n")
            mixer.music.stop()
            break

# watertime = time()
# watersec = 1*20
# while True:
#     if time() - watertime > watersec:

