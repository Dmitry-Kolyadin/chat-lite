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

class MyApp(App):
    def build(self):

        skren1 = BoxLayout()
        if 1:#bokovie
            bokovie = BoxLayout(orientation='vertical',size_hint=(.2, .2))
            name = Label(text='bokovie: ',
                          size_hint=(1, 1),color=[1,0,0,1])
            bokovie.add_widget(name)
            skren1.add_widget(bokovie)
        if 1:#osnov

            if 1:#osnovup
                osnovup = BoxLayout(orientation='vertical')
                name = Label(text='верх',
                              size_hint=(.5, .5),
                              pos_hint={'center_x': .5, 'center_y': .5})
                osnovup.add_widget(name)
            if 1:#osnovchat
                osnovchat = BoxLayout()
                name = Label(text='osnovchat: ',
                              size_hint=(.5, .5),
                              pos_hint={'center_x': .5, 'center_y': .5})
                osnovup.add_widget(name)
                labels = BoxLayout()
                osnovchat.add_widget(labels)


            if 1:#osnovdown
                osnovdown = BoxLayout()
                t=TextInput(text='', multiline=False)
                osnovdown.add_widget(t)
                name = Label(text='отпр',
                              size_hint=(.2, .2),
                              pos_hint={'center_x': .5, 'center_y': .5})
                osnovdown.add_widget(name)
            osnov = BoxLayout(orientation='vertical')
            osnov.add_widget(osnovup)
            osnov.add_widget(osnovchat)
            osnov.add_widget(osnovdown)
            skren1.add_widget(osnov)
        return skren1

if __name__ == '__main__':
    app = MyApp()
    app.run()
