from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.boxlayout import BoxLayout
import boto3
import threading
import json
import time
i = ''
from kivy.clock import Clock
queue_msg = []
if 1:#мой
    lisurlqeue = 'https://message-queue.api.cloud.yandex.net/b1ggqans59j5o7kc2tbt/dj6000000000tg6p05i6/test'
    senduriqueue='https://message-queue.api.cloud.yandex.net/b1ggqans59j5o7kc2tbt/dj6000000000thtg05i6/test2'

if 1:#вася
    senduriqueue = 'https://message-queue.api.cloud.yandex.net/b1ggqans59j5o7kc2tbt/dj6000000000tg6p05i6/test'
    lisurlqeue='https://message-queue.api.cloud.yandex.net/b1ggqans59j5o7kc2tbt/dj6000000000thtg05i6/test2'
#botocore.exceptions.EndpointConnectionError
AWS_ACCESS_KEY_ID="PDTI3oNeFVjPhtcOv9Oh"
AWS_SECRET_ACCESS_KEY="sR2SheJG6g8zuYFOUQeMB1mJMSL2VjTYilVw9Pob"




def dddd():
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
                    queue_msg.append(json.loads(mspitngjdrfhgwdswwww)['text'])

                # Delete processed messages
                for msg in messages:
                    client.delete_message(
                        QueueUrl=queue_urlt2,
                        ReceiptHandle=msg.get('ReceiptHandle')
                    )
                    print('Вы получили сообщение')




threading.Thread(target=dddd).start()



def sendmsmmmm(msg):
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
    # Send message to queue
    jfnjvdgjfjfikllll={'text':str(msg)}
    clientm.send_message(
    QueueUrl=queue_urltest,
        MessageBody=json.dumps(jfnjvdgjfjfikllll)
        )
    print('Отправленно')































def change_text(labels, period, new_text):
    def rekyrsss():
        if queue_msg:
            ms = queue_msg[0]
            queue_msg.pop(0)
            labely = Label(text=str(ms) ,
                          size_hint=(.5, .5),
                          pos_hint={'center_x': .5, 'center_y': .5})
            labels.add_widget(labely)
    rekyrsss()
    Clock.schedule_once(lambda _: change_text(labels, period, new_text), period)





class MyApp(App):
    def build(self):

        skren1 = BoxLayout()
        if 1:#bokovie
            bokovie = BoxLayout(orientation='vertical',size_hint=(1, .25))
            skren1.add_widget(bokovie)
        if 1:#osnov
            osnov = BoxLayout(orientation='vertical',size_hint=(1, 1))
            if 1:#osnovup
                osnovup = BoxLayout(orientation='vertical',size_hint=(1, 1))
                skren1.add_widget(osnovup)
            if 1:#osnovdown
                osnovdown = BoxLayout(orientation='vertical',size_hint=(1, 1))
                t=TextInput(size_hint=(1, .25),text=i, multiline=False)
                osnovdown.add_widget(t)


                skren1.add_widget(osnovdown)
            if 1:#osnovchat
                osnovchat = BoxLayout(orientation='vertical',size_hint=(1, 1))

                labels = BoxLayout(orientation='vertical')
                osnovchat.add_widget(labels)

                skren1.add_widget(osnovchat)


            skren1.add_widget(osnov)


        def  on_enter (instance ,):
                print ('пользователь нажал enter in' ,  instance.text )
                sendmsmmmm(instance.text)

                labely = Label(text='You: '+instance.text ,
                              size_hint=(.5, .5),
                              pos_hint={'center_x': .5, 'center_y': .5})
                labels.add_widget(labely)
                t.text = ''
        def  addskr (txt):
                print ('msg ^ ' , text )
                labely = Label(text=text ,
                              size_hint=(.5, .5),
                              pos_hint={'center_x': .5, 'center_y': .5})
                labels.add_widget(labely)


        t.bind(on_text_validate=on_enter)
        layout = BoxLayout(orientation='vertical')
        label1 = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
        labels.add_widget(label1)
        layout.add_widget(labels)

        change_text(labels, period=0.5, new_text='B')
        return skren1

if __name__ == '__main__':
    app = MyApp()
    app.run()
