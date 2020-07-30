import threading, random
import requests


data = {'QueueUrl':'data'}

url = 'https://functions.yandexcloud.net/d4enqmko3pkmobp9n74m'

r = requests.post(url, data = data)
print(r)
print(r.text)
















































#'PDTI3oNeFVjPhtcOv9Oh'
#sR2SheJG6g8zuYFOUQeMB1mJMSL2VjTYilVw9Pob
