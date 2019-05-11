import network
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import StringProperty


class MainScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class StockSimApp(App):
    def build(self):
        Config.set('graphics', 'fullscreen', 'auto')
        Config.write()
        screenmanager = ScreenManager()
        screenmanager.add_widget(MainScreen(name="main"))
        screenmanager.add_widget(ProfileScreen(name="profile"))
        return screenmanager

StockSimApp().run()