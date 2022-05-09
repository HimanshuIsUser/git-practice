import datetime
import time
from pygame import mixer
def physical():
    while True:
        mixer.init()
        mixer.music.load('Cant Be Touched.mp3')
        mixer.music.play()
        with open("physical programme.text","a") as pp:
            data = datetime.datetime.now()
            pp.write(str(data)+' :- ')
            pp.write(input("enter Physical to feed your activity :- ")+'\n')
            mixer.music.stop()
            break
             #2880 seconds for every 45 mins break