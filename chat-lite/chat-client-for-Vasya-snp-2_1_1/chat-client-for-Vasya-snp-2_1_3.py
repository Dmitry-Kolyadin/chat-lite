import boto3
import threading
import json
import time
senduriqueue = 'https://message-queue.api.cloud.yandex.net/b1ggqans59j5o7kc2tbt/dj6000000000tg6p05i6/test'
lisurlqeue='https://message-queue.api.cloud.yandex.net/b1ggqans59j5o7kc2tbt/dj6000000000thtg05i6/test2'
#botocore.exceptions.EndpointConnectionError
AWS_ACCESS_KEY_ID="ElDANOXYwqD2hRUJzXyA"
AWS_SECRET_ACCESS_KEY="wjie71VccwqK46r11-6Q4osRbxfkX3fPwowtFnC5"
while 1:
    try:
        def main():
            # Create client
            clientm = boto3.client(
                service_name='sqs',
                endpoint_url='https://message-queue.api.cloud.yandex.net',
                region_name='ru-central1',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )
            # Create queue and get its url
            queue_urltest = senduriqueue
            print('Подключенно')
            jfnjvdgjfjfikllll={'text':input('Ваш текст: ')}
            while 1:
                # Send message to queue
                jfnjvdgjfjfikllll={'text':input('Ваш текст: ')}
                clientm.send_message(
                    QueueUrl=queue_urltest,
                    MessageBody=json.dumps(jfnjvdgjfjfikllll)
                )
                print('Отправленно')

        def listen():
            # Create client
            client = boto3.client(
                service_name='sqs',
                endpoint_url='https://message-queue.api.cloud.yandex.net',
                region_name='ru-central1',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY
            )

            # Create queue and get its url
            queue_urlt2 = lisurlqeue
            print('()Подключенно')
            # Receive sent message
            while 1:

                messages = client.receive_message(
                    QueueUrl=queue_urlt2,
                    MaxNumberOfMessages=10,
                    VisibilityTimeout=60,
                    WaitTimeSeconds=20
                ).get('Messages')
                if messages:
                    for msg in messages:
                        mspitngjdrfhgwdswwww=msg.get('Body')
                        print('--'+json.loads(mspitngjdrfhgwdswwww)['text'])

                    # Delete processed messages
                    for msg in messages:
                        client.delete_message(
                            QueueUrl=queue_urlt2,
                            ReceiptHandle=msg.get('ReceiptHandle')
                        )
                        print('Вы получили сообщение')
        threading.Thread(target=listen).start()
        main()
        #pyinstaller -F chat-client-for-Vasya-snp-2_1_1.py
    except:
        print('Нет подключения к интернету повторная попытка через 30 секунд!')
        time.sleep(30)
