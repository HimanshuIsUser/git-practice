import exerwater
import exereye
import exerphysical
import datetime
from time import time

init_water = time()
eyetime = time()
physicaltime = time()
watersec = 10
eyesec=20
physicalsec=25
while True:
    if time() - init_water > watersec:
        print(exerwater.water())
        init_water = time()
    if time() - eyetime > eyesec:
        print(exereye.eye())
        eyetime = time()
    if time() - physicaltime > physicalsec:
        print(exerphysical.physical())
        physicaltime = time()