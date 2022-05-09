# import requests
# request = requests.get("https://www.overpipe.com/")
# print(request.text)
# url = "http://www.facebook.com"
# data = { "p":"himanshu","m":"manish"}
# r2 = requests.post(url=url,data=data)
# print(r2.text)
print("hello")
import json
r = '{"k":"himanshu","m":"manish"}'
t = json.dumps(r)
print(t["k"])
