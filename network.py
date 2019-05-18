import random
from training_data import generate


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
        for i in range(loop):
            for j in range(len(training_input)):
                prediction = self._feedforward(training_input[j])
                if prediction != 0:
                    self._change_weights(prediction, training_output[j])
        print("Training finished!")

    def predict(self, market):
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
        prediction = self.predict(market)
        operation = dict()
        for company in prediction.keys():
            operation[company] = [self, 0, 0]
            if prediction[company] >= 20:
                price = round(float(market[company][-1]) * random.randint(120, 130) * 0.01)
                if self.money >= price * 100:
                    operation[company] = [self, price, 100]
                elif price <= self.money:
                    operation[company] = [self, price, self.money // price]
            elif prediction[company] >= 10:
                price = round(float(market[company][-1])*(random.randint(110, 120)*0.01))
                if self.money >= price * 75:
                    operation[company] = [self, price, 75]
                elif price <= self.money:
                    operation[company] = [self, price, self.money // price]
            elif prediction[company] >= 5:
                price = round(float(market[company][-1])*(random.randint(100, 110)*0.01))
                if self.money >= price * 50:
                    operation[company] = [self, price, 50]
                elif price <= self.money:
                    operation[company] = [self, price, self.money // price]
            elif prediction[company] >= 2.5:
                price = round(float(market[company][-1])*(random.randint(100, 110)*0.01))
                if self.money >= price * 25:
                    operation[company] = [self, price, 25]
                elif price <= self.money:
                    operation[company] = [self, price, self.money // price]
            elif prediction[company] >= 1:
                price = round(float(market[company][-1])*(random.randint(90, 100)*0.01))
                if self.money >= price * 10:
                    operation[company] = [self, price, 10]
                elif price <= self.money:
                    operation[company] = [self, price, self.money // price]
            elif prediction[company] >= 0.5:
                price = round(float(market[company][-1])*random.randint(90, 100)*0.01)
                if self.money >= price * 5:
                    operation[company] = [self, price, 5]
                elif price <= self.money:
                    operation[company] = [self, price, self.money // price]
            elif prediction[company] >= 0:
                operation[company] = [self, round(float(market[company][-1])*random.randint(110, 120)*0.01, 2), -(self.stocks[company] // 6)]
            elif prediction[company] >= -0.5:
                operation[company] = [self, round(float(market[company][-1])*random.randint(100, 110)*0.01, 2), -(self.stocks[company] // 6)]
            elif prediction[company] >= -1:
                operation[company] = [self, round(float(market[company][-1])*random.randint(90, 100)*0.01, 2), -(self.stocks[company] // 5)]
            elif prediction[company] >= -1.5:
                operation[company] = [self, round(float(market[company][-1])*random.randint(90, 100)*0.01, 2), -(self.stocks[company] // 5)]
            elif prediction[company] >= -2.5:
                operation[company] = [self, round(float(market[company][-1])*random.randint(80, 90)*0.01, 2), -(self.stocks[company] // 4)]
            elif prediction[company] >= -5:
                operation[company] = [self, round(float(market[company][-1])*random.randint(80, 90)*0.01, 2), -(self.stocks[company] // 2)]
            else:
                operation[company] = [self, round(float(market[company][-1])*random.randint(70, 80)*0.01, 2), -self.stocks[company]]
        return operation


def generate_ai():
    ais = []
    prices, results = generate()
    for n in range(50):
        indexes = []
        for m in range(3):
            indexes.append(random.randint(0, 7))
        ais.append(AI({'AAPL': [], 'AMD': [], 'AMZN': [], "INTC": [], "MSFT": [], "CSCO": [], "GPRO": [], "NVDA": []}))
    for each in ais:
        each.train([prices[indexes[0]], prices[indexes[1]], prices[indexes[2]]], [results[indexes[0]], results[indexes[1]], results[indexes[2]]], 1000 * random.randint(4, 10))
    print("Generation finished!")
    return ais
