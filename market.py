import requests
import json
from network import AI
from marketadt import MarketADT


class Market(MarketADT):
    def __init__(self):
        super(Market, self).__init__()
        self.companies = ['AAPL', 'AMD', 'AMZN', 'TSLA']
        self.basic = self.get_basic()
        self.active_offers = {company: [(None, 10000)] for company in self.companies}
        self.ais = []

    def get_basic(self):
        basic = []
        for company in self.companies:
            data = {"function": 'TIME_SERIES_DAILY',
                    "symbol": company,
                    "outputsize": 'compact',
                    "datatype": "json",
                    "apikey": "YGGL6LXB7FIUYNWF"}
            prices = []
            output = requests.get("https://www.alphavantage.co/query", data).json()
            parsed_data = dict()
            for time in output['Time Series (Daily)']:
                parsed_data[time] = dict()
                parsed_data[time]['point'] = float(data['Time Series (Daily)'][time]['4. close'])
            basic.append(parsed_data)
        return basic

    def add_ais(self, ais):
        self.ais = ais

    def calculate(self):
        for company in self.active_offers:
            operations = self.active_offers[company]
            sellers = [seller for seller in operations if seller[3] < 0]
            buyers = [buyer for buyer in operations if buyer[3] < 0]

            prices = []

            while len(sellers) > 0:
                for seller in sellers:
                    for buyer in buyers:
                        if buyer[1] > seller[1]:
                            sell = abs(seller[3])
                            buy = buyer[3]
                            if sell > buy:
                                quant = sell - buy
                            else:
                                quant = sell

                            prices.append(seller[1])
                            seller[0].money += quant * seller[1]
                            seller[2] += quant
                            seller[0].stocks[company] -= quant
                            buyer[0].money -= quant * seller[1]
                            buyer[2] -= quant
                            buyer[0].stocks[company] += quant

                        if buyer[2] == 0:
                            buyers.remove(buyer)

                    if seller[2] == 0:
                        sellers.remove(seller)

            self.basic[company] = min(prices)


mrkt = Market()
print(mrkt.companies)
print(mrkt.basic)

