import threading, random
import requests
import json
url = 'https://functions.yandexcloud.net/d4enqmko3pkmobp9n74m?integration=raw'


send={
    'new_akkaynt':0,
    'login':'login',
    'password':'password',
    'new_devais':1,
    'name_devais':'name_devais',
    }
r = requests.post(url, data = send)
print(r)
print(json.loads(r.text))
print(type(json.loads(r.text)))
