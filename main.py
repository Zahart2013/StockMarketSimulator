from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.image import Image
from network import generate_ai
from market import Market
from copy import copy
from user import User
import matplotlib.pyplot as plt


class MainScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class CurrentCompanyLabel(Label):
    company = StringProperty("AAPL")

    def __init__(self, **kwargs):
        super(CurrentCompanyLabel, self).__init__(**kwargs)
        self.text = "Company: " + self.company
        self.font_size = '20sp'
        self.pos_hint = {'right': 1.35, 'top': 1.2}
        self.bind(company=self.update)

    def update(self, *args, **kwargs):
        self.text = "Company: " + self.company


class BalanceLabel(Label):
    balance = StringProperty("5000")

    def __init__(self, **kwargs):
        super(BalanceLabel, self).__init__(**kwargs)
        self.text = "Balance: " + self.balance
        self.font_size = '20sp'
        self.pos_hint = {'right': .65, 'top': 1.4}
        self.bind(balance=self.update)

    def update(self, *args, **kwargs):
        self.text = "Balance " + self.balance


class CurrentPriceLabel(Label):
    price = StringProperty()

    def __init__(self, **kwargs):
        super(CurrentPriceLabel, self).__init__(**kwargs)
        self.text = "Price: " + self.price
        self.font_size = '20sp'
        self.pos_hint = {'right': 1.35, 'top': 1.15}
        self.bind(price=self.update)

    def update(self, *args, **kwargs):
        self.text = "Price: " + self.price


class Graph(Image):
    def __init__(self, **kwargs):
        super(Graph, self).__init__(**kwargs)
        Clock.schedule_interval(lambda dt: self.reload(), 2)


class StockSimApp(App):
    def __init__(self):
        super(StockSimApp, self).__init__()
        self.market = Market()
        self.ais = generate_ai()
        self.market.add_ais(self.ais)
        for each in self.market.ais:
            each.market = copy(self.market.basic)
        self.user = User(self.market)
        self.current_company = "AAPL"
        self.current_price = str(float(self.market.basic["AAPL"][-1]))
        self.generate_graph(self.current_company)

    def start(self):
        Clock.schedule_interval(lambda dt: self.main_loop(self.market), 2)

    def main_loop(self, market):
        for each in market.ais:
            choice = each.choice(market.basic)
            if len(choice.keys()) > 0:
                for key in market.active_offers.keys():
                    market.active_offers[key].append(choice[key])
        market.calculate()
        self.generate_graph(self.current_company)
        print(self.market.active_offers)

    def generate_graph(self, company):
        plt.style.use('dark_background')
        plt.plot(self.market.basic[company],
                 color='#A967D5',
                 marker='o',
                 linewidth=2,
                 markersize=5)
        plt.savefig('graph.jpg')
        plt.clf()

    def build(self):
        Config.set('graphics', 'fullscreen', 'auto')
        Config.write()
        screenmanager = ScreenManager()
        screenmanager.add_widget(MainScreen())
        screenmanager.add_widget(ProfileScreen())
        self.start()
        return screenmanager


if __name__ == '__main__':
    StockSimApp().run()
