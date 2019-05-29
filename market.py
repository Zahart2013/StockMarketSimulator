from source.marketadt import MarketADT


class Market(MarketADT):
    def __init__(self, mrkt):
        """
        Creates object which contains information about market
        """
        super(Market, self).__init__()
        self.companies = ['AAPL', 'AMD', 'AMZN', "INTC", "MSFT", "CSCO", "GPRO", "NVDA",
                          "FB", "COKE", "WIX", "TSLA", "NTES", "MU", "ROKU", "YAHOY",
                          "UBSFF", "NDAQ", "NICE", "WMT", "BABA", "GOOG", "IBM", 'QCOM',
                          'CMCSA', 'SPLK', "ADSK", "NFLX", "AVGO", "INTU"]
        self.basic = mrkt
        self.active_offers = {company: [[None, self.basic[company][-1], -5000]] for company in self.companies}
        self.ais = []

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
        print(self.active_offers)
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
                            quant = buy
                        else:
                            quant = sell

                        if seller[0] is None:
                            if buyer[0].money >= buyer[1] * buyer[2]:
                                seller[2] += quant
                                buyer[0].money -= quant * float(seller[1])
                                buyer[2] -= quant
                                buyer[0].stocks[company] += quant
                                for j in range(int(quant)):
                                    prices.append(seller[1])
                        else:
                            if buyer[0].money >= buyer[1] * buyer[2]:
                                seller[0].money += quant * float(seller[1])
                                seller[2] += quant
                                seller[0].stocks[company] -= quant
                                buyer[0].money -= quant * float(seller[1])
                                buyer[2] -= quant
                                buyer[0].stocks[company] += quant
                                for j in range(int(quant)):
                                    prices.append(seller[1])

                    if buyer[2] == 0:
                        buyers.remove(buyer)

                if seller[2] == 0:
                    sellers.remove(seller)

            del self.basic[company][0]
            if len(prices) > 0:
                self.basic[company].append(round(sum(prices)/len(prices), 2))
            else:
                self.basic[company].append(self.basic[company][-1])
            self.active_offers[company] = []
