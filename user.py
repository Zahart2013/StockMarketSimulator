class User:
    """
    Represents program's user
    """
    def __init__(self, market):
        self.market = market
        self.stocks = dict()
        self.want_to_sell = dict()
        for each in market.companies:
            self.stocks[each] = 0
            self.want_to_sell[each] = 0
        self.money = 5000


    def buy(self, company, price, amount):
        """
        Process of buying stocks
        :param company: str - company's name
        :param price: float - price
        :param amount: int - quantity of stocks to buy
        """
        print(price)
        print(amount)
        if self.money >= price*amount:
            self.market.active_offers[company].insert(1, [self, price, amount])

    def sell(self, company, price, amount):
        """
        Process of selling stocks
        :param company: str - company's name
        :param price: float - price
        :param amount: int - quantity of stocks to sell
        """
        if amount <= self.stocks[company] and self.want_to_sell[company] + amount <= self.stocks[company]:
            self.market.active_offers[company].insert(1, [self, price, -amount])
            self.want_to_sell[company] += amount
