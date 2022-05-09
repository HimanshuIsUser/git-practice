import time
from functools import lru_cache
@lru_cache(maxsize=4)
def news(n):
    time.sleep(n)
    print("here is the news")

news(3)
print("what about interantionsal news:-",input())
news(2)
print("local news")
news(3)
news(2)
news(3)