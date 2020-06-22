import threading, random
import requests
AWS_ACCESS_KEY_ID="PDTI3oNeFVjPhtcOv9Oh"
AWS_SECRET_ACCESS_KEY="sR2SheJG6g8zuYFOUQeMB1mJMSL2VjTYilVw9Pob"
data = {'QueueUrl':'https://message-queue.api.cloud.yandex.net/b1ggqans59j5o7kc2tbt/dj6000000000tg6p05i6/test',
        'MessageBody':'https://message-queue.api.cloud.yandex.net/b1ggqans59j5o7kc2tbt/dj6000000000tg6p05i6/test',
        'Content-Type':'application/x-www-form-urlencoded',
        'Action':'SendMessage',
        'Authorization':{'AWS_ACCESS_KEY_ID':AWS_ACCESS_KEY_ID,
                        "AWS_SECRET_ACCESS_KEY":AWS_SECRET_ACCESS_KEY}}

#r = requests.post('https://message-queue.api.cloud.yandex.net/b1ggqans59j5o7kc2tbt/dj6000000000tg6p05i6/test?Action=ReceiveMessage',
#    data = data)

url = 'https://message-queue.api.cloud.yandex.net/'
headers = {'Content-Type':'application/x-www-form-urlencoded',
                }
r = requests.post(url, headers=headers, data = data)

#r = requests.post('https://message-queue.api.cloud.yandex.net/',
#    data = data)




print(r.text)
















































#'PDTI3oNeFVjPhtcOv9Oh'
#sR2SheJG6g8zuYFOUQeMB1mJMSL2VjTYilVw9Pob
