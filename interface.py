from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import StringProperty
from network import AI, generate_ai
from market import Market
from multiprocessing import Process, Manager


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
    market = Market()
    ais = generate_ai()
    market.add_ais(ais)
    for each in market.ais:
        each.market = market.basic
    counter = 0
    while True:
        for each in market.ais:
            choice = each.choice(market.basic)
            if len(choice.keys()) > 0:
                for key in market.active_offers.keys():
                    market.active_offers[key].append(choice[key])
        market.calculate()
        counter += 1
        print(counter)
        if counter == 10:
            print(market.basic)
