import datetime
from pygame import mixer
def eye():
    for i in range(1):
        mixer.init()
        mixer.music.load('Gulabi Aankhen Jo Teri Dekhi Remix Song.mp3')
        mixer.music.play()
        while True:
            with open("eye file.text","a") as ep:
                data=datetime.datetime.now()
                ep.write(str(data)+' :- ')
                ep.write(input("enter eye to feed your activity :- ")+"\n")
                mixer.music.stop()
                break
