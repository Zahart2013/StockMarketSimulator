from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import StringProperty
from network import AI
from kivy.clock import Clock, mainthread
import time
import threading


class MainScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class StockSimApp(App):
    def build(self):
        Config.set('graphics', 'fullscreen', 'auto')
        Config.write()
        screenmanager = ScreenManager()
        screenmanager.add_widget(MainScreen())
        screenmanager.add_widget(ProfileScreen())
        return screenmanager


if __name__ == '__main__':
    app = StockSimApp()
    app.run()
