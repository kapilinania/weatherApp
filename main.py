import requests
import json
import pyttsx3

city = str(input("Enter the name of your city :"))
url = f"http://api.weatherapi.com/v1/current.json?key=b28ec9723517432fb7c141702231907&q={city}"
r = requests.get(url)
# print(r.text)
# print(type(r.text))
dictCity = json.loads(r.text)
a = dictCity["current"]['temp_c']
engine = pyttsx3.init()
engine.say(f'your Current city is {city} and temperature is {a} degrees .')
engine.runAndWait()

