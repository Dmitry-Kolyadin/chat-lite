import threading, random
import requests
import json

shab = {
    "httpMethod": "POST",
    "headers": {
        "Accept": "*/*",
        "Content-Length": "13",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "curl/7.58.0",
        "X-Real-Remote-Address": "[88.99.0.24]:37310",
        "X-Request-Id": "cd0d12cd-c5f1-4348-9dff-c50a78f1eb79",
        "X-Trace-Id": "92c5ad34-54f7-41df-a368-d4361bf376eb"
    },
    "path": "",
    "multiValueHeaders": {
        "Accept": [
            "*/*"
        ],
        "Content-Length": [
            "13"
        ],
        "Content-Type": [
            "application/x-www-form-urlencoded"
        ],
        "User-Agent": [
            "curl/7.58.0"
        ],
        "X-Real-Remote-Address": [
            "[88.99.0.24]:37310"
        ],
        "X-Request-Id": [
            "cd0d12cd-c5f1-4348-9dff-c50a78f1eb79"
        ],
        "X-Trace-Id": [
            "92c5ad34-54f7-41df-a368-d4361bf376eb"
        ]
    },
    "queryStringParameters": {
        "a": "2",
        "b": "1"
    },
    "multiValueQueryStringParameters": {
        "a": [
            "1",
            "2"
        ],
        "b": [
            "1"
        ]
    },
    "requestContext": {
        "identity": {
            "sourceIp": "88.99.0.24",
            "userAgent": "curl/7.58.0"
        },
        "httpMethod": "POST",
        "requestId": "cd0d12cd-c5f1-4348-9dff-c50a78f1eb79",
        "requestTime": "26/Dec/2019:14:22:07 +0000",
        "requestTimeEpoch": 1577370127
    },
    "body": {"new_akkaynt": 0, "login": "login", "password": "pass", "new_devais": 1, "name_devais": "ffff"},
    "isBase64Encoded": 1
}

data = {"new_akkaynt": 0, "login": "login", "password": "pass", "new_devais": 1, "name_devais": "ffff"}

#data=json.dumps(data)
#shab['body']=data
url = 'https://functions.yandexcloud.net/d4enqmko3pkmobp9n74m'
#print(data['new_akkaynt'])Content-Type: application/json
print(type(shab))
r = requests.post(url, data = shab, json=data)
print(r)
print(r.text)
print(type(r.text))










#'PDTI3oNeFVjPhtcOv9Oh'
#sR2SheJG6g8zuYFOUQeMB1mJMSL2VjTYilVw9Pob
