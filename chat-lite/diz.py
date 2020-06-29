from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.boxlayout import BoxLayout
import boto3
from kivy.uix.button import Button
import threading
import json
import time
i = ''
from kivy.clock import Clock

class MyApp(App):
    def build(self):

        skren1 = BoxLayout()
        if 1:#bokovie
            bokovie = BoxLayout(orientation='vertical',size_hint=(.15, .15))
            batiidat = Button(text ='Я', font_size ="15sp",

                   background_color =(1, 1, 1, 1),

                   color =(1, 1, 1, 1),

                   # size = (32, 32),

                   # size_hint = (. 2, .2),

                   #pos =(300, 250)]
                   )
            cobesedniki = BoxLayout()
            settings = Button(text ='set', font_size ="15sp",

                   background_color =(1, 1, 1, 1),

                   color =(1, 1, 1, 1),

                   # size = (32, 32),

                   # size_hint = (. 2, .2),

                   #pos =(300, 250)]
                   )


            bokovie.add_widget(batiidat)
            #okovie.add_widget(cobesedniki)
            bokovie.add_widget(settings)
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
                name = Button(text='отпр',
                       size_hint=(.2, 1),
                       pos_hint={'center_x': .5, 'center_y': .5}, font_size ="15sp",

                       background_color =(1, 1, 1, 1),

                       color =(1, 1, 1, 1)
                       )
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
