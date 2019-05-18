class User:
    def __init__(self, market):
        self.market = market
        self.stocks = dict()
        for each in market.companies:
            self.stocks[each] = 0
        self.money = 5000

    def buy(self, company, price, amount):
        print(price)
        print(amount)
        if self.money >= price*amount:
            self.market.active_offers[company].insert(1, [self, price, amount])

    def sell(self, company, price, amount):
        if amount <= self.stocks[company]:
            self.market.active_offers[company].insert(1, [self, price, -amount])
