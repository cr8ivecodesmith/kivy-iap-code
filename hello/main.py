import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.button import Label


class HelloApp(App):
    def build(self):
        return Label(text='Hello world!')


if __name__ == '__main__':
    HelloApp().run()
