from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.image import Image
from source.network import generate_ai
from source.market import Market
from source.user import User
import matplotlib.pyplot as plt


class MainScreen(Screen):
    """
    UI of main page
    """
    pass


class ProfileScreen(Screen):
    """
    UI of profile page
    """
    pass


class CurrentCompanyLabel(Label):
    """
    UI element which represents currently chosen company
    """
    company = StringProperty("AAPL")

    def __init__(self, **kwargs):
        super(CurrentCompanyLabel, self).__init__(**kwargs)
        self.text = "Company: " + self.company
        self.font_size = '20sp'
        self.pos_hint = {'right': 1.35, 'top': 1.2}
        self.bind(company=self.update)

    def update(self, *args, **kwargs):
        self.text = "Company: " + self.company


class CompanyStocks(Label):
    quantity = StringProperty("0")
    company = StringProperty("")

    def __init__(self, **kwargs):
        super(CompanyStocks, self).__init__(**kwargs)
        self.text = self.company + ": " + self.quantity
        self.bind(quantity=self.update)

    def update(self, *args, **kwargs):
        self.text = self.company + ": " + self.quantity


class BalanceLabel(Label):
    """
    UI element which represents current user's money
    """
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
    """
    UI element which shows currently chosen companies's price
    """
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
    """
    Graph used in UI
    """
    def __init__(self, **kwargs):
        super(Graph, self).__init__(**kwargs)
        Clock.schedule_interval(lambda dt: self.reload(), 2)


class StockSimApp(App):
    """
    Main app class
    """
    def __init__(self):
        super(StockSimApp, self).__init__()

        self.ais, mrkt = generate_ai()
        self.market = Market(mrkt)
        self.market.add_ais(self.ais)
        self.user = User(self.market)
        self.current_company = "AAPL"
        self.current_price = str(float(self.market.basic["AAPL"][-1]))
        self.generate_graph(self.current_company)

    def start(self):
        """
        Starts main program loop
        """
        Clock.schedule_interval(lambda dt: self.main_loop(self.market), 2)

    def main_loop(self, market):
        """
        Main program's loop
        :param market: dict - basic market data
        """
        for each in market.ais:
            choice = each.choice(market.basic)
            if len(choice.keys()) > 0:
                for key in market.active_offers.keys():
                    market.active_offers[key].append(choice[key])
        market.calculate()
        for each in self.market.companies:
            self.user.want_to_sell[each] = 0
        self.generate_graph(self.current_company)

    def generate_graph(self, company):
        """
        Creates new graph
        :param company: str - company's name
        """
        plt.style.use('dark_background')
        plt.plot(self.market.basic[company],
                 color='#A967D5',
                 marker='o',
                 linewidth=2,
                 markersize=5)
        plt.savefig('graph.jpg')
        plt.clf()

    def build(self):
        """
        Draws UI
        """
        Config.set('graphics', 'fullscreen', 'auto')
        Config.write()
        screenmanager = ScreenManager()
        screenmanager.add_widget(MainScreen())
        screenmanager.add_widget(ProfileScreen())
        self.start()
        return screenmanager


if __name__ == '__main__':
    StockSimApp().run()
