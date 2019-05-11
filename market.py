import requests
from marketadt import MarketADT
from time import time as t


class Market(MarketADT):
    def __init__(self):
        """
        Creates object which contains information about market
        """
        super(Market, self).__init__()
        self.companies = ['AAPL', 'AMD', 'AMZN', "INTC", "MSFT", "CSCO", "GPRO", "NVDA"]
        self.basic = self.get_basic()
        self.active_offers = {company: [[None, self.basic[company][-1], -5000]] for company in self.companies}
        self.ais = []

    def get_basic(self):
        """
        Generates basic set of information about companies' prices on market
        :return: dict - contains prices for last 30 days for each company
        """
        basic = dict()
        for company in self.companies:
            data = {"function": 'TIME_SERIES_DAILY',
                    "symbol": company,
                    "outputsize": 'compact',
                    "datatype": "json",
                    "apikey": "PCT8XEO3EICMQ5T2"}
            prices = []
            output = requests.get("https://www.alphavantage.co/query", data).json()
            time1 = t()
            while "Note" in output:
                while t()-time1 < 60:
                    continue
                output = requests.get("https://www.alphavantage.co/query",
                                      data).json()
            count = 0
            for time in output['Time Series (Daily)']:
                prices.append(output['Time Series (Daily)'][time]['4. close'])
                count += 1
                if count == 30:
                    break
            prices.reverse()
            basic[company] = prices
        return basic

    def add_ais(self, ais):
        """
        Adds AIs which are players on market
        :param ais: list -
        """
        if type(ais) == list:
            for every in ais:
                self.ais.append(every)
        else:
            self.ais.append(ais)

    def calculate(self):
        """
        Calculates all operations with market's data
        """
        for company in self.active_offers:
            operations = self.active_offers[company]
            sellers = [seller for seller in operations if seller[2] < 0]
            buyers = [buyer for buyer in operations if buyer[2] > 0]
            prices = []
            for seller in sellers:
                for buyer in buyers:
                    if buyer[1] >= float(seller[1]):
                        sell = abs(seller[2])
                        buy = buyer[2]
                        if sell > buy:
                            quant = sell - buy
                        else:
                            quant = sell

                        prices.append(seller[1])
                        if seller[0] is None:
                            seller[2] += quant
                            buyer[0].money -= quant * float(seller[1])
                            buyer[2] -= quant
                            buyer[0].stocks[company] += quant
                        else:
                            seller[0].money += quant * float(seller[1])
                            seller[2] += quant
                            seller[0].stocks[company] -= quant
                            buyer[0].money -= quant * float(seller[1])
                            buyer[2] -= quant
                            buyer[0].stocks[company] += quant

                    if buyer[2] == 0:
                        buyers.remove(buyer)

                if seller[2] == 0:
                    sellers.remove(seller)

            del self.basic[company][0]
            self.basic[company].append(min(prices))
