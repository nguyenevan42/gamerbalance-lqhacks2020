import kivy 
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    print('Liquid Hacks 2020')

    def build(self):
        return Label(text="Hello World")

if __name__ == '__main__':
    MyApp().run()

