import random
from source.training_data import generate


class AI:
    def __init__(self, market, weights=None):
        self.stocks = dict()
        for each in market.keys():
            self.stocks[each] = 0
        self.money = 8000
        if not weights:
            self._weights = [random.random() for i in range(30)]
        else:
            self._weights = weights

    def train(self, training_input, training_output, loop):
        """
        Training script of AI
        :param training_input: list - training input sequences
        :param training_output: list - training output sequences
        :param loop: int - number of times to repeat training process
        """
        for i in range(loop):
            for j in range(len(training_input)):
                prediction = self._feedforward(training_input[j])
                if prediction != 0:
                    self._change_weights(prediction, training_output[j])
        print("Training finished!")

    def predict(self, market):
        """
        Makes prediction for 10 days
        :param market: dict - current data about market
        :return: number - percent of change for price
        """
        prediction = dict()
        for company in market.keys():
            prediction[company] = self._feedforward(market[company]) * 200 / (float(market[company][-1]) / 100) - 100
        return prediction

    def _feedforward(self, info):
        input_neurons = info
        z = 0
        for i in range(len(self._weights)):
            z += float(input_neurons[i])/200 * self._weights[i]
        if z <= 0:
            return 0
        else:
            return z

    def _change_weights(self, prediction, actual):
        print("Error " + str(prediction*200-actual))
        for index in range(len(self._weights)):
            change = (actual/200-prediction)*self._weights[index]
            self._weights[index] += 10 ** (-4) * change

    def choice(self, market):
        """
        Generates choices for AI
        :param market: dict - current data about market
        :return: list - data about choice of AI
        """
        prediction = self.predict(market)
        operation = dict()
        for company in prediction.keys():
            operation[company] = [self, 0, 0]

            if prediction[company] >= 20:
                price = round(market[company][-1]*(random.randint(100, 130)/100), 2)
                quantity = 100
                if self.money >= price*quantity:
                    operation[company] = [self, price, 50]
                elif self.money >= price*quantity/2:
                    operation[company] = [self, price, 25]
                else:
                    operation[company] = [self, market[company][-1], self.money//market[company][-1]]

            elif prediction[company] >= 15:
                price = round(market[company][-1] * (random.randint(100, 120) / 100), 2)
                quantity = random.randint(20, 50)
                if self.money >= price*quantity:
                    operation[company] = [self, price, quantity]
                elif self.money >= price*quantity/2:
                    operation[company] = [self, round(price/2, 2), quantity]
                elif self.money >= price*quantity/4:
                    operation[company] = [self, round(price / 2, 2), quantity//2]
                else:
                    operation[company] = [self, market[company][-1], self.money // market[company][-1]]

            elif prediction[company] >= 10:
                price = round(market[company][-1] * (random.randint(90, 110) / 100), 2)
                quantity = random.randint(10, 30)
                if self.money >= price * quantity:
                    operation[company] = [self, price, quantity]
                elif self.money >= price * quantity / 2:
                    operation[company] = [self, round(price / 2, 2), quantity]
                elif self.money >= price * quantity / 4:
                    operation[company] = [self, round(price / 2, 2), quantity // 2]
                else:
                    operation[company] = [self, market[company][-1], self.money // market[company][-1]]

            elif prediction[company] >= 5:
                price = round(market[company][-1] * (random.randint(90, 110) / 100), 2)
                quantity = random.randint(5, 25)
                if self.money >= price * quantity:
                    operation[company] = [self, price, quantity]
                elif self.money >= price * quantity / 2:
                    operation[company] = [self, round(price / 2, 2), quantity]
                elif self.money >= price * quantity / 4:
                    operation[company] = [self, round(price / 2, 2), quantity // 2]
                else:
                    operation[company] = [self, market[company][-1], self.money // market[company][-1]]

            elif prediction[company] >= 2.5:
                if random.randint(1, 2) == 1:
                    price = round(market[company][-1] * (random.randint(80, 110) / 100), 2)
                    quantity = random.randint(5, 20)
                    if self.money >= price * quantity:
                        operation[company] = [self, price, quantity]
                    elif self.money >= price * quantity / 2:
                        operation[company] = [self, round(price / 2, 2), quantity]
                    elif self.money >= price * quantity / 4:
                        operation[company] = [self, round(price / 2, 2), quantity // 2]
                    else:
                        operation[company] = [self, market[company][-1], self.money // market[company][-1]]
                else:
                    price = round(market[company][-1] * (random.randint(100, 130) / 100), 2)
                    quantity = random.randint(int(-self.stocks[company]//6), int(-self.stocks[company]//10))
                    operation[company] = [self, price, quantity]

            elif prediction[company] >= 1:
                if random.randint(1, 2) == 1:
                    price = round(market[company][-1] * (random.randint(90, 120) / 100), 2)
                    quantity = random.randint(0, 10)
                    if self.money >= price * quantity:
                        operation[company] = [self, price, quantity]
                    elif self.money >= price * quantity / 2:
                        operation[company] = [self, round(price / 2, 2), quantity]
                    elif self.money >= price * quantity / 4:
                        operation[company] = [self, round(price / 2, 2), quantity // 2]
                    else:
                        operation[company] = [self, market[company][-1], self.money // market[company][-1]]
                else:
                    price = round(market[company][-1] * (random.randint(80, 110) / 100), 2)
                    quantity = random.randint(int(-self.stocks[company]//4), int(-self.stocks[company]//10))
                    operation[company] = [self, price, quantity]

            elif prediction[company] >= -0.5:
                if random.randint(1, 4) == 1:
                    price = round(market[company][-1] * (random.randint(70, 110) / 100), 2)
                    quantity = random.randint(0, 10)
                    if self.money >= price * quantity:
                        operation[company] = [self, price, quantity]
                    elif self.money >= price * quantity / 2:
                        operation[company] = [self, round(price / 2, 2), quantity]
                    elif self.money >= price * quantity / 4:
                        operation[company] = [self, round(price / 2, 2), quantity // 2]
                    else:
                        operation[company] = [self, market[company][-1], self.money // market[company][-1]]
                else:
                    price = round(market[company][-1] * (random.randint(80, 100) / 100), 2)
                    quantity = random.randint(int(-self.stocks[company]//4), int(-self.stocks[company]//8))
                    operation[company] = [self, price, quantity]

            elif prediction[company] >= -2.5:
                if random.randint(1, 4) == 1:
                    price = round(market[company][-1] * (random.randint(60, 100) / 100), 2)
                    quantity = random.randint(0, 5)
                    if self.money >= price * quantity:
                        operation[company] = [self, price, quantity]
                    elif self.money >= price * quantity / 2:
                        operation[company] = [self, round(price / 2, 2), quantity]
                    elif self.money >= price * quantity / 4:
                        operation[company] = [self, round(price / 2, 2), quantity // 2]
                    else:
                        operation[company] = [self, market[company][-1], self.money // market[company][-1]]
                else:
                    price = round(market[company][-1] * (random.randint(80, 100) / 100), 2)
                    quantity = random.randint(int(-self.stocks[company]//4), int(-self.stocks[company]//6))
                    operation[company] = [self, price, quantity]

            elif prediction[company] >= -5:
                if random.randint(1, 6) == 1:
                    price = round(market[company][-1] * (random.randint(60, 80) / 100), 2)
                    quantity = random.randint(0, 5)
                    if self.money >= price * quantity:
                        operation[company] = [self, price, quantity]
                    elif self.money >= price * quantity / 2:
                        operation[company] = [self, round(price / 2, 2), quantity]
                    elif self.money >= price * quantity / 4:
                        operation[company] = [self, round(price / 2, 2), quantity // 2]
                    else:
                        operation[company] = [self, market[company][-1], self.money // market[company][-1]]
                else:
                    price = round(market[company][-1] * (random.randint(70, 100) / 100), 2)
                    quantity = random.randint(int(-self.stocks[company]//2), int(-self.stocks[company]//4))
                    operation[company] = [self, price, quantity]

            elif prediction[company] >= -10:
                if random.randint(1, 8) == 1:
                    price = round(market[company][-1] * (random.randint(60, 80) / 100), 2)
                    quantity = random.randint(0, 5)
                    if self.money >= price * quantity:
                        operation[company] = [self, price, quantity]
                    elif self.money >= price * quantity / 2:
                        operation[company] = [self, round(price / 2, 2), quantity]
                    elif self.money >= price * quantity / 4:
                        operation[company] = [self, round(price / 2, 2), quantity // 2]
                    else:
                        operation[company] = [self, market[company][-1], self.money // market[company][-1]]
                else:
                    price = round(market[company][-1] * (random.randint(60, 90) / 100), 2)
                    quantity = random.randint(int(-self.stocks[company]), int(-self.stocks[company]//3))
                    operation[company] = [self, price, quantity]
            else:
                price = round(market[company][-1] * (random.randint(50, 80) / 100), 2)
                quantity = random.randint(int(-self.stocks[company]), int(-self.stocks[company] // 2))
                operation[company] = [self, price, quantity]

            if self.money < 100 and self.stocks[company] > 0:
                price = round(
                    market[company][-1] * (random.randint(90, 110) / 100), 2)
                quantity = random.randint(int(-self.stocks[company]),
                                          int(-self.stocks[company] // 5))
                operation[company] = operation[company] = [self, price, quantity]

        return operation


def generate_ai():
    """
    Generates set of AIs
    :return: list - set of AIs
    """
    ais = []
    prices, results = generate()
    companies = ['AAPL', 'AMD', 'AMZN', "INTC", "MSFT", "CSCO", "GPRO", "NVDA",
                 "FB", "COKE", "WIX", "TSLA", "NTES", "MU", "ROKU", "YAHOY",
                 "UBSFF", "NDAQ", "NICE", "WMT", "BABA", "GOOG", "IBM", 'QCOM',
                 'CMCSA', 'SPLK', "ADSK", "NFLX", "AVGO", "INTU"]
    for n in range(100):
        indexes = []
        for m in range(5):
            indexes.append(random.randint(0, 29))
        ai = AI({'AAPL': [], 'AMD': [], 'AMZN': [], "INTC": [], "MSFT": [],
                 "CSCO": [], "GPRO": [], "NVDA": [], "FB": [], "COKE": [],
                 "WIX": [], "TSLA": [], "NTES": [], "MU": [], "ROKU": [],
                 "YAHOY": [], "UBSFF": [], "NDAQ": [], "NICE": [], "WMT": [],
                 "BABA": [], "GOOG": [], "IBM": [], 'QCOM': [], 'CMCSA': [],
                 'SPLK': [], "ADSK": [], "NFLX": [], "AVGO": [], "INTU": []})
        ai.train([prices[indexes[0]], prices[indexes[1]], prices[indexes[2]], prices[indexes[3]], prices[indexes[4]]], [results[indexes[0]], results[indexes[1]], results[indexes[2]], results[indexes[3]], results[indexes[4]]], 1000 * random.randint(6, 10))
        ais.append(ai)
    mrkt = {companies[index]: prices[index] for index in range(30)}
    print("Generation finished!")
    return ais, mrkt
